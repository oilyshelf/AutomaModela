from uuid import uuid4
from .TransformationStrategy import TransformationStrategy
from pandas import DataFrame
from time import time, strftime, gmtime


class Token():

    def __init__(self, context: str):
        self.data = DataFrame()
        self.taken_paths = 1
        self.id = str(uuid4())
        self.cur_time = time()
        self.context: str = f"{strftime('%d-%m-%Y %H:%M:%S', gmtime())} : {context}"

    def add_context(self, element: str) -> None:
        t = time()
        time_it = (lambda x, y: round((x - y) / 60, 3))
        self.context = f"{self.context}--{time_it(t,self.cur_time)}-->{strftime('%d-%m-%Y %H:%M:%S', gmtime())} : {element}"
        self.cur_time = t

    def __repr__(self):
        return f"Token:{self.id}\nPath taken:{self.context}\nData:{self.data.head()}"

    def __deepcopy__(self, memo):
        copied = Token(self.context)
        copied.data = self.data.copy()
        return copied

    def transform(self, strategy: TransformationStrategy):
        self.data = strategy.transform(self.data)


t = Token("test")
print(t)
