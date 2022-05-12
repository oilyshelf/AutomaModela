from __future__ import annotations
import secrets
from BPMN.CodeWriter import CodeWriter
from BPMN.TransformationStrategy import SelectRowsStrategy, TransformationStrategy
from BPMN.CombineStrategy import CombineStrategy
from pandas import DataFrame
from time import time, strftime, gmtime
from BPMN.logger import logger


class Token():

    def __init__(self, code_writer: CodeWriter, context: str = None):
        self.data = DataFrame()
        self.taken_paths = [1]
        self.id = f"Token_{secrets.token_urlsafe(16)}".replace("-", "_")
        self.cur_time = time()
        self.code_writer = code_writer
        if context is None:
            context = ""
            self.code_writer.write_code(f"#Tokencreation\n{self.id} = None")
        self.context: str = context
        self.priority = 20

    def add_context(self, element: str) -> None:
        t = time()
        time_it = (lambda x, y: round((x - y) / 60, 3))
        self.context = f"{self.context}--{time_it(t,self.cur_time)}-->{strftime('%d-%m-%Y %H:%M:%S', gmtime())} : {element}"
        self.cur_time = t

    def transform(self, strategy: TransformationStrategy) -> None:
        logger.info(f"Token {self.id} is executing {str(strategy)}")
        self.data = strategy.transform(self.data)
        self.code_writer.write_code(strategy.get_code(self.id))

    def query(self, query_string: str) -> bool:
        return SelectRowsStrategy(query_string).transform(self.data).empty

    def combine(self, other: Token, strategy: CombineStrategy) -> None:
        logger.info(f"Token {self.id} is executing {str(strategy)}")
        self.data = strategy.combine(self.data, other.data)
        self.code_writer.write_code(strategy.get_code(self.id, other.id))

    def setPrio(self, prio: int | None) -> None:
        if prio:
            self.priority = prio

    def addTakenPath(self, num: int):
        self.taken_paths.append(num)

    def getTakenPath(self) -> int:
        return self.taken_paths[-1]

    def rmTakenPath(self):
        if len(self.taken_paths) > 1:
            self.taken_paths.pop()

    def __lt__(self, other: Token) -> bool:

        if self.priority == other.priority:
            return self.cur_time < other.cur_time
        return self.priority < other.priority

    def __repr__(self):
        return f"Token:{self.id}\nPath taken:{self.context}\nData:{self.data.head()}\n"

    def __deepcopy__(self, memo) -> Token:
        copied = Token(self.code_writer, self.context)
        copied.data = self.data.copy()
        copied.taken_paths = self.taken_paths.copy()
        self.code_writer.write_code(f"#Creating new Dataframe based on {self.id}\n{copied.id} = {self.id}.copy(True)\n")
        return copied
