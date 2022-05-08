from typing import List
import re


class FunctionParser():
    def __init__(self):
        self.regex_base = re.compile(r'(\w+)(\([$a-zA-Z0-9_:\[\]=, ".;<>`!?()@]*\))')
        self.regex_empty_brackets = re.compile(r"(\(\s*\))")
        self.regex_string = re.compile(r'("[\w\d\s.?!,]*")')
        self.regex_int = re.compile(r"(\d+)")
        self.regex_float = re.compile(r'(\d+\.\d+)')
        self.regex_eval = re.compile(r'([\w\d.,!?_]+|`[ \w\d.,!?_]+`)( *)=(?!;+)([\w\d .,!?()"`=<>&|@_]+)')
        self.regex_opt = re.compile(r'([\w\d]+[\s]*)=([\s]*[\w\d".]+)')
        self.regex_plain = re.compile(r'(?!;+)(?!\s)[\w\d .,!?()"`=<>&|@_]+')
        self.regex_attribute = re.compile(r'([\w\d.,!?_]+|`[ \w\d.,!?_]+`)')
        self.regex_bool = re.compile(r"(True|False)")
        self.regex_none = re.compile(r"(None)")

    def determine_par_type(self, parameter: str) -> dict:
        if self.regex_string.fullmatch(parameter) is not None:
            return {"parameter": parameter[1:-1], "type": "str", "string": parameter}
        elif self.regex_float.fullmatch(parameter) is not None:
            return {"parameter": float(parameter), "type": "float", "string": parameter}
        elif self.regex_int.fullmatch(parameter) is not None:
            return {"parameter": int(parameter), "type": "int", "string": parameter}
        elif self.regex_bool.fullmatch(parameter) is not None:
            return {"parameter": parameter == "True", "type": "int", "string": parameter}
        elif self.regex_none.fullmatch(parameter) is not None:
            return {"parameter": None, "type": "int", "string": parameter}
        elif self.regex_attribute.fullmatch(parameter) is not None:
            return {"parameter": parameter.strip("`"), "type": "attribute", "string": parameter}
        elif self.regex_opt.fullmatch(parameter) is not None:
            parts = [s.strip() for s in parameter.split("=")]
            return {**self.determine_par_type(parts[-1]), "optional": True, "opt_name": parts[0]}
        elif self.regex_plain.fullmatch(parameter) is not None:
            return {"parameter": parameter, "type": "expr", "string": parameter}
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

    def optional_mapper(self, list_of: List[dict]) -> dict:
        res = {}
        for entry in list_of:
            if entry.get("optional", False):
                res[entry.get("opt_name")] = entry.get("parameter")
        return res

    def parameterlist_mapper(self, parameters: List[dict], ensure_type: str = None):
        res = []
        for par in parameters:
            assert ensure_type is None or par.get("type") == ensure_type, f"Given Parameters are not matchin function call {par} is not an {ensure_type}"
            res.append(par.get("parameter"))
        return res
