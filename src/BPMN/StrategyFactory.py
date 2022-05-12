from BPMN.CombineStrategy import CombineStrategy
from BPMN.OpeningStrategy import OpeningStrategy
from BPMN.Strategy import Strategy
from BPMN.TransformationStrategy import TransformationStrategy, dotStrategy
from BPMN.ParameterHandler import ParameterHandler
from BPMN.FunctionBuilder import StrategyFunction
from typing import List
from BPMN.TaskFunctionsDefinitions import compiled_task_funcs
from BPMN.CombineFuncDefinitions import compiled_combine_funcs
from BPMN.OpeningFuncDefinitions import compiled_eo_funcs, compiled_io_funcs, compiled_po_funcs
import re


class StrategyFactory():
    def __init__(self, additional_funcs: List[StrategyFunction] | None = None) -> None:
        self.parameter_handler: ParameterHandler = ParameterHandler()

        self.functions: List[StrategyFunction] = list()

        if additional_funcs:
            self.functions.extend(additional_funcs)

    def get_strategy(self, prov_string: str) -> Strategy:
        for taskfunc in self.functions:
            if m := re.fullmatch(taskfunc.definition, prov_string):
                parameter = self.parameter_handler.handleInputs(m, taskfunc.groups)
                needed_parameter = parameter.pop("needed", list())
                return taskfunc.strategy(*needed_parameter, **parameter)
        return None


class TSF(StrategyFactory):

    def __init__(self, additional_funcs: List[StrategyFunction] | None = None) -> None:
        functions = compiled_task_funcs
        if additional_funcs:
            functions.extend(additional_funcs)
        super().__init__(functions)

    def get_strategy(self, prov_string: str) -> TransformationStrategy:
        if strategy := super().get_strategy(prov_string):
            return strategy
        if prov_string.startswith("."):
            return dotStrategy(prov_string)
        return None


class CSF(StrategyFactory):

    def __init__(self, additional_funcs: List[StrategyFunction] | None = None) -> None:
        functions = compiled_combine_funcs
        if additional_funcs:
            functions.extend(additional_funcs)
        super().__init__(functions)

    def get_strategy(self, prov_string: str) -> CombineStrategy:
        return super().get_strategy(prov_string)


class POSF(StrategyFactory):

    def __init__(self, additional_funcs: List[StrategyFunction] | None = None) -> None:
        functions = compiled_po_funcs
        if additional_funcs:
            functions.extend(additional_funcs)
        super().__init__(functions)

    def get_strategy(self, prov_string: str) -> OpeningStrategy:
        return super().get_strategy(prov_string)


class IOSF(StrategyFactory):

    def __init__(self, additional_funcs: List[StrategyFunction] | None = None) -> None:
        functions = compiled_io_funcs
        if additional_funcs:
            functions.extend(additional_funcs)
        super().__init__(functions)

    def get_strategy(self, prov_string: str) -> OpeningStrategy:
        return super().get_strategy(prov_string)


class EOSF(StrategyFactory):

    def __init__(self, additional_funcs: List[StrategyFunction] | None = None) -> None:
        functions = compiled_eo_funcs
        if additional_funcs:
            functions.extend(additional_funcs)
        super().__init__(functions)

    def get_strategy(self, prov_string: str) -> OpeningStrategy:
        return super().get_strategy(prov_string)
