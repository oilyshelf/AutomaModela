import copy
from typing import OrderedDict
from BPMN import Token
from BPMN.StrategyFactory import CSF
from BPMN.TransformationStrategy import FilterStrategy
from BPMN.BPMN_Component import BPMNComponent


class InclusiveGateway(BPMNComponent):
    def __init__(self, process_definition: OrderedDict, token: Token, factory: CSF):
        super().__init__(process_definition)
        self.token = [token]
        self.opening = process_definition.get("@opening", False)
        self.default = process_definition.get("@default", None)
        self.factory = factory

    def execute(self):
        if self.opening:
            return self._opening()
        else:
            return self._closing()

    def _opening(self):
        # return list ToBeAdded
        tba = list()
        # define token
        b_token = self.token[0]
        # keeping track of default flow
        defa = None
        suc_querys = []
        # loop trough all querys
        for el in sorted(self.outgoing, key=lambda d: d["@priority"] if d["@priority"] else 20):
            # sucessfull query
            if not b_token.query(el.get("@name")):
                # copy
                token_cp = copy.deepcopy(b_token)
                # transform
                token_cp.transform(FilterStrategy(el.get("@name")))
                # prep
                token_cp.setPrio(el.get("@priority"))
                # keeping track of successful queries
                suc_querys.append(el.get("@name"))
                # logging
                self._add_info(token_cp, f"took path: {el.get('@id')} with query: {el.get('@name')}")
                # append to return list
                tba.append({
                    "id": el.get("@targetRef"),
                    "token": token_cp
                })
            elif el.get("@id") == self.default:
                name = el.get("@name")
                # set flag to calculate rest at the end
                if name == "rest":
                    defa = el.get("@id")
                    continue
                token_cp = copy.deepcopy(b_token)
                # perform transformation if query is provided
                if name != "no_name":
                    token_cp.transform(FilterStrategy(name))
                # prep
                token_cp.setPrio(el.get("@priority"))
                # logging
                self._add_info(token_cp, f"took path: {el.get('@id')} with query: {'no query' if name == 'no_name' else name}")
                # append to return list
                tba.append({
                    "id": el.get("@targetRef"),
                    "token": token_cp
                })
        # special case for rest default flows
        if defa is not None:
            # copy
            token_cp = copy.deepcopy(b_token)
            # calculate inverse query
            query = " & ".join([f"~({s})" for s in suc_querys])
            # transform
            token_cp.transform(FilterStrategy(query))
            # prep
            token_cp.setPrio(el.get("@priority"))
            # logging
            self._add_info(token_cp, f"took path: {el.get('@id')} with query: {el.get('@name')}")
            # append to return list
            tba.append({
                "id": el.get("@targetRef"),
                "token": token_cp
            })
        # set taken paths for every token
        token_count = len(tba)
        for key, obj in enumerate(tba):
            tba[key]["token"].taken_paths = token_count
        # return
        return {"operation": "add", "elements": tba}

    def _closing(self):
        token_len = len(self.token)
        if token_len != self.token[0].taken_paths:
            return {"operation": "repush"}
        # sorting token
        self.token = sorted(self.token)
        # choosing base token
        new_token = self.token[0]
        # combining tokens
        strategy = self.factory.get_strategy(self.name)
        for t in self.token[1:]:
            new_token.combine(t, strategy)
        # prep
        new_token.taken_paths = 1
        new_token.setPrio(20)
        new_token.setPrio(self.outgoing.get("@priority"))
        # logging
        self._add_info(new_token, "combined")
        # return
        return {
            "operation": "add",
            "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
        }
