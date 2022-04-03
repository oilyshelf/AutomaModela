from .Token import Token
from .BPMN_Component import BPMNComponent
from typing import OrderedDict


class EndEvent(BPMNComponent):

    def __init__(self, process_definition: OrderedDict, token: Token):
        self.token = token
        super().__init__(process_definition)

    def execute(self):
        self.token.add_context(str(self))
        print(self.token)
        return {
            "operation": "end"
        }
