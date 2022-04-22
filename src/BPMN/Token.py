from __future__ import annotations
import secrets
from BPMN.CodeWriter import CodeWriter
from BPMN.TransformationStrategy import TransformationStrategy
from BPMN.CombineStrategy import CombineStrategy
from pandas import DataFrame
from time import time, strftime, gmtime
from BPMN.logger import logger


class Token():

    def __init__(self, context: str, code_writer: CodeWriter):
        self.data = DataFrame()
        self.taken_paths = 1
        self.id = f"Token_{secrets.token_urlsafe(16)}".replace("-", "_")
        self.cur_time = time()
        self.context: str = f"{strftime('%d-%m-%Y %H:%M:%S', gmtime())} : {context}"
        self.code_writer = code_writer

    def add_context(self, element: str) -> None:
        t = time()
        time_it = (lambda x, y: round((x - y) / 60, 3))
        self.context = f"{self.context}--{time_it(t,self.cur_time)}-->{strftime('%d-%m-%Y %H:%M:%S', gmtime())} : {element}"
        self.cur_time = t

    def __repr__(self):
        return f"Token:{self.id}\nPath taken:{self.context}\nData:{self.data.head()}\n"

    def __deepcopy__(self, memo) -> Token:
        copied = Token(self.context, self.code_writer)
        copied.data = self.data.copy()
        self.code_writer.write_code(f"#Creating new Dataframe based on {self.id}\n{copied.id} = {self.id}.copy(True)\n")
        return copied

    def transform(self, strategy: TransformationStrategy) -> None:
        logger.info(f"Token {self.id} is executing {str(strategy)}")
        self.code_writer.write_code(strategy.get_code(self.id))
        self.data = strategy.transform(self.data)

    def query(self, query_string: str) -> bool:
        engines = [{"engine": "numexpr"}, {"engine": "python"}]
        for e in engines:
            try:
                return self.data.query(query_string, **e).empty
                # print(df.head(), f"this engine was useed {e}")
            except Exception:
                logger.info(f"{e} didn't work to quering {query_string} trying next engine")
        return False

    def combine(self, other: Token, strategy: CombineStrategy) -> None:
        logger.info(f"Token {self.id} is executing {str(strategy)}")
        self.code_writer.write_code(strategy.get_code(self.id, other.id))
        self.data = strategy.combine(self.data, other.data)
