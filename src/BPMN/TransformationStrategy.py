import abc
from typing import List
import numpy as np
import pandas as pd
from BPMN.logger import logger
from BPMN.ExprFuncDefinitions import expr_locals
from BPMN.Strategy import Strategy


# abstract base class
class TransformationStrategy(Strategy):

    @abc.abstractclassmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

    @abc.abstractclassmethod
    def get_code(self, df_name: str) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


# load and save
class LoadExcelStrategy(TransformationStrategy):

    def __init__(self, file_name: str, sheet_name: str | int = 0, index: str | None = None):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.index = index

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = pd.read_excel(self.file_name, sheet_name=self.sheet_name, index_col=self.index)
        df = df.replace({np.nan: None})
        return df

    def get_code(self, df_name: str) -> str:
        return f"""
#here we read the data provided by the {self.file_name} from the sheet {self.sheet_name if type(self.sheet_name) != int else "number "+str(self.sheet_name)} and set the index to {self.index}
{df_name} = pd.read_excel("{self.file_name}", sheet_name = {self.sheet_name if type(self.sheet_name) == int else "'"+self.sheet_name+"'"}{f', index_col = "'+self.index+'"' if self.index is not None else ""})
{df_name} = {df_name}.replace({{np.nan:None}})
"""


class SaveExcelStrategy(TransformationStrategy):

    def __init__(self, file_name: str, sheet_name: str = "Sheet1", impl_bool_3: bool = False):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.index = impl_bool_3

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        ret_df = df.copy()
        for col in df.columns:
            if col.startswith("BACKTICK_QUOTED_STRING_"):
                df.rename(columns={col: col[23:].replace("_", " ")}, inplace=True)

        df.to_excel(self.file_name, index=self.index, sheet_name=self.sheet_name)
        return ret_df

    def get_code(self, df_name: str) -> str:
        return f"""#here we save the data from {df_name} to the the {self.file_name} into the  sheet {self.sheet_name} and {"use" if self.index else "dont use"} the index
for col in {df_name}.columns:
    if col.startswith("BACKTICK_QUOTED_STRING_"):
        {df_name}.rename(columns={{col:col[23:].replace("_", " ")}}, inplace=True)
{df_name}.to_excel("{self.file_name}", sheet_name = "{self.sheet_name}", index = {self.index})
"""


# views
class SelectRowsStrategy(TransformationStrategy):

    def __init__(self, query: str):
        self.query = query
        self.engines = [{"engine": "numexpr"}, {"engine": "python"}]

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        for engine in self.engines:
            try:
                df = df.query(self.query, local_dict=expr_locals, **engine)
                return df
            except Exception as e:
                logger.warning(f"{e}: {engine} didn't work on querying {self.query} trying next engine")
        return pd.DataFrame(columns=df.columns)

    def get_code(self, df_name: str) -> str:
        return f"""#Here we try to query the Expression {self.query} with diffrent engines
for engine in {self.engines}:
    try:
        {df_name} = {df_name}.query('{self.query}', **engine)
    except Exception:
        print(engine, "failed to query", '{self.query}', "trying next")
"""


class SelectColumnStrategy(TransformationStrategy):

    def __init__(self, column: List[str]) -> None:
        self.cols = column

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[self.cols]

    def get_code(self, df_name: str) -> str:
        return f"#we get a subset of the dataframe with these columns {self.cols}\n{df_name} = {df_name}[{self.cols}]\n"


class RenameStrategy(TransformationStrategy):

    def __init__(self, from_col: str, to_col: str) -> None:
        self.mapper = {from_col: to_col}

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.rename(columns=self.mapper)

    def get_code(self, df_name: str) -> str:
        return f'#rename column from-> to {self.mapper}\n{df_name}={df_name}.rename(columns={self.mapper})\n'


class deleteDataStrategy(TransformationStrategy):

    def __init__(self, impl_bool_1: bool = False) -> None:
        self.keep = impl_bool_1

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.keep:
            return df[0:0]
        return pd.DataFrame()

    def get_code(self, df_name: str) -> str:
        return f"#delete all data keep structure\n{df_name}[0:0]" if self.keep else f"#delete dataframe completly by creating a new one\n{df_name} = pd.DataFrame()"


# updates row based
class addRowStrategy(TransformationStrategy):

    def __init__(self, values: List) -> None:
        if type(values[0]) == dict:
            self.order = False
            self.tba = {k: [v] for d in values for k, v in d.items()}
        else:
            self.order = True
            self.tba = values

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.order:
            df.loc[len(df.index)] = self.tba
        else:
            row_df = pd.DataFrame(data=self.tba)
            df = df.append(row_df, ignore_index=True)
        return df

    def get_code(self, df_name: str) -> str:
        if self.order:
            return f"#add row based on args order\n{df_name}.loc[len({df_name}.index)] = {self.tba}"
        return f"#add row based on keywords by creating a temp df\ntemp_df = pd.DataFrame(data = {self.tba})\n{df_name} = {df_name}.append(temp_df, ignore_index = True)"


