from BPMN.CombineStrategy import CombineStrategy, ConcatStrategy
from BPMN.TransformationStrategy import TransformationStrategy, dotStrategy
from BPMN.logger import logger
from BPMN.ParameterHandler import ParameterHandler
from BPMN.FunctionBuilder import StrategyFunction
from typing import List
from BPMN.TaskFunctionsDefinitions import compiled_base_funcs
import re


class TSF():
    def __init__(self, additional_funcs: List[StrategyFunction] | None = None) -> None:
        self.parameter_handler: ParameterHandler = ParameterHandler()

        self.functions: List[StrategyFunction] = compiled_base_funcs

        if additional_funcs:
            self.functions.extend(additional_funcs)

    def get_strategy(self, prov_string: str) -> TransformationStrategy:
        for taskfunc in self.functions:
            if m := re.fullmatch(taskfunc.definition, prov_string):
                parameter = self.parameter_handler.handleInputs(m, taskfunc.groups)
                needed_parameter = parameter.pop("needed", list())
                return taskfunc.strategy(*needed_parameter, **parameter)
        if prov_string.startswith("."):
            return dotStrategy(prov_string)
        return None


class CSF():

    def __init__(self) -> None:
        # (left |right |outer |) for the diffrent types
        self.regex_equi = re.compile(r'(left |right |outer |)(join on)(.+)(==)(.+)')
        self.regex_theta = re.compile(r"(left |right |outer |)(join on)((.+)(!=|>=|<=|<|>)(.+))")
        self.regex_singlexol = re.compile(r"(left |right |outer |)(join on)([\w\s\d]+[^=!><])")

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
                    logger.info(x)
                    return "EquiStrat"
                elif x := self.regex_theta.fullmatch(gateway_string) is not None:
                    logger.info(x)
                    return "thetaStrat"
                elif x := self.regex_singlexol.fullmatch(gateway_string) is not None:
                    logger.info(x)
                    return "SimpleJoinStrat"
                else:
                    return None
