from .Functionparser import FunctionParser
from .TransformationStrategy import TransformationStrategy, DoNothingStrategy, LoadExcelStrategy, SaveExcelStrategy, dotStrategy, evalStrategy
from BPMN.logger import logger


class TSF():
    def __init__(self):
        self.parser = FunctionParser()

    def get_strategy(self, function_string: str) -> TransformationStrategy | None:
        function_def = self.parser.parse(function_string)
        logger.info(f'parsed function string : {function_def}')
        match function_def:
            case {"name": "doNothing", "parameters": None}:
                return DoNothingStrategy()
            case {"name":"loadExcel", "parameters":[{"parameter":x, "type":"str"},*rest]}:
                opt_par = self.parser.optional_mapper(rest)
                return LoadExcelStrategy(x, **opt_par)
            case {"name":"saveExcel", "parameters":[{"parameter":x, "type":"str"}, *rest]}:
                opt_par = self.parser.optional_mapper(rest)
                return SaveExcelStrategy(x,**opt_par)
            case {"name": "dotOperation", "parameters": [{"parameter": x, "type": "code"}]}:
                return dotStrategy(x)
            case {"name": "eval", "parameters": [{"parameter": x, "type": "code"}]}:
                return evalStrategy(x)

            case _:
                return None
