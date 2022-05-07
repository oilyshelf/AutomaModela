import copy
from typing import OrderedDict
from BPMN import Token
from BPMN.StrategyFactory import CSF
from BPMN.TransformationStrategy import FilterStrategy
from BPMN.logger import logger
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
            # logging
            for token in self.token:
                token.add_context(str(self))
                logger.info(token)

            tba = []
            b_token = self.token[0]
            defa = None
            suc_querys = []
            for el in sorted(self.outgoing, key=lambda d: d["@priority"]):
                if not b_token.query(el.get("@name")):
                    token_cp = copy.deepcopy(b_token)
                    token_cp.transform(FilterStrategy(el.get("@name")))
                    token_cp.setPrio(el.get("@priority"))
                    suc_querys.append(el.get("@name"))
                    token_cp.add_context(f"took path: {el.get('@id')} with query: {el.get('@name')}")
                    tba.append({
                        "id": el.get("@targetRef"),
                        "token": token_cp
                    })
                elif el.get("@id") == self.default:
                    n = el.get("@name")
                    if n == "no_name":
                        b_token.add_context(f"took default path: {el.get('@id')} with no query")
                        tba.append({
                            "id": el.get("@targetRef"),
                            "token": b_token
                        })
                    elif n == "rest":
                        defa = el.get("@id")
                    else:
                        token_cp = copy.deepcopy(b_token)
                        token_cp.transform(FilterStrategy(el.get("@name")))
                        token_cp.add_context(f"took path: {el.get('@id')} with query: {el.get('@name')}")
                        suc_querys.append(el.get("@name"))
                        tba.append({
                            "id": el.get("@targetRef"),
                            "token": token_cp
                        })

            if defa is not None:
                token_cp = copy.deepcopy(b_token)

                query = " & ".join([f"~({s})" for s in suc_querys])
                token_cp.transform(FilterStrategy(query))
                token_cp.add_context(f"took default rest path: {defa} with query: {query}")
                tba.append({
                    "id": el.get("@targetRef"),
                    "token": token_cp
                })

            token_count = len(tba)
            logger.info(tba)
            for key, obj in enumerate(tba):
                tba[key]["token"].taken_paths = token_count
            return {"operation": "add", "elements": tba}
        else:
            # sorting
            self.token = sorted(self.token, key=lambda t: t.priority)
            token_len = len(self.token)
            if token_len == self.token[0].taken_paths:
                # logging
                for token in self.token:
                    token.add_context(str(self))
                    logger.info(token)
                new_token = self.token[0]
                for t in self.token[1:]:
                    new_token.combine(t, self.factory.get_strategy(self.name))
                new_token.taken_paths = 1
                new_token.setPrio(self.outgoing.get("@priority"))
                return {
                    "operation": "add",
                    "elements": [{"id": self.outgoing["@targetRef"], "token":new_token}]
                }
            else:
                return {"operation": "repush"}
