import abc
from typing import OrderedDict


class BPMNComponent:

    def __init__(self, process_definition: OrderedDict):
        self.id = process_definition.get("@id")
        self.name = process_definition.get("@name", "no_name")
        self.incoming = process_definition.get("bpmn:incoming", None)
        self.outgoing = process_definition.get("bpmn:outgoing", None)

    @abc.abstractclassmethod
    def execute(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.id}{'('+self.name+')' if self.name != 'no_name' else ''}"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.id}{'('+self.name+')' if self.name != 'no_name' else ''}"

    def __lt__(self, other):
        # here it needs to be definied which task should be done first lol
        return True
