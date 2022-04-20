from copy import deepcopy
from typing import OrderedDict
from BPMN import Token
from BPMN.BPMN_Component import BPMNComponent
from BPMN.TransformationStrategy import FilterStrategy
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
            def_flow = None
            b_token = self.token[0]
            for key, el in enumerate(self.outgoing):
                
                if el.get("@id", None) == self.default: def_flow = key

                if b_token.query(el.get("@name")):
                    token_cp =  deepcopy(b_token)
                    token_cp.transform(FilterStrategy(el.get("@name")))
                    return {
                        "operation": "add",
                        "elements": [{"id": el["@targetRef"], "token":self.token_cp}]
                    }

            if def_flow is not None:
                if query_string := self.outgoing[def_flow].get("@name", "no_name") != "no_name":
                    b_token.transform(FilterStrategy(query_string))
                return {
                        "operation": "add",
                        "elements": [{"id": self.outgoing[def_flow]["@targetRef"], "token":b_token}]
                    }
                     
        else:
            # here you could customize the behaviour with some keywords
            new_token = self.token[0]
            return {
                "operation": "add",
                "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
            }
