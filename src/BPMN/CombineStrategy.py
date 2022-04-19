import pandas as pd
import abc


class CombineStrategy():

    @abc.abstractclassmethod
    def combine(self, df_1: pd.DataFrame, df_2:pd.DataFrame) -> pd.DataFrame:
        pass