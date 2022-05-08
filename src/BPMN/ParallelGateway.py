import copy
from typing import OrderedDict
from BPMN import Token
from BPMN.BPMN_Component import BPMNComponent
from BPMN.StrategyFactory import CSF


class ParallelGateway(BPMNComponent):
    def __init__(self, process_definition: OrderedDict, token: Token, factory: CSF):
        super().__init__(process_definition)
        self.token = [token]
        self.opening = process_definition.get("@opening", False)
        self.factory = factory

    def execute(self):
        if self.opening:
            return self._opening()
        else:
            return self._closing()

    def _opening(self):
        # calculating taken paths
        new_paths = len(self.outgoing)
        tba = list()
        # for every path
        for el in self.outgoing:
            # copy token and prep it
            new_token = copy.deepcopy(self.token[0])
            new_token.taken_paths = new_paths
            new_token.setPrio(el.get("@priority"))
            tba.append({"id": el["@targetRef"], "token": new_token})
            # logging
            self._add_info(new_token)
        # return
        return {"operation": "add", "elements": tba}

    def _closing(self):
        # check if all tokens are arrived
        token_len = len(self.token)
        if token_len != self.token[0].taken_paths:
            return {"operation": "repush"}
        # sorting
        self.token = sorted(self.token)
        # choose basis token
        new_token = self.token[0]
        # combine tokens
        strategy = self.factory.get_strategy(self.name)
        for t in self.token[1:]:
            new_token.combine(t, strategy)
        # prep return
        new_token.taken_paths = 1
        new_token.setPrio(20)
        new_token.setPrio(self.outgoing.get("@priorty"))
        # logging
        self._add_info(new_token)
        # return
        return {
            "operation": "add",
            "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
        }
