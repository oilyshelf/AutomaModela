import pandas as pd
import numpy as np 
import math

# special
ALL = slice(None)

# number


def root_of(a: int | float, base: int = 2) -> int | float:
    return a**(1 / base)

# float


def round_to(a: float, places: int = 2) -> float:
    return round(a, places)


def floor(a: float) -> int:
    return math.floor(a)


def ceil(a: float) -> int:
    return math.ceil(a)

# string 


def concat(a: str, b: str) -> str:
    match (type(a), type(b)):
        case (pd.Series, str):
            return a.astype(str) + b
        case (str, pd.Series):
            return a + b.astype(str)
        case _:
            return a + b


def substr(a: str, start: int, end: int) -> str:
    if type(a) == pd.Series:
        return a.str.slice(start=start, stop=end)
    return a[start:end]


def strip(a: str, special_char: str | None = None) -> str:
    if type(a) == pd.Series:
        return a.str.strip(special_char)
    return a.strip(special_char)


def split(a: str, on_what: str, keep: int = 0) -> str:
    if type(a) == pd.Series:
        a = a.str.split(on_what, expand=True)
        print(a)
        return a[keep]
    return a.split(on_what)[keep]


def replace(a: str, where: int, _with: str) -> str:
    if type(a) == pd.Series:
        a = a.str
    return a[:where] + _with + a[where + 1:]


def replace_all(a: str, what: str, _whith: str) -> str:
    if type(a) == pd.Series:
        a = a.str
    return a.replace(what, _whith)

# data conversion


def to_string(a: int | float) -> str:
    if type(a) == pd.Series:
        return a.astype(str)
    return str(a)


def to_int(a: str | float) -> int:
    if type(a) == pd.Series:
        return a.astype(int)
    return int(a)


def to_float(a: str | int) -> float:
    if type(a) == pd.Series:
        return a.astype(float)
    float(a)

# data reduction 


def get_sum(a) -> int | float:
    return np.sum(a)


def get_prod(a) -> int | float:
    return np.prod(a)


def get_min(a) -> int | float:
    return np.min(a)


def get_max(a) -> int | float:
    return np.max(a)


def get_mean(a) -> int | float:
    return np.mean(a)

# data evaluation 


def is_empty(a) -> bool:
    return pd.isnull(a)


def contains(a: str, c_str: str, at: int | None = None) -> bool:
    match (type(a), at):
        case (pd.Series, None):
            return a.str.contains(c_str)
        case (pd.Series, int):  # noqa: F841
            return a.str[at] == c_str
        case (str, int):  # noqa: F841
            return a[at] == c_str
        case _:
            return c_str in a


def starts_with(a: str, c_str: str) -> str:
    if type(a) == pd.Series:
        a = a.str
    return a.startswith(c_str)


expr_locals = {
    "root_of": root_of,
    "round_to": round_to,
    "floor": floor,
    "ceil": ceil,
    "concat": concat,
    "substr": substr,
    "strip": strip,
    'split': split,
    "replace": replace,
    "replace_all": replace_all,
    "to_string": to_string,
    "to_float": to_float,
    "to_int": to_int,
    "get_sum": get_sum,
    "get_prod": get_prod,
    "get_min": get_min,
    "get_max": get_max,
    "get_mean": get_mean,
    "is_empty": is_empty,
    "contains": contains,
    "starts_with": starts_with,
    "ALL": ALL
}


expr_code = """import math
#these are wrappers for function which may be used in site of an expr (ik not the best design lol)
# special
ALL = slice(None)
# number
def root_of(a:int|float, base:int = 2)->int|float:
    return a**(1/base)

#float
def round_to(a:float, places:int = 2) ->float:
    return round(a,places)

def floor(a:float)->int:
    return math.floor(a)

def ceil(a:float)->int:
    return math.ceil(a)

#string 
def concat(a:str, b:str)->str:
    match (type(a), type(b)):
        case (pd.Series, str):
            return a.astype(str)+b
        case (str, pd.Series):
            return a+b.astype(str)
        case _:
            return a+b

def substr(a:str, start:int, end:int)->str:
    if type(a) == str:
        return a.str.slice(start=start, stop = end)
    return a[start:end]

def strip(a:str, special_char:str|None = None)->str:
    if type(a) == str:
        return a.str.strip(special_char)
    return a.strip(special_char)

def split(a:str, on_what:str, keep:int = 0)->str:
    if type(a) == str:
        return a.str.split(on_what)[keep]
    return a.split(on_what)[keep]


def replace(a:str, where:int, _with:str)->str:
    if type(a) == pd.Series:
        a = a.str
    return a[:where]+_with+a[where+1:]  

def replace_all(a:str, what:str, _whith:str)->str:
    if type(a) == pd.Series:
        a = a.str
    return a.replace(what, _whith)

#data conversion
def to_string(a:int|float)->str:
    if type(a) == pd.Series:
        return a.astype(str)
    return str(a)

def to_int(a:str|float)->int:
    if type(a) == pd.Series:
        return a.astype(int)
    return int(a)

def to_float(a:str|int)->float:
    if type(a) == pd.Series:
        return a.astype(float)
    float(a)

# data reduction 
def get_sum(a)->int|float:
    return np.sum(a)

def get_prod(a)->int|float:
    return np.prod(a)

def get_min(a)->int|float:
    return np.min(a)

def get_max(a)->int|float:
    return np.max(a)

def get_mean(a)->int|float:
    return np.mean(a)

# data evaluation 
def is_empty(a)->bool:
    return pd.isnull(a)


def contains(a:str, c_str:str, at:int|None = None)->bool:
    match (type(a), at):
        case (pd.Series, None):
            return a.str.contains(c_str)
        case (pd.Series, int):
            return a.str[at] == c_str
        case (str, int):
            return a[at] == c_str
        case _:
            return c_str in a


def starts_with(a:str, c_str:str)->str:
    if type(a) == pd.Series:
        a = a.str
    return a.startswith(c_str)

"""
