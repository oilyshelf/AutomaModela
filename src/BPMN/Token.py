from dataclasses import dataclass, field
from multiprocessing import context
import string
from typing import List
from pandas import DataFrame
from .TransfomationsStratagies import _TokenStrategy


@dataclass(frozen=True)
class Token():
    id: int
    df: DataFrame
    context: str
    taken_paths: int = 1

    def transform(strategy: _TokenStrategy) -> None:
        pass
