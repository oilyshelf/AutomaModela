from .Token import Token
from.BPMN_Component import BPMNComponent


class StartEvent(BPMNComponent):

    def execute(self):
        token = Token(str(self))
        target = self.outgoing
        print(token)
        assert target["@targetRef"] != None, "missing refernce!!"
        return {
            "operation": "add",
            "elements": [{"id": target["@targetRef"], "token":token}]
        }
