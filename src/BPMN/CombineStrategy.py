import pandas as pd
import abc


class CombineStrategy():

    @abc.abstractclassmethod
    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        pass


class ConcatStrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_c = pd.concat([df_1, df_2])
        return df_c