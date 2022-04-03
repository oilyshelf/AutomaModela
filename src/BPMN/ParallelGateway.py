import copy
from typing import OrderedDict
from BPMN import Token
from BPMN.BPMN_Component import BPMNComponent


class ParallelGateway(BPMNComponent):
    def __init__(self, process_definition: OrderedDict, token: Token):
        self.token = [token]
        self.opening = process_definition.get("@opening", False)
        super().__init__(process_definition)

    def execute(self):
        for token in self.token:
            token.add_context(str(self))
            print(token)
        if self.opening:
            new_paths = len(self.outgoing)
            tba = [{"id": el["@targetRef"], "token":copy.deepcopy(self.token[0])} for el in self.outgoing]
            for key, obj in enumerate(tba):
                # print(key, obj)
                tba[key]["token"].taken_paths = new_paths
            return {"operation": "add", "elements": tba}
        else:
            token_len = len(self.token)
            if token_len == self.token[0].taken_paths:
                # do stuff
                new_token = self.token[0]
                new_token.taken_paths = 1
                return {
                    "operation": "add",
                    "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
                }
            else:
                return {"operation": "repush"}
