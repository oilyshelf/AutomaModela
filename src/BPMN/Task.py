from typing import OrderedDict
from BPMN.BPMN_Component import BPMNComponent
from BPMN.StrategyFactory import BAF
from BPMN.Token import Token


class Task(BPMNComponent):

    def __init__(self, process_definition: OrderedDict, token: Token, factory: BAF):
        self.token = token
        self.factory = factory
        super().__init__(process_definition)

    def execute(self):
        self.token.add_context(str(self))
        print(self.token)
        self.token.transform(self.factory.get_strategy(self.name))
        target = self.outgoing
        return {
            "operation": "add",
            "elements": [{"id": target["@targetRef"], "token":self.token}]
        }
