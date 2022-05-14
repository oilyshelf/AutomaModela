from typing import List, OrderedDict

from BPMN import Token
from BPMN.BPMN_Component import BPMNComponent
from BPMN.StrategyFactory import CSF, POSF


class ParallelGateway(BPMNComponent):
    def __init__(self, process_definition: OrderedDict, token: Token, comb_factory: CSF, po_factory: POSF):
        super().__init__(process_definition)
        self.token: List[Token] = [token]
        self.opening = process_definition.get("@opening", False)
        self.comb_factory = comb_factory
        self.op_factory = po_factory

    def execute(self):
        if self.opening:
            return self._opening()
        else:
            return self._closing()

    def _opening(self):
        # getting list of tokens to add from Strategy
        tba = self.op_factory.get_strategy(self.name).determine(self.token[0], self.outgoing)
        # calculating taken paths
        paths = len(tba)
        # adding paths and logging
        for el in tba:
            cont = el.pop("info", "")
            token: Token = el.get("token")
            self._add_info(token, cont)
            token.addTakenPath(paths)
        # return
        return {"operation": "add", "elements": tba}

    def _closing(self):
        # check if all tokens are arrived
        token_len = len(self.token)
        if token_len != self.token[0].getTakenPath():
            return {"operation": "repush"}
        # sorting
        self.token = sorted(self.token)
        # choose basis token
        new_token: Token = self.token[0]
        # combine tokens
        strategy = self.comb_factory.get_strategy(self.name)
        for t in self.token[1:]:
            new_token.combine(t, strategy)
        # prep return
        new_token.rmTakenPath()
        new_token.resetPrio()
        new_token.setPrio(self.outgoing.get("@priorty"))
        # logging
        self._add_info(new_token)
        # return
        return {
            "operation": "add",
            "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
        }
