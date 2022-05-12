from BPMN.TransformationStrategy import TransformationStrategy
from BPMN.CombineStrategy import CombineStrategy
from dataclasses import dataclass
from BPMN.DataTypes import DataTypes
from typing import List


@dataclass(frozen=True)
class StrategyFunction():
    strategy: type[TransformationStrategy]
    definition: str
    groups: List


class FunctionBuilder():

    def build_function(self, strategy: type[TransformationStrategy | CombineStrategy], needed: dict, *args) -> StrategyFunction:
        """providing a strategy , and definition of a function , build a text based function with a regex to find it 
            and an instruction set to filter the string for parameters (look at needed for more info)
        Args:
            strategy (type[TransformationStrategy]): definition of strategy on which this func should be used on
            needed (dict): {
                text:str --> a text with or without marked spots to place regex for parameter finding e.g. "this is a function {parameter}" -- required
                types:dict a dictonary that maps paramter(defined in text) to the enum DataTypes which the parameter should have -- optional
                repeating: dict maps parameters to boolean if there are of an variable lenght -- optional
                implicite: Bool a boolean parameter can be representet as text itself instead of a parameter --optional
            }
            *args if you want to extend the call with optional parameters --> same as needed

        Returns:
            StrategyFunction: dataclass with all the things needed combined
        """
        whole_function, group_mapper, counter = self.unpacker(needed, 1)
        for arg in args:
            apendy = self.unpacker(arg, counter, True)
            whole_function += apendy[0]
            group_mapper.extend(apendy[1])
            counter = apendy[2]

        return StrategyFunction(strategy, whole_function, group_mapper)

    def unpacker(self, function_part: dict, counter: int, optional: bool = False) -> tuple:
        func_regex = function_part.get("text")

        if function_part.get("implicite", False):
            if not optional:
                return (func_regex, [
                    {
                        "types": DataTypes.BOOL,
                        "group": None,
                        "repeating": False,
                        "needed": not optional,
                        "implicite": True,
                        "name": None
                    }
                ], counter)

            return (f"( {func_regex})?", [{
                "types": DataTypes.BOOL,
                "group": counter,
                "repeating": False,
                "needed": not optional,
                "implicite": True,
                "name": f"impl_bool_{counter}"
            }], counter + 1)
        types = function_part.get("types", dict())
        repeating = function_part.get("repeating", dict())
        parameter_reg = {key: self.combination_builder(el, repeating.get(key, False)) for key, el in types.items()}
        if optional:
            func_regex = f"(?: {func_regex})?"
        func_regex = func_regex.format(**parameter_reg)
        group_mapper = list()
        for key, type in types.items():
            group_mapper.append({
                "types": type,
                "group": counter,
                "repeating": repeating.get(key, False),
                "needed": not optional,
                "implicite": False,
                "name": key
            })
            counter += 1

        return (func_regex, group_mapper, counter)

    def combination_builder(self, types: tuple, repeating: bool = False) -> str:
        comb = "|".join(t.value for t in types)
        if repeating:
            return f"((?:(?:{comb})(?:, )?)+)"
        return f"({comb})"
