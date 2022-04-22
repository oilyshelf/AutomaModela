from BPMN.CombineStrategy import ConcatStrategy, CombineStrategy
from .Functionparser import FunctionParser
from .TransformationStrategy import FilterStrategy, SelectStrategy, TransformationStrategy, DoNothingStrategy, LoadExcelStrategy, SaveExcelStrategy, dotStrategy, evalStrategy
from BPMN.logger import logger
import re


class TSF():
    def __init__(self):
        self.parser = FunctionParser()

    def get_strategy(self, function_string: str) -> TransformationStrategy | None:
        function_def = self.parser.parse(function_string)
        logger.info(f'parsed function string : {function_def}')
        match function_def:
            case {"name": "doNothing", "parameters": None}:
                return DoNothingStrategy()
            case {"name": "loadExcel", "parameters": [{"parameter": x, "type": "str"}, *rest]}:
                opt_par = self.parser.optional_mapper(rest)
                return LoadExcelStrategy(x, **opt_par)
            case {"name": "saveExcel", "parameters": [{"parameter": x, "type": "str"}, *rest]}:
                opt_par = self.parser.optional_mapper(rest)
                return SaveExcelStrategy(x, **opt_par)
            case {"name": "dotOperation", "parameters": [{"parameter": x, "type": "code"}]}:
                return dotStrategy(x)
            case {"name": "eval", "parameters": [{"parameter": x, "type": "code"}]}:
                return evalStrategy(x)
            case {"name": "filter", "parameters": [{"parameter": x, "type": "plain_text"}]}:
                return FilterStrategy(x)
            case {"name": "select", "parameters": [*pars]}:
                p = self.parser.parameterlist_mapper(pars, ensure_type="plain_text")
                return SelectStrategy(p)

            case _:
                return None


class CSF():

    def __init__(self) -> None:
        # (left |right |outer |) for the diffrent types
        self.regex_equi = re.compile(r'(join on)(.+)(==)(.+)')
        self.regex_theta = re.compile(r"(join on)(.+)(!=|>=|<=|<|>)(.+)")
        self.regex_singlexol = re.compile(r"(join on)([\w\s\d]+[^=!><])")

    def get_strategy(self, gateway_string: str) -> CombineStrategy | None:

        match gateway_string:
            case "join":
                return "naturaljoinstrategy"
            case "concat":
                return ConcatStrategy()
            case "intersect":
                return "intersectstrategy"
            case "difference":
                "difStrat"
            case "cross":
                return "crossStrat"
            case _:

                if x := self.regex_equi.fullmatch(gateway_string) is not None:
                    return "EquiStrat"
                elif x := self.regex_theta.fullmatch(gateway_string) is not None:
                    return "thetaStrat"
                elif x := self.regex_singlexol.fullmatch(gateway_string) is not None:
                    return "SimpleJoinStrat"
                else:
                    return None
