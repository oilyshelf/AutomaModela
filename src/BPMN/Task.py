from typing import OrderedDict
from BPMN.BPMN_Component import BPMNComponent
from BPMN.StrategyFactory import TSF
from BPMN.Token import Token
from BPMN.logger import logger


class Task(BPMNComponent):

    def __init__(self, process_definition: OrderedDict, token: Token, factory: TSF):
        self.token = token
        self.factory = factory
        super().__init__(process_definition)

    def execute(self):
        self.token.add_context(str(self))
        logger.info(self.token)
        self.token.transform(self.factory.get_strategy(self.name))
        target = self.outgoing
        return {
            "operation": "add",
            "elements": [{"id": target["@targetRef"], "token":self.token}]
        }
