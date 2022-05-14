from typing import List, OrderedDict

from BPMN import Token
from BPMN.BPMN_Component import BPMNComponent
from BPMN.StrategyFactory import EOSF


class ExclusiveGateway(BPMNComponent):
    def __init__(self, process_definition: OrderedDict, token: Token, op_factory: EOSF):
        super().__init__(process_definition)
        self.token: List[Token] = [token]
        self.opening = process_definition.get("@opening", False)
        self.default = process_definition.get("@default", None)
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
                default = list(filter(lambda x: x["@id"] == self.default, self.outgoing))[0]
                tba = [{"id": default["@targetRef"], "token":self.token[0], "info":"default"}]
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
        # here you could customize the behaviour with some keywords in the future 
        # prep return
        new_token = self.token[0]
        new_token.rmTakenPath()
        new_token.resetPrio()
        new_token.setPrio(self.outgoing.get("@priorty"))
        # logging
        self._add_info(new_token)
        return {
            "operation": "add",
            "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
        }
