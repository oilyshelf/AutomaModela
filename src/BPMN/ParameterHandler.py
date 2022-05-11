from BPMN.DataTypes import DataTypes
from typing import List
import re


class ParameterHandler():

    def repeatingHelper(self, types: tuple):
        return f"({'|'.join(t.value for t in types)})"

    def typeHandler(self, type_str: str, datatype: DataTypes):
        match datatype:
            case DataTypes.ATTR | DataTypes.STRING:
                return type_str[1:-1]
            case DataTypes.FLOAT:
                return float(type_str)
            case DataTypes.INT:
                return int(type_str)
            case DataTypes.BOOL:
                return type_str == "True"
            case DataTypes.NONE:
                return None
            case DataTypes.EXPR:
                return type_str
            case DataTypes.ATTRMAP:
                s = type_str.split("=")
                # print(s)
                return {self.typeHandler(s[0], DataTypes.ATTR): self.determineType(s[1], (DataTypes.FLOAT, DataTypes.INT, DataTypes.STRING, DataTypes.NONE, DataTypes.BOOL))}

    def determineType(self, match_str: str, types: tuple):
        for t in types:
            if re.fullmatch(t.value, match_str) is not None:
                return self.typeHandler(match_str, t)

    def handleRepeating(self, match_str, types: tuple):
        finder = self.repeatingHelper(types)
        return [self.determineType(t, types) for t in re.findall(finder, f"{match_str}, ")]

    def handleInputs(self, matched_str: re.Match, group_def: List[dict]) -> dict:
        res = {"needed": list()}
        for definition in group_def:
            match definition:
                case {"needed": True, "implicite": True}:
                    res["needed"].append(True)

                case {"needed": False, "implicite": True, "group": group, "name": name}:
                    par = True if matched_str.group(group) else False
                    res[name] = par

                case {"needed": False, "implicite": False, "group": group, "repeating": False, "name": name, "types": types}:
                    if par := matched_str.group(group):
                        res[name] = self.determineType(par, types) 

                case {"needed": True, "implicite": False, "group": group, "repeating": False, "types": types}:
                    res["needed"].append(self.determineType(matched_str.group(group), types))

                case {"needed": False, "implicite": False, "group": group, "repeating": True, "name": name, "types": types}:
                    if par := matched_str.group(group):
                        res[name] = self.handleRepeating(par, types)

                case {"needed": True, "implicite": False, "group": group, "repeating": True, "types": types}:
                    res["needed"].append(self.handleRepeating(matched_str.group(group), types))

                case _:
                    print(f"no match for {definition}")
        return res
