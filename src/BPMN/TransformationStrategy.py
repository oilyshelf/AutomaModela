from typing import List
from BPMN.logger import logger
import pandas as pd
import abc


# abstract base class
class TransformationStrategy():

    @abc.abstractclassmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

    @abc.abstractclassmethod
    def get_code(self, df_name: str) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


# special functions
class DoNothingStrategy(TransformationStrategy):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df

    def get_code(self, df_name: str) -> str:
        return f"# fyi here was called a Do Nothing call on {df_name}\n"


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

# load and save


class LoadExcelStrategy(TransformationStrategy):

    def __init__(self, file_name: str, **kwargs):
        self.file_name = file_name
        self.sheet_name = kwargs.get("sheetname", 0)
        self.index = kwargs.get("index", None)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return pd.read_excel(self.file_name, sheet_name=self.sheet_name, index_col=self.index)

    def get_code(self, df_name: str) -> str:
        return f"""
#here we read the data provided by the {self.file_name} from the sheet {self.sheet_name if type(self.sheet_name) != int else "number"+str(self.sheet_name)} and set the index to {self.index}
{df_name} = pd.read_excel("{self.file_name}", sheet_name = {self.sheet_name if type(self.sheet_name) == int else "'"+self.sheet_name+"'"}{f', index_col = "'+self.index+'"' if self.index is not None else ""})
"""


class SaveExcelStrategy(TransformationStrategy):

    def __init__(self, file_name: str, **kwargs):
        self.file_name = file_name
        self.sheet_name = kwargs.get("sheetname", "Sheet1")
        self.index = True if kwargs.get("index", False) == "True" else False

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df.to_excel(self.file_name, index=self.index, sheet_name=self.sheet_name)
        return df

    def get_code(self, df_name: str) -> str:
        return f"""
#here we save the data from {df_name} to the the {self.file_name} into the  sheet {self.sheet_name} and {"use" if self.index else "dont use"} the index
{df_name}.to_excel("{self.file_name}", sheet_name = "{self.sheet_name}", index = {self.index})
"""

# views


class FilterStrategy(TransformationStrategy):

    def __init__(self, query: str):
        self.query = query
        self.engines = [{"engine": "numexpr"}, {"engine": "python"}]

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        for e in self.engines:
            try:
                df = df.query(self.query, **e)
                return df
            except Exception:
                logger.warning(f"{e} didn't work on quering {self.eval_string} trying next engine")
        return pd.DataFrame(columns=df.columns)

    def get_code(self, df_name: str) -> str:
        return f"""#Here we try to query the Expression {self.query} with diffrent engines
for engine in {self.engines}:
    try:
        {df_name} = {df_name}.query('{self.query}', **engine)
    except Exception:
        print(engine, "failed to query", '{self.query}', "trying next")
"""


class SelectStrategy(TransformationStrategy):

    def __init__(self, cols: List[str]) -> None:
        self.cols = cols

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


class deleteData(TransformationStrategy):

    def __init__(self, **kwargs) -> None:
        self.keep = kwargs.get("keepCols", False)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.keep:
            return df[0:0]
        return pd.DataFrame()

    def get_code(self, df_name: str) -> str:
        return f"#delete all data keep structure\n{df_name}[0:0]" if self.keep else f"#delete dataframe completly by creating a new one\n{df_name} = pd.DataFrame()"


# updates row based
class addRow(TransformationStrategy):

    def __init__(self, *args, **kwargs) -> None:
        if args:
            self.order = True
            self.tba = args
        elif kwargs:
            self.order = False
            self.tba = {key: [entry] for key, entry in kwargs.items()}

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


class deleteRow(TransformationStrategy):

    def __init__(self, *args, **kwargs) -> None:
        self.engines = [{"engine": "numexpr"}, {"engine": "python"}]
        if args:
            self.order = True
            self.tbd = args
        elif kwargs:
            self.order = False
            self.tbd = " and ".join([f"""({key} == {entry if type(entry) is not str else '"'+entry+'"' })""" for key, entry in kwargs.items()])

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        if self.order:
            self.tbd = " and ".join(f"""({key} == {entry if type(entry) is not str else '"'+entry+'"' })""" for key, entry in dict(zip(df.columns, self.tbd)).items())
        return FilterStrategy(f" not ({self.tbd})").transform(df)

    def get_code(self, df_name: str) -> str:
        return f"""#delete row by filtering the invers
if {self.order}:
    del = '"'
    filter = " and ".join(f"({{key}} == {{entry if type(entry) is not str else del+entry+del}})" for key, entry in dict(zip(df.columns, {self.tba})).items())
else:
    filter = {self.tba}
# filter 
for engine in {self.engines}:
    try:
        {df_name} = {df_name}.query(f'not ({{filter}})', **engine)
    except Exception:
        print(engine, "failed to query", f'not ({{filter}})', "trying next")
"""


class changeRow(TransformationStrategy):

    def __init__(self, cur: List | dict, new_v: List | dict) -> None:
        if type(cur) == dict:
            self.cur = deleteRow(**cur)
            self.new_v = addRow(**new_v)
        else:
            self.cur = deleteRow(*cur)
            self.new_v = addRow(*new_v)

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
class deleteColumn(TransformationStrategy):

    def __init__(self, col: str) -> None:
        self.tbd = col

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.drop(self.tbd, axis=1)

    def get_code(self, df_name: str) -> str:
        return f"#delete column\n{df_name} = {df_name}.drop('{self.tbd}', axis = 1)"


class evalStrategy(TransformationStrategy):
    def __init__(self, eval_string: str):
        self.eval_string = eval_string
        self.engines = [{}, {"engine": "python"}]

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:

        for engine in self.engines:
            try:
                df = df.eval(self.eval_string, **engine)
                return df
            except Exception:
                logger.warning(f"{engine} didn't work on eval {self.eval_string} trying next engine")
        return df

    def get_code(self, df_name: str) -> str:
        return f"""#Here we try to evaluate the Expression {self.eval_string} with diffrent engines
for engine in {self.engines}:
    try:
        {df_name} = {df_name}.eval('{self.eval_string}', **engine)
    except Exception:
        print(engine, "failed to evaluate", '{self.eval_string}', "trying next")
"""


class addOrChangeColumn(TransformationStrategy):

    def __init__(self, col: str, value, _isString: bool = False) -> None:
        self.query = f"""`{col}` = {'"'+value+'"' if _isString else value}"""
        self.eval = evalStrategy(self.query)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return self.eval.transform(df)

    def get_code(self, df_name: str) -> str:
        return self.eval.get_code(df_name)
