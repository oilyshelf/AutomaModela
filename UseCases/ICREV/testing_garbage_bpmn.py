import pandas as pd
import numpy as np
#to run this code u need python 3.x with these packages installed pandas, numpy, numexpr
import math
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

#Tokencreation
Token_XgcH6tTPW_9B8fOX0mXj5A = None
#Here we try to evaluate the Expression `counter` = None with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`counter` = None', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`counter` = None', "trying next")

#Here we try to evaluate the Expression `other` = None with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`other` = None', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`other` = None', "trying next")

#add row based on args order
Token_XgcH6tTPW_9B8fOX0mXj5A.loc[len(Token_XgcH6tTPW_9B8fOX0mXj5A.index)] = [1, 'test']
#Here we try to evaluate the Expression `counter` = `counter`+1 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`counter` = `counter`+1', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`counter` = `counter`+1', "trying next")

#Here we try to evaluate the Expression `counter` = `counter`+1 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`counter` = `counter`+1', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`counter` = `counter`+1', "trying next")

#Here we try to evaluate the Expression `counter` = `counter`+1 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`counter` = `counter`+1', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`counter` = `counter`+1', "trying next")

#Here we try to evaluate the Expression `counter` = `counter`+1 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`counter` = `counter`+1', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`counter` = `counter`+1', "trying next")

#Here we try to evaluate the Expression `counter` = `counter`+1 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`counter` = `counter`+1', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`counter` = `counter`+1', "trying next")

#Here we try to evaluate the Expression `counter` = `counter`+1 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`counter` = `counter`+1', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`counter` = `counter`+1', "trying next")

#Here we try to evaluate the Expression `counter` = `counter`+1 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`counter` = `counter`+1', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`counter` = `counter`+1', "trying next")

#Here we try to evaluate the Expression `counter` = `counter`+1 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`counter` = `counter`+1', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`counter` = `counter`+1', "trying next")

#Here we try to evaluate the Expression `counter` = `counter`+1 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XgcH6tTPW_9B8fOX0mXj5A = Token_XgcH6tTPW_9B8fOX0mXj5A.eval('`counter` = `counter`+1', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`counter` = `counter`+1', "trying next")

#Creating new Dataframe based on Token_XgcH6tTPW_9B8fOX0mXj5A
Token_KmXiCZoi6Z8RBBmhaytY5A = Token_XgcH6tTPW_9B8fOX0mXj5A.copy(True)

#Here we try to query the Expression `counter` == 10 with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_KmXiCZoi6Z8RBBmhaytY5A = Token_KmXiCZoi6Z8RBBmhaytY5A.query('`counter` == 10', **engine)
    except Exception:
        print(engine, "failed to query", '`counter` == 10', "trying next")

#Here we try to evaluate the Expression `other` = @replace_all(`other`, "t","T") with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_KmXiCZoi6Z8RBBmhaytY5A = Token_KmXiCZoi6Z8RBBmhaytY5A.eval('`other` = @replace_all(`other`, "t","T")', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`other` = @replace_all(`other`, "t","T")', "trying next")


#here we save the data from Token_KmXiCZoi6Z8RBBmhaytY5A to the the counter.xlsx into the  sheet Sheet1 and dont use the index
Token_KmXiCZoi6Z8RBBmhaytY5A.to_excel("counter.xlsx", sheet_name = "Sheet1", index = False)

