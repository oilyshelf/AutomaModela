import copy
from typing import OrderedDict
from BPMN import Token
from BPMN.BPMN_Component import BPMNComponent
from BPMN.StrategyFactory import CSF
from BPMN.logger import logger


class ParallelGateway(BPMNComponent):
    def __init__(self, process_definition: OrderedDict, token: Token, factory: CSF):
        super().__init__(process_definition)
        self.token = [token]
        self.opening = process_definition.get("@opening", False)
        self.factory = factory

    def execute(self):

        if self.opening:
            # logging
            for token in self.token:
                token.add_context(str(self))
                logger.info(token)
            new_paths = len(self.outgoing)
            tba = list()
            for el in self.outgoing:
                new_token = copy.deepcopy(self.token[0])
                new_token.taken_paths = new_paths
                new_token.setPrio(el.get("@priority"))
                tba.append({"id": el["@targetRef"], "token": new_token})
            return {"operation": "add", "elements": tba}
        else:
            token_len = len(self.token)
            # sorting
            self.token = sorted(self.token, key=lambda t: t.priority)
            if token_len == self.token[0].taken_paths:
                # logging
                for token in self.token:
                    token.add_context(str(self))
                    logger.info(token)

                new_token = self.token[0]
                for t in self.token[1:]:
                    new_token.combine(t, self.factory.get_strategy(self.name))
                new_token.taken_paths = 1
                new_token.setPrio(self.outgoing.get("@priorty"))
                return {
                    "operation": "add",
                    "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
                }
            else:
                return {"operation": "repush"}
