from typing import OrderedDict
from BPMN.CodeWriter import CodeWriter
from .Token import Token
from.BPMN_Component import BPMNComponent


class StartEvent(BPMNComponent):

    def __init__(self, process_definition: OrderedDict, code_writer: CodeWriter):
        super().__init__(process_definition)
        self.code_writer = code_writer
        self.token = Token(self.code_writer)

    def execute(self):
        # execute
        target = self.outgoing
        self.token.setPrio(target.get("@priority"))
        # logging
        self._add_info(self.token)
        # returning
        return {
            "operation": "add",
            "elements": [{"id": target["@targetRef"], "token":self.token}]
        }
