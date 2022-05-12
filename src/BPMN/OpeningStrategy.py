import abc
import copy
import re
from typing import List
from BPMN.CombineStrategy import SubtractStrategy
from BPMN.Token import Token
from BPMN.TransformationStrategy import SelectRowsStrategy
from BPMN.Strategy import Strategy
from BPMN.DataTypes import DataTypes


class OpeningStrategy(Strategy):

    @abc.abstractclassmethod
    def determine(self, token: Token, flows: List[dict], default: str | None = None) -> List[dict] | None:
        """
        Args:
            token (Token): _description_
            flows (List[dict]): _description_
            default (str | None, optional): _description_. Defaults to None.

        Returns:
            List[dict] | None: _description_
        """
        pass

# ParallelGateways


class CopyStrategy(OpeningStrategy):

    def determine(self, token: Token, flows: List[dict], default: str | None = None) -> List[dict] | None:
        tba = list()
        for el in flows:
            new_token = copy.deepcopy(token)
            new_token.setPrio(el.get("@priority"))
            tba.append({"id": el["@targetRef"], "token": new_token, "info": "copied"})

        return tba


class NewStrategy(OpeningStrategy):
    def __init__(self, impl_bool_1: bool = False) -> None:
        self.keep = impl_bool_1

    def determine(self, token: Token, flows: List[dict], default: str | None = None) -> List[dict] | None:
        tba = list()
        for el in flows:
            if self.keep and el.get("@name", "False") == "True": 
                new_token = copy.deepcopy(token)
            else:
                new_token = Token(token.code_writer)
                new_token.add_context(token.context)
            # prep token
            new_token.setPrio(el.get("@priority"))
            tba.append({"id": el["@targetRef"], "token": new_token, "info": f"{'kept' if self.keep else 'new'}"})

        return tba

# Exclusive Gateways


class CheckStartegy(OpeningStrategy):
    def __init__(self, impl_bool_1: bool = False) -> None:
        super().__init__()
        self.keep = impl_bool_1
        self.fp = DataTypes.EXPR

    def determine(self, token: Token, flows: List[dict], default: str | None = None) -> List[dict] | None:

        for el in sorted(flows, key=lambda d: d["@priority"] if d["@priority"] else 20):
            # if a outgoing flow is default skip if it has no name (Datatype is expr with .+ no value for regexing lol )
            if el.get("@id", None) == default and el.get("@name") == "no_name":
                continue
            # check query
            if not token.query(el.get("@name")):

                if self.keep:
                    token_cp = token
                else:
                    # copy
                    token_cp = copy.deepcopy(token)
                    # transform
                    token_cp.transform(SelectRowsStrategy(el.get("@name")))

                # prep return
                token_cp.setPrio(el.get("@priorty"))
                # return
                return [{"id": el["@targetRef"], "token":token_cp, "info":f"queried {el.get('@name')}{'and kept' if self.keep else 'and transformed'}"}]
        return None


class EmptyStrategy(OpeningStrategy):

    def __init__(self) -> None:
        super().__init__()
        self.fp = DataTypes.BOOL

    def determine(self, token: Token, flows: List[dict], default: str | None = None) -> List[dict] | None:
        is_empty = token.data.empty
        for el in sorted(flows, key=lambda d: d["@priority"] if d["@priority"] else 20):
            # if a outgoing flow is skip
            if el.get("@id", None) == default and re.fullmatch(self.fp, el.get("@name")) is None:
                continue
            wants = el.get("@name") == "True"
            if is_empty == wants:
                token.setPrio(el.get("@priority"))
                return [{"id": el["@targetRef"], "token":token}]
        return False

# inclusive


class SpliceStartegy(OpeningStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.fp = DataTypes.EXPR

    def determine(self, token: Token, flows: List[dict], default: str | None = None) -> List[dict] | None:
        tba = list()
        for el in sorted(flows, key=lambda d: d["@priority"] if d["@priority"] else 20):
            # if a outgoing flow is default skip if it has no name (Datatype is expr with .+ no value for regexing lol )
            if el.get("@id", None) == default and el.get("@name") == "no_name":
                continue
            # check query
            if not token.query(el.get("@name")):

                # copy
                token_cp = copy.deepcopy(token)
                # transform
                token_cp.transform(SelectRowsStrategy(el.get("@name")))
                # remove queried rows
                token.combine(token_cp, SubtractStrategy())

                # prep return
                token_cp.setPrio(el.get("@priorty"))
                # return
                tba.append({"id": el["@targetRef"], "token": token_cp, "info": f"queried {el.get('@name')}"})
        return tba if len(tba) else None


class ResetStartegy(OpeningStrategy):

    def __init__(self) -> None:
        super().__init__()
        self.fp = DataTypes.EXPR

    def determine(self, token: Token, flows: List[dict], default: str | None = None) -> List[dict] | None:
        tba = list()
        for el in sorted(flows, key=lambda d: d["@priority"] if d["@priority"] else 20):
            # if a outgoing flow is default skip if it has no name (Datatype is expr with .+ no value for regexing lol )
            if el.get("@id", None) == default and el.get("@name") == "no_name":
                continue
            # check query
            if not token.query(el.get("@name")):

                # copy
                token_cp = copy.deepcopy(token)
                # transform
                token_cp.transform(SelectRowsStrategy(el.get("@name")))
                # prep return
                token_cp.setPrio(el.get("@priorty"))
                # return
                tba.append({"id": el["@targetRef"], "token": token_cp, "info": f"queried {el.get('@name')}"})
        return tba if len(tba) else None
