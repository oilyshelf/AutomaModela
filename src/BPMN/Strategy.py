from dataclasses import dataclass
from typing import List


# class for typ hinting lol
class Strategy():
    pass


@dataclass(frozen=True)
class StrategyFunction():
    strategy: type[Strategy]
    definition: str
    groups: List
