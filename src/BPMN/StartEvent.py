from typing import OrderedDict
from BPMN.CodeWriter import CodeWriter
from BPMN.logger import logger
from .Token import Token
from.BPMN_Component import BPMNComponent


class StartEvent(BPMNComponent):

    def __init__(self, process_definition: OrderedDict, code_writer: CodeWriter):
        super().__init__(process_definition)
        self.code_writer = code_writer
        self.token = Token(str(self), self.code_writer)

    def execute(self):
        target = self.outgoing
        logger.info(self.token)
        self.token.setPrio(target.get("@priority", 20))
        return {
            "operation": "add",
            "elements": [{"id": target["@targetRef"], "token":self.token}]
        }
