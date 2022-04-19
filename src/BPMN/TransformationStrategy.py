from BPMN.logger import logger
import pandas as pd
import abc


class TransformationStrategy():

    @abc.abstractclassmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}"


class DoNothingStrategy(TransformationStrategy):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df


class LoadExcelStrategy(TransformationStrategy):

    def __init__(self, file_name: str, **kwargs):
        self.file_name = file_name
        self.sheet_name = kwargs.get("sheetname", 0)
        self.index = kwargs.get("index", None)

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return pd.read_excel(self.file_name, sheet_name=self.sheet_name, index_col=self.index)


class SaveExcelStrategy(TransformationStrategy):

    def __init__(self, file_name: str, **kwargs):
        self.file_name = file_name
        self.sheet_name = kwargs.get("sheetname", "Sheet1")
        self.index = True if kwargs.get("index", False) == "True" else False

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df.to_excel(self.file_name, index=self.index, sheet_name=self.sheet_name)
        return df


class dotStrategy(TransformationStrategy):
    def __init__(self, func_string: str):
        self.func_string = func_string

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        exec_string = f'edf = df{self.func_string}'
        loc = {}
        exec(exec_string, locals(), loc)
        return loc["edf"]


class evalStrategy(TransformationStrategy):
    def __init__(self, eval_string: str):
        self.eval_string = eval_string

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        engines = [{}, {"engine": "python"}]
        for engine in engines:
            try:
                df = df.eval(self.eval_string, **engine)
                return df
            except Exception:
                logger.warning(f"{engine} didn't work on eval {self.eval_string} trying next engine")
        return df


class FilterStrategy(TransformationStrategy):

    def __init__(self, query: str):
        self.query = query

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        engines = [{"engine": "numexpr"}, {"engine": "python"}]
        for e in engines:
            try:
                df = df.query(self.query, **e)
                return df
            except Exception:
                logger.warning(f"{e} didn't work on quering {self.eval_string} trying next engine")
        return pd.DataFrame(columns=df.columns)
