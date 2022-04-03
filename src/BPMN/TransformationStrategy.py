import pandas as pd
import abc


class TransformationStrategy():

    @abc.abstractclassmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


class DoNothingStrategy(TransformationStrategy):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return df


class LoadExcelStrategy(TransformationStrategy):

    def __init__(self, file_name: str):
        self.file_name = file_name

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        return pd.read_excel(self.file_name)


class SaveExcelStrategy(TransformationStrategy):

    def __init__(self, file_name: str):
        self.file_name = file_name

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df.to_excel(self.file_name, index=False)
        return df


class dotStrategy(TransformationStrategy):
    def __init__(self, func_string: str):
        self.func_string = func_string

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        exec_string = f'df = df{self.func_string}'
        exec(exec_string, globals())
