import pandas as pd
import abc
from BPMN.logger import logger
from BPMN.TransformationStrategy import FilterStrategy


class CombineStrategy():

    @abc.abstractclassmethod
    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        pass

    @abc.abstractclassmethod
    def get_code(self, df_1: str, df_2: str) -> str:
        pass


class ConcatStrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_c = pd.concat([df_1, df_2]).drop_duplicates(keep="first")
        return df_c

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"#Here we concate two Dataframes\n{df_1} = pd.concat([{df_1},{df_2}]).drop_duplicates(keep=True)\n"


class DiffrenceStrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_c = pd.concat([df_1, df_2]).drop_duplicates(keep=False)
        return df_c

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"#Here we concate two Dataframes\n{df_1} = pd.concat([{df_1},{df_2}]).drop_duplicates(keep=False)\n"


class CrossStrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        return df_1.merge(df_2, how="cross")

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#Here we cross two Dataframes\n{df_1} = {df_1}.merge({df_2}, how = "cross")\n"""


class Intersecttrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        return df_1.merge(df_2, on=list(df_1.columns), how="inner")

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#Here we cross two Dataframes\n{df_1} = {df_1}.merge({df_2}, on = list({df_1}.columns) , how = "inner")\n"""


class ThetaStrategy(CombineStrategy):

    def __init__(self, query: str) -> None:
        super().__init__()
        self.query = query
        self.filter = FilterStrategy(query)

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = df_1.merge(df_2, how="cross")
        return self.filter.transform(df_1)

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#Here we do a theta join on {self.query} by  crossing and then querying two Dataframes\n{df_1} = {df_1}.merge({df_2}, how = "cross")\n{self.filter.get_code(df_1)}"""


class JoinOnStrategy(CombineStrategy):

    def __init__(self, on: str, how: str = "inner") -> None:
        super().__init__()
        self.on = on
        self.how = how

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        return df_1.merge(df_2, on=self.on, how=self.how)

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#Here we {self.how }join on {self.on} two Dataframes\n{df_1} = {df_1}.merge({df_2}, on = "{self.on}",  how="{self.how}")\n"""


class NaturaljoinStrategy(CombineStrategy):
    def __init__(self, _index: bool = False) -> None:
        super().__init__(self)
        self.index = _index

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        try:
            if self._index:
                return df_1.join(df_2)
            else:
                return df_1.merge(df_2)
        except Exception:
            logger.warning(f"Natural Join failed return cross product")
            return df_1.merge(df_2, how="cross")

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#trying to do a natural join on {"index" if self._index else "columns"}
try:
    {df_1+"="+df_1+".join("+df_2+")" if self._index else df_1+"="+df_1+".merge("+df_2+")"}
except Exception:
    {df_1} = {df_1}.merge({df_2}, how = "cross")
"""


class EquijoinStrategy(CombineStrategy):
    def __init__(self, right: str, left: str, how: str = "inner") -> None:
        super().__init__()
        self.how = how
        self.right = right
        self.left = left

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        return df_1.merge(df_2, left_on=self.left, right_on=self.right, how=self.how)

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#Here we make an equi join two Dataframes\n{df_1} = {df_1}.merge({df_2},left_on="{self.left}", right_on="{self.right}", how="{self.how}")\n"""
