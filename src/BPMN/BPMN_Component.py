from __future__ import annotations
import abc
from BPMN.Token import Token
from typing import OrderedDict
from time import time
from BPMN.logger import logger


class BPMNComponent:

    def __init__(self, process_definition: OrderedDict):
        self.id = process_definition.get("@id")
        self.name = process_definition.get("@name", "no_name")
        self.incoming = process_definition.get("bpmn:incoming", None)
        self.outgoing = process_definition.get("bpmn:outgoing", None)
        self.creation_time = time()
        self.token: Token = None

    def _add_info(self, token: Token, additional_msg: str = "") -> None:
        token.add_context(str(self) + additional_msg)
        logger.info(token)

    @abc.abstractclassmethod
    def execute(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}{'('+self.name+')' if self.name != 'no_name' else ''}"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.id}{'('+self.name+')' if self.name != 'no_name' else ''}"

    def __lt__(self, other: BPMNComponent) -> bool:
        # Component which was created first is prioritised
        t1 = self.token
        t2 = other.token
        if t1 == t2:
            return self.creation_time < other.creation_time
        return t1 < t2
