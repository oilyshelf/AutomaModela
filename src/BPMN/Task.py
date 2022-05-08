from typing import OrderedDict
from BPMN.BPMN_Component import BPMNComponent
from BPMN.StrategyFactory import TSF
from BPMN.Token import Token


class Task(BPMNComponent):

    def __init__(self, process_definition: OrderedDict, token: Token, factory: TSF):
        super().__init__(process_definition)
        self.token = token
        self.factory = factory

    def execute(self):
        # transform
        self.token.transform(self.factory.get_strategy(self.name))
        # prep return
        target = self.outgoing
        self.token.setPrio(target.get("@priority"))
        # logging
        self._add_info(self.token)
        return {
            "operation": "add",
            "elements": [{"id": target["@targetRef"], "token":self.token}]
        }
