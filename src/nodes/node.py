from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True, order=True)
class Node():
    id:int
    name:str = field(compare=False)
    children: List[int] = field(default_factory=list)