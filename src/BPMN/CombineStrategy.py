import pandas as pd
import abc


class CombineStrategy():

    @abc.abstractclassmethod
    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        pass
    @abc.abstractclassmethod
    def get_code(self, df_1:str, df_2:str) -> str:
        pass


class ConcatStrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_c = pd.concat([df_1, df_2])
        return df_c
    def get_code(self, df_1:str, df_2:str) -> str:
        return f"#Here we concate two Dataframes\n{df_1} = pd.concat([{df_1},{df_2}])\n"