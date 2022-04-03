from .Functionparser import FunctionParser
from .TransformationStrategy import TransformationStrategy, DoNothingStrategy, LoadExcelStrategy, SaveExcelStrategy


class BAF():
    def __init__(self):
        self.parser = FunctionParser()

    def get_strategy(self, function_string: str) -> TransformationStrategy | None:
        function_def = self.parser.parse(function_string)
        print(function_def)
        match function_def:
            case {"name": "doNothing", "parameters": None}:
                return DoNothingStrategy()
            case {"name": "loadExcel", "parameters": [{"parameter": x, "type": "str"}]}:
                return LoadExcelStrategy(x)
            case {"name": "saveExcel", "parameters": [{"parameter": x, "type": "str"}]}:
                return SaveExcelStrategy(x)
            case {"name": "dotOperation", "parameters": [{"parameter": x, "type": "code"}]}:
                return SaveExcelStrategy(x)

            case _:
                return None
