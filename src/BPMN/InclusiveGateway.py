from typing import List, OrderedDict

from BPMN import Token
from BPMN.BPMN_Component import BPMNComponent
from BPMN.StrategyFactory import CSF, IOSF


class InclusiveGateway(BPMNComponent):
    def __init__(self, process_definition: OrderedDict, token: Token, comb_factory: CSF, op_factory: IOSF):
        super().__init__(process_definition)
        self.token: List[Token] = [token]
        self.opening = process_definition.get("@opening", False)
        self.default = process_definition.get("@default", None)
        self.comb_factory = comb_factory
        self.op_factory = op_factory

    def execute(self):
        if self.opening:
            return self._opening()
        else:
            return self._closing()

    def _opening(self):
        # getting list of tokens to add from Strategy
        tba = self.op_factory.get_strategy(self.name).determine(self.token[0], self.outgoing, self.default)
        # handle default
        if tba is None:
            if self.default is not None:
                tba = [{"id": self.outgoing["@targetRef"], "token":self.token[0], "info":"default"}]
            else:
                raise Exception("Gateway Error no flow was taken and no default flow specified")
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
        token_len = len(self.token)
        if token_len != self.token[0].getTakenPath():
            return {"operation": "repush"}
        # sorting token
        self.token = sorted(self.token)
        # choosing base token
        new_token = self.token[0]
        # combining tokens
        strategy = self.comb_factory.get_strategy(self.name)
        for t in self.token[1:]:
            new_token.combine(t, strategy)
        # prep
        new_token.rmTakenPath()
        new_token.setPrio(20)
        new_token.setPrio(self.outgoing.get("@priority"))
        # logging
        self._add_info(new_token, "combined")
        # return
        return {
            "operation": "add",
            "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
        }
