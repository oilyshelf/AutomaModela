from typing import OrderedDict
from BPMN.CodeWriter import CodeWriter
from BPMN.logger import logger
from .Token import Token
from.BPMN_Component import BPMNComponent


class StartEvent(BPMNComponent):

    def __init__(self, process_definition: OrderedDict, code_writer:CodeWriter):
        super().__init__(process_definition)
        self.code_writer = code_writer

    def execute(self):
        token = Token(str(self), self.code_writer)
        target = self.outgoing
        logger.info(token)
        assert target["@targetRef"] is not None, "missing refernce!!"
        return {
            "operation": "add",
            "elements": [{"id": target["@targetRef"], "token":token}]
        }
