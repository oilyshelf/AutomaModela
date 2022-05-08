from .Token import Token
from .BPMN_Component import BPMNComponent
from typing import OrderedDict


class EndEvent(BPMNComponent):

    def __init__(self, process_definition: OrderedDict, token: Token):
        super().__init__(process_definition)
        self.token = token

    def execute(self):
        self._add_info(self.token)
        return {
            "operation": "end"
        }
