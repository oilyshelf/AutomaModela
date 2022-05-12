import pandas as pd
import abc
import numpy as np
from BPMN.TransformationStrategy import SelectRowsStrategy

# abstract base class


class CombineStrategy():

    @abc.abstractclassmethod
    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        pass

    @abc.abstractclassmethod
    def get_code(self, df_1: str, df_2: str) -> str:
        pass


# joins
class NaturalJoinStrategy(CombineStrategy):
    def __init__(self, impl_bool_1: bool = False) -> None:
        super().__init__(self)
        self.index = impl_bool_1
        self.how = "inner"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        if self._index:
            return df_1.join(df_2, how=self.how)
        return df_1.merge(df_2, how=self.how)

    def get_code(self, df_1: str, df_2: str) -> str:
        if self.index:
            return f"#join on indcies\n{df_1}.join({df_2}, how = '{self.how}')"
        return f"#natural join on columns \n{df_1}.merge({df_2}, how = '{self.how}')"


class LeftNaturalJoinStrategy(NaturalJoinStrategy):

    def __init__(self, impl_bool_1: bool = False) -> None:
        super().__init__(impl_bool_1)
        self.how = "left"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = super().combine(df_1, df_2)
        df_1.replace({np.nan: None})

    def get_code(self, df_1: str, df_2: str) -> str:
        return super().get_code(df_1, df_2) + f"\n{df_1}.replace({{np.nan: None}})"


class RightNaturalJoinStrategy(NaturalJoinStrategy):

    def __init__(self, impl_bool_1: bool = False) -> None:
        super().__init__(impl_bool_1)
        self.how = "right"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = super().combine(df_1, df_2)
        df_1.replace({np.nan: None})

    def get_code(self, df_1: str, df_2: str) -> str:
        return super().get_code(df_1, df_2) + f"\n{df_1}.replace({{np.nan: None}})"


class OuterNaturalJoinStrategy(NaturalJoinStrategy):

    def __init__(self, impl_bool_1: bool = False) -> None:
        super().__init__(impl_bool_1)
        self.how = "outer"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = super().combine(df_1, df_2)
        df_1.replace({np.nan: None})

    def get_code(self, df_1: str, df_2: str) -> str:
        return super().get_code(df_1, df_2) + f"\n{df_1}.replace({{np.nan: None}})"


class JoinOnStrategy(CombineStrategy):

    def __init__(self, column: str) -> None:
        super().__init__()
        self.on = column
        self.how = "inner"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        return df_1.merge(df_2, on=self.on, how=self.how)

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#Here we {self.how }join on {self.on} two Dataframes\n{df_1} = {df_1}.merge({df_2}, on = "{self.on}",  how="{self.how}")\n"""


class LeftJoinOnStrategy(JoinOnStrategy):

    def __init__(self, column: str) -> None:
        super().__init__(column)
        self.how = "left"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = super().combine(df_1, df_2)
        df_1.replace({np.nan: None})

    def get_code(self, df_1: str, df_2: str) -> str:
        return super().get_code(df_1, df_2) + f"\n{df_1}.replace({{np.nan: None}})"


class RightJoinOnStrategy(JoinOnStrategy):

    def __init__(self, column: str) -> None:
        super().__init__(column)
        self.how = "right"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = super().combine(df_1, df_2)
        df_1.replace({np.nan: None})

    def get_code(self, df_1: str, df_2: str) -> str:
        return super().get_code(df_1, df_2) + f"\n{df_1}.replace({{np.nan: None}})"


class OuterJoinOnStrategy(JoinOnStrategy):

    def __init__(self, column: str) -> None:
        super().__init__(column)
        self.how = "outer"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = super().combine(df_1, df_2)
        df_1.replace({np.nan: None})

    def get_code(self, df_1: str, df_2: str) -> str:
        return super().get_code(df_1, df_2) + f"\n{df_1}.replace({{np.nan: None}})"


