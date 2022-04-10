from typing import List
import re


class FunctionParser():
    def __init__(self):
        self.regex_base = re.compile(r'(\w+)(\([$a-zA-Z0-9_:\[\]=, "".;]*\))')
        self.regex_empty_brackets = re.compile(r"(\(\s*\))")
        self.regex_string = re.compile(r'("[\w\d\s.?!,]*")+')
        self.regex_int = re.compile(r"(\d*)")
        self.regex_float = re.compile(r'(\d*\.\d*)')
        self.regex_eval = re.compile(r"(.*=.*)")

    def determine_par_type(self, parameter: str) -> dict:
        if self.regex_string.fullmatch(parameter) is not None:
            return {"parameter": parameter[1:-1], "type": "str", "string": parameter}
        elif self.regex_float.fullmatch(parameter) is not None:
            return {"parameter": float(parameter), "type": "float", "string": parameter}
        elif self.regex_int.fullmatch(parameter) is not None:
            return {"parameter": int(parameter), "type": "int", "string": parameter}
        else:
            return {"parameter": None, "type": "not supported Datatype", "string": parameter}

    def cleansplit_param(self, parameter: str) -> List[str] | None:
        # check if the string are empty brackets
        if self.regex_empty_brackets.fullmatch(parameter) is not None:
            return None
        return [self.determine_par_type(s.strip()) for s in parameter[1:-1].split(";")]

    def parse(self, string: str) -> dict | None:
        if m := self.regex_base.fullmatch(string):
            return {
                "name": m.group(1),
                "parameters": self.cleansplit_param(m.group(2))
            }
        elif string.startswith("."):
            return{
                "name": "dotOperation",
                "parameters": [{"parameter": string, "type": "code"}]
            }
        elif m := self.regex_eval.fullmatch(string):
            return{
                "name": "eval",
                "parameters": [{"parameter": string, "type": "code"}]
            }
        else:
            return None
