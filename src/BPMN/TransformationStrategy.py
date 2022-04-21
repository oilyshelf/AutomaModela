from typing import List
from BPMN.logger import logger
import pandas as pd
import abc


class TransformationStrategy():

    @abc.abstractclassmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

    @abc.abstractclassmethod
    def get_code(self, df_name:str) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


class DoNothingStrategy(TransformationStrategy):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df
    def get_code(self, df_name:str) -> str:
        return f"# fyi here was called a Do Nothing call on {df_name}\n"


class LoadExcelStrategy(TransformationStrategy):

    def __init__(self, file_name: str, **kwargs):
        self.file_name = file_name
        self.sheet_name = kwargs.get("sheetname", 0)
        self.index = kwargs.get("index", None)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return pd.read_excel(self.file_name, sheet_name=self.sheet_name, index_col=self.index)
    def get_code(self, df_name:str) -> str:
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
    def get_code(self, df_name:str) -> str:
        return f"""
#here we save the data from {df_name} to the the {self.file_name} into the  sheet {self.sheet_name} and {"use" if self.index else "dont use"} the index
{df_name}.to_excel("{self.file_name}", sheet_name = "{self.sheet_name}", index = {self.index})
"""


class dotStrategy(TransformationStrategy):
    def __init__(self, func_string: str):
        self.func_string = func_string

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        exec_string = f'edf = df{self.func_string}'
        loc = {}
        exec(exec_string, locals(), loc)
        return loc["edf"]
    def get_code(self, df_name:str) -> str:
        return f"#Here is a call Happing using the dotStrategy aka pure python code beaware\n{df_name} = {df_name}{self.func_string}\n"


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
    def get_code(self, df_name:str) -> str:
        return f"""#Here we try to evaluate the Expression {self.eval_string} with diffrent engines
for engine in {self.engines}:
    try:
        {df_name} = {df_name}.eval('{self.eval_string}', **engine)
    except Exception:
        print(engine, "failed to evaluate", '{self.eval_string}', "trying next")
"""


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
    def get_code(self, df_name:str) -> str:
        return f"""#Here we try to query the Expression {self.query} with diffrent engines
for engine in {self.engines}:
    try:
        {df_name} = {df_name}.query('{self.query}', **engine)
    except Exception:
        print(engine, "failed to query", '{self.query}', "trying next")
"""

class SelectStrategy(TransformationStrategy):

    def __init__(self, cols:List[str]) -> None:
        self.cols = cols
    
    def transform(self, df:pd.DataFrame)->pd.DataFrame:
        return df[self.cols]
    def get_code(self, df_name:str) -> str:
        return f"#we get a subset of the dataframe with these columns {self.cols}\n{df_name} = {df_name}[{self.cols}]\n"