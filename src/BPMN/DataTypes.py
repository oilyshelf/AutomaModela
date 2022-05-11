from enum import Enum


class DataTypes(Enum):
    INT = r"-?\d+"
    FLOAT = r"-?\d+\.\d+"
    STRING = r'"[^"]+"'
    BOOL = r"True|False"
    NONE = r"None"
    EXPR = r".+"
    ATTR = r"`[^`]+`"
    ATTRMAP = r"""(?:`[^`]+`)=(?:-?\d+\.\d+|-?\d+|"[^"]+"|True|False|None)"""
