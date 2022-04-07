from typing import OrderedDict
from BPMN import Token
from BPMN.BPMN_Component import BPMNComponent
from BPMN.logger import logger


class ExclusiveGateway(BPMNComponent):
    def __init__(self, process_definition: OrderedDict, token: Token):
        self.token = [token]
        self.opening = process_definition.get("@opening", False)
        self.default = process_definition.get("@default", None)
        super().__init__(process_definition)

    def execute(self):
        for token in self.token:
            token.add_context(str(self))
            logger.info(token)
        if self.opening:
            for el in self.outgoing:
                if el.get("@id", None) == self.default:
                    return {
                        "operation": "add",
                        "elements": [{"id": el["@targetRef"], "token":self.token[0]}]
                    }
        else:
            # here you could customize the behaviour with some keywords
            new_token = self.token[0]
            return {
                "operation": "add",
                "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
            }
