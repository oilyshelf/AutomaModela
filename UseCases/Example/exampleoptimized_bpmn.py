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
Token_WZEUIWMfhFy1HhIq4zJbSQ = None
#Creating new Dataframe based on Token_WZEUIWMfhFy1HhIq4zJbSQ
Token_CGSdyDcPcEEsG0A6mUmRPA = Token_WZEUIWMfhFy1HhIq4zJbSQ.copy(True)

#Creating new Dataframe based on Token_WZEUIWMfhFy1HhIq4zJbSQ
Token_sSeYrNJAOnKqKsuqCQmlnA = Token_WZEUIWMfhFy1HhIq4zJbSQ.copy(True)


#here we read the data provided by the Beispiel.xlsx from the sheet Tabelle1 and set the index to None
Token_CGSdyDcPcEEsG0A6mUmRPA = pd.read_excel("Beispiel.xlsx", sheet_name = 'Tabelle1')
Token_CGSdyDcPcEEsG0A6mUmRPA = Token_CGSdyDcPcEEsG0A6mUmRPA.replace({np.nan:None})


#here we read the data provided by the Beispiel.xlsx from the sheet Tabelle2 and set the index to None
Token_sSeYrNJAOnKqKsuqCQmlnA = pd.read_excel("Beispiel.xlsx", sheet_name = 'Tabelle2')
Token_sSeYrNJAOnKqKsuqCQmlnA = Token_sSeYrNJAOnKqKsuqCQmlnA.replace({np.nan:None})

#Here we try to query the Expression not @is_empty(`Profitcenter`) with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_CGSdyDcPcEEsG0A6mUmRPA = Token_CGSdyDcPcEEsG0A6mUmRPA.query('not @is_empty(`Profitcenter`)', **engine)
    except Exception:
        print(engine, "failed to query", 'not @is_empty(`Profitcenter`)', "trying next")

#we get a subset of the dataframe with these columns ['Cost Center', 'Department Description']
Token_sSeYrNJAOnKqKsuqCQmlnA = Token_sSeYrNJAOnKqKsuqCQmlnA[['Cost Center', 'Department Description']]

#Here we try to evaluate the Expression "dummy" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_CGSdyDcPcEEsG0A6mUmRPA["Kostenstelle"] = Token_CGSdyDcPcEEsG0A6mUmRPA.eval('"dummy"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '"dummy"', "trying next")

#rename column from-> to {'Cost Center': 'Kostenstelle'}
Token_sSeYrNJAOnKqKsuqCQmlnA=Token_sSeYrNJAOnKqKsuqCQmlnA.rename(columns={'Cost Center': 'Kostenstelle'})

#rename column from-> to {'Department Description': 'GF-Bereich'}
Token_sSeYrNJAOnKqKsuqCQmlnA=Token_sSeYrNJAOnKqKsuqCQmlnA.rename(columns={'Department Description': 'GF-Bereich'})

#Creating new Dataframe based on Token_CGSdyDcPcEEsG0A6mUmRPA
Token_I_M8Ha5Z36LxfIA23Dcw3w = Token_CGSdyDcPcEEsG0A6mUmRPA.copy(True)

#Here we try to query the Expression `Profitcenter` == "P1" or `Profitcenter` == "P3" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_I_M8Ha5Z36LxfIA23Dcw3w = Token_I_M8Ha5Z36LxfIA23Dcw3w.query('`Profitcenter` == "P1" or `Profitcenter` == "P3"', **engine)
    except Exception:
        print(engine, "failed to query", '`Profitcenter` == "P1" or `Profitcenter` == "P3"', "trying next")

#Here we concate two Dataframes
Token_CGSdyDcPcEEsG0A6mUmRPA = Token_CGSdyDcPcEEsG0A6mUmRPA[~Token_CGSdyDcPcEEsG0A6mUmRPA.apply(tuple, 1).isin(Token_I_M8Ha5Z36LxfIA23Dcw3w.apply(tuple, 1))]

#Creating new Dataframe based on Token_CGSdyDcPcEEsG0A6mUmRPA
Token_L8hw1ikVosUPFySrDVd3Wg = Token_CGSdyDcPcEEsG0A6mUmRPA.copy(True)

#Here we try to query the Expression `Profitcenter` == "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_L8hw1ikVosUPFySrDVd3Wg = Token_L8hw1ikVosUPFySrDVd3Wg.query('`Profitcenter` == "P2"', **engine)
    except Exception:
        print(engine, "failed to query", '`Profitcenter` == "P2"', "trying next")

#Here we concate two Dataframes
Token_CGSdyDcPcEEsG0A6mUmRPA = Token_CGSdyDcPcEEsG0A6mUmRPA[~Token_CGSdyDcPcEEsG0A6mUmRPA.apply(tuple, 1).isin(Token_L8hw1ikVosUPFySrDVd3Wg.apply(tuple, 1))]

#Here we try to evaluate the Expression "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_I_M8Ha5Z36LxfIA23Dcw3w["Kostenstelle"] = Token_I_M8Ha5Z36LxfIA23Dcw3w.eval('"K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '"K2"', "trying next")

#Here we try to evaluate the Expression "K1" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_L8hw1ikVosUPFySrDVd3Wg["Kostenstelle"] = Token_L8hw1ikVosUPFySrDVd3Wg.eval('"K1"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '"K1"', "trying next")

#Here we concate two Dataframes
Token_I_M8Ha5Z36LxfIA23Dcw3w = pd.concat([Token_I_M8Ha5Z36LxfIA23Dcw3w,Token_L8hw1ikVosUPFySrDVd3Wg])

#natural join on columns 
Token_I_M8Ha5Z36LxfIA23Dcw3w.merge(Token_sSeYrNJAOnKqKsuqCQmlnA, how = 'inner')
#here we save the data from Token_I_M8Ha5Z36LxfIA23Dcw3w to the the eine_sehr_sehr_gute_note.xlsx into the  sheet Sheet1 and dont use the index
for col in Token_I_M8Ha5Z36LxfIA23Dcw3w.columns:
    if col.startswith("BACKTICK_QUOTED_STRING_"):
        Token_I_M8Ha5Z36LxfIA23Dcw3w.rename(columns={col:col[23:].replace("_", " ")}, inplace=True)
Token_I_M8Ha5Z36LxfIA23Dcw3w.to_excel("eine_sehr_sehr_gute_note.xlsx", sheet_name = "Sheet1", index = False)