class deleteRowStrategy(TransformationStrategy):

    def __init__(self, values: List) -> None:
        self.engines = [{"engine": "numexpr"}, {"engine": "python"}]   
        if type(values[0]) == dict:
            self.order = False
            delist = {k: v for d in values for k, v in d.items()}
            self.tbd = " and ".join([f"""(`{key}` == {entry if type(entry) is not str else '"'+entry+'"' })""" for key, entry in delist.items()])
        else:
            self.order = True
            self.tbd = values

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.order:
            self.tbd = " and ".join(f"""(`{key}` == {entry if type(entry) is not str else '"'+entry+'"' })""" for key, entry in dict(zip(df.columns, self.tbd)).items())
        return SelectRowsStrategy(f" not ({self.tbd})").transform(df)

    def get_code(self, df_name: str) -> str:
        comment = "# delete row by filtering the inverse of the provided values\n"
        if self.order:
            filter_part = f"""deli = '"'
filter = " and ".join(f"(`{{key}}` == {{entry if type(entry) is not str else deli+entry+deli}})" for key, entry in dict(zip({df_name}.columns, {self.tbd})).items())
"""
        else:
            filter_part = f"filter = '{self.tbd}'\n"
        query_part = f"""for engine in {self.engines}:
    try:
        {df_name} = {df_name}.query(f'not ({{filter}})', **engine)
    except Exception:
        print(engine, "failed to query", f'not ({{filter}})', "trying next")
"""
        return comment + filter_part + query_part


class changeRowStrategy(TransformationStrategy):

    def __init__(self, org_value: List, new_value: List) -> None:
        self.cur = deleteRowStrategy(org_value)
        self.new_v = addRowStrategy(new_value)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = self.cur.transform(df)
        return self.new_v.transform(df)

    def get_code(self, df_name: str) -> str:
        return f"""#updating values by first deleting and then adding
#deleting
{self.cur.get_code(df_name)}
#adding
{self.new_v.get_code(df_name)}
"""


# updates on cols
class deleteColumnStrategy(TransformationStrategy):

    def __init__(self, column: str) -> None:
        self.tbd = column

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.drop(self.tbd, axis=1)

    def get_code(self, df_name: str) -> str:
        return f"#delete column\n{df_name} = {df_name}.drop('{self.tbd}', axis = 1)"


class setColumnStrategy(TransformationStrategy):

    def __init__(self, column: str, value: str) -> None:
        self.expr = value
        self.col = column
        self.engines = [{}, {"engine": "python"}]
        # logger.warning(f"____________________________________________|{self.expr}|____________________________")

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        for engine in self.engines:
            try:
                df[self.col] = df.eval(self.expr, local_dict=expr_locals, **engine)
                return df
            except Exception:
                logger.warning(f"{engine} didn't work on evaluating {self.expr} trying next engine")
                pass
        raise Exception(f"Transformation failed: not a valid value ({self.expr}) provided")

    def get_code(self, df_name: str) -> str:
        return f"""#Here we try to evaluate the Expression {self.expr} with diffrent engines
for engine in {self.engines}:
    try:
        {df_name}["{self.col}"] = {df_name}.eval('{self.expr}', **engine)
    except Exception:
        print(engine, "failed to evaluate", '{self.expr}', "trying next")
"""


class addColumnStrategy(TransformationStrategy):
    def __init__(self, column: str, value: str) -> None:
        self.setter = setColumnStrategy(column, value)
        self.column = column

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.column in df.columns:
            raise Exception(f"Transformation failed: Column {self.column} already in dataframe")
        return self.setter.transform(df)

    def get_code(self, df_name: str) -> str:
        return self.setter.get_code(df_name)


class changeColumnStrategy(TransformationStrategy):
    def __init__(self, column: str, value: str) -> None:
        self.setter = setColumnStrategy(column, value)
        self.column = column

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.column not in df.columns:
            raise Exception(f"Transformation failed: Column {self.column} not in dataframe")
        return self.setter.transform(df)

    def get_code(self, df_name: str) -> str:
        return self.setter.get_code(df_name)


# special functions
class DoNothingStrategy(TransformationStrategy):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df

    def get_code(self, df_name: str) -> str:
        return f"# fyi here was called a Do Nothing call on {df_name}\n"


class SetIndexStrategy(TransformationStrategy):

    def __init__(self, column: str):
        self.column = column

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.set_index(self.column)

    def get_code(self, df_name: str) -> str:
        return f"# set index to {self.column} in {df_name}\n{df_name}.set_index('{self.column}', inplace = True)"


class ResetIndexStrategy(TransformationStrategy):

    def __init__(self, impl_bool_1: bool = False):
        self.drop = not impl_bool_1

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.reset_index(drop=self.drop)

    def get_code(self, df_name: str) -> str:
        return f"# rest index to in {df_name}\n{df_name}.reset_index(drop = {self.drop}, inplace = True)"


# special special functions
class dotStrategy(TransformationStrategy):
    def __init__(self, func_string: str):
        self.func_string = func_string

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        exec_string = f'edf = df{self.func_string}'
        loc = {}
        exec(exec_string, locals(), loc)
        return loc["edf"]

    def get_code(self, df_name: str) -> str:
        return f"#Here is a call Happing using the dotStrategy aka pure python code beaware\n{df_name} = {df_name}{self.func_string}\n"