class EquiJoinStrategy(CombineStrategy):
    def __init__(self, left_col: str, right_col: str) -> None:
        self.how = "inner"
        self.right = right_col
        self.left = left_col

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        return df_1.merge(df_2, left_on=self.left, right_on=self.right, how=self.how)

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#Here we make an equi join two Dataframes\n{df_1} = {df_1}.merge({df_2},left_on="{self.left}", right_on="{self.right}", how="{self.how}")\n"""


class LeftEquiJoinStrategy(EquiJoinStrategy):

    def __init__(self, left_col: str, right_col: str) -> None:
        super().__init__(left_col, right_col)
        self.how = "left"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = super().combine(df_1, df_2)
        df_1.replace({np.nan: None})

    def get_code(self, df_1: str, df_2: str) -> str:
        return super().get_code(df_1, df_2) + f"\n{df_1}.replace({{np.nan: None}})"


class RightEquiJoinStrategy(EquiJoinStrategy):

    def __init__(self, left_col: str, right_col: str) -> None:
        super().__init__(left_col, right_col)
        self.how = "right"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = super().combine(df_1, df_2)
        df_1.replace({np.nan: None})

    def get_code(self, df_1: str, df_2: str) -> str:
        return super().get_code(df_1, df_2) + f"\n{df_1}.replace({{np.nan: None}})"


class OuterEquiJoinStrategy(EquiJoinStrategy):

    def __init__(self, left_col: str, right_col: str) -> None:
        super().__init__(left_col, right_col)
        self.how = "outer"

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = super().combine(df_1, df_2)
        df_1.replace({np.nan: None})

    def get_code(self, df_1: str, df_2: str) -> str:
        return super().get_code(df_1, df_2) + f"\n{df_1}.replace({{np.nan: None}})"


class ThetaStrategy(CombineStrategy):

    def __init__(self, query: str) -> None:
        super().__init__()
        self.query = query
        self.filter = SelectRowsStrategy(query)

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_1 = df_1.merge(df_2, how="cross")
        return self.filter.transform(df_1)

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#Here we do a theta join on {self.query} by  crossing and then querying two Dataframes\n{df_1} = {df_1}.merge({df_2}, how = "cross")\n{self.filter.get_code(df_1)}"""


# set things
class ConcatStrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_c = pd.concat([df_1, df_2])
        return df_c

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"#Here we concate two Dataframes\n{df_1} = pd.concat([{df_1},{df_2}])\n"


class UnionStrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        df_c = pd.concat([df_1, df_2]).drop_duplicates(keep="first")
        return df_c

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"#Here we concate two Dataframes\n{df_1} = pd.concat([{df_1},{df_2}]).drop_duplicates(keep='first')\n"


class Intersecttrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        return df_1.merge(df_2, on=list(df_1.columns), how="inner")

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#Here we cross two Dataframes\n{df_1} = {df_1}.merge({df_2}, on = list({df_1}.columns) , how = "inner")\n"""


class DiffrenceStrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        return pd.concat([df_1, df_2]).drop_duplicates(keep=False)

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"#Here we concate two Dataframes\n{df_1} = pd.concat([{df_1},{df_2}]).drop_duplicates(keep=False)\n"


class SubtractStrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        return df_1[~df_1.apply(tuple, 1).isin(df_2.apply(tuple, 1))]

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"#Here we concate two Dataframes\n{df_1} = {df_1}[~{df_1}.apply(tuple, 1).isin({df_2}.apply(tuple, 1))]\n"


class CrossStrategy(CombineStrategy):

    def combine(self, df_1: pd.DataFrame, df_2: pd.DataFrame) -> pd.DataFrame:
        return df_1.merge(df_2, how="cross")

    def get_code(self, df_1: str, df_2: str) -> str:
        return f"""#Here we cross two Dataframes\n{df_1} = {df_1}.merge({df_2}, how = "cross")\n"""
