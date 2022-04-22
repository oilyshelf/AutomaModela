import copy
from typing import OrderedDict
from BPMN import Token
from BPMN.StrategyFactory import CSF
from BPMN.TransformationStrategy import FilterStrategy
from BPMN.logger import logger
from BPMN.BPMN_Component import BPMNComponent


class InclusiveGateway(BPMNComponent):
    def __init__(self, process_definition: OrderedDict, token: Token, factory: CSF):
        self.token = [token]
        self.opening = process_definition.get("@opening", False)
        self.default = process_definition.get("@default", None)
        self.factory = factory
        super().__init__(process_definition)

    def execute(self):
        for token in self.token:
            token.add_context(str(self))
            logger.info(token)
        if self.opening:
            tba = []
            b_token = self.token[0]
            for el in self.outgoing:
                if not b_token.query(el.get("@name")) or el.get('@id') == self.default:
                    token_cp = copy.deepcopy(b_token)
                    token_cp.transform(FilterStrategy(el.get("@name")))
                    tba.append({
                        "id": el.get("@targetRef"),
                        "token": token_cp
                    })

            token_count = len(tba)
            logger.info(tba)
            for key, obj in enumerate(tba):
                tba[key]["token"].taken_paths = token_count
            return {"operation": "add", "elements": tba}
        else:
            token_len = len(self.token)
            if token_len == self.token[0].taken_paths:
                new_token = self.token[0]
                for t in self.token[1:]:
                    new_token.combine(t, self.factory.get_strategy(self.name))
                new_token.taken_paths = 1
                return {
                    "operation": "add",
                    "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
                }
            else:
                return {"operation": "repush"}
