from BPMN.logger import logger
from .Token import Token
from.BPMN_Component import BPMNComponent


class StartEvent(BPMNComponent):

    def execute(self):
        token = Token(str(self))
        target = self.outgoing
        logger.info(token)
        assert target["@targetRef"] is not None, "missing refernce!!"
        return {
            "operation": "add",
            "elements": [{"id": target["@targetRef"], "token":token}]
        }
