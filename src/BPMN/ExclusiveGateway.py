from copy import deepcopy
from typing import OrderedDict
from BPMN import Token
from BPMN.BPMN_Component import BPMNComponent
from BPMN.TransformationStrategy import FilterStrategy


class ExclusiveGateway(BPMNComponent):
    def __init__(self, process_definition: OrderedDict, token: Token):
        super().__init__(process_definition)
        self.token = [token]
        self.opening = process_definition.get("@opening", False)
        self.default = process_definition.get("@default", None)

    def execute(self):
        if self.opening:
            return self._opening()
        else:
            return self._closing()

    def _opening(self):
        # loop trough all outgoings sorted by prio
        def_flow = None
        b_token = self.token[0]
        for key, el in enumerate(sorted(self.outgoing, key=lambda d: d["@priority"] if d["@priority"] else 20)):
            # if a outgoing flow is default mark it for later
            if el.get("@id", None) == self.default:
                def_flow = key
            # check query
            if not b_token.query(el.get("@name")):
                # copy
                token_cp = deepcopy(b_token)
                # transform
                token_cp.transform(FilterStrategy(el.get("@name")))
                # prep return
                token_cp.setPrio(el.get("@priorty"))
                # logging
                self._add_info(token_cp, f"choosen path: {el.get('@name')}")
                # return
                return {
                    "operation": "add",
                    "elements": [{"id": el["@targetRef"], "token":self.token_cp}]
                }
        # no other successfull path go to default if there is one
        if def_flow is not None:
            # if default flow has a query performe it
            if query_string := self.outgoing[def_flow].get("@name", "no_name") != "no_name":
                b_token.transform(FilterStrategy(query_string))
                # prep
            b_token.setPrio(el.get("@priorty"))
            # logging
            self._add_info(b_token, f"choosen default path: {query_string}")
            # return
            return {
                "operation": "add",
                "elements": [{"id": self.outgoing[def_flow]["@targetRef"], "token":b_token}]
            }
        else:
            # if nothing worked just end lol
            return {
                "operation": "end"
            }

    def _closing(self):
        # here you could customize the behaviour with some keywords
        # prep return
        new_token = self.token[0]
        new_token.setPrio(20)
        new_token.setPrio(self.outgoing.get("@priorty"))
        # logging
        self._add_info(new_token)
        return {
            "operation": "add",
            "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
        }
