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
Token_s54RdIJdfgTUcAwdTeuDbQ = None
#Creating new Dataframe based on Token_s54RdIJdfgTUcAwdTeuDbQ
Token_UxVyZn7vYzuHR_3O8UtZDA = Token_s54RdIJdfgTUcAwdTeuDbQ.copy(True)

#Creating new Dataframe based on Token_s54RdIJdfgTUcAwdTeuDbQ
Token_OxPEmA43Kb0BnE9OEmjaeg = Token_s54RdIJdfgTUcAwdTeuDbQ.copy(True)


#here we read the data provided by the Beispiel.xlsx from the sheet Tabelle1 and set the index to None
Token_UxVyZn7vYzuHR_3O8UtZDA = pd.read_excel("Beispiel.xlsx", sheet_name = 'Tabelle1')
Token_UxVyZn7vYzuHR_3O8UtZDA = Token_UxVyZn7vYzuHR_3O8UtZDA.replace({np.nan:None})


#here we read the data provided by the Beispiel.xlsx from the sheet Tabelle2 and set the index to None
Token_OxPEmA43Kb0BnE9OEmjaeg = pd.read_excel("Beispiel.xlsx", sheet_name = 'Tabelle2')
Token_OxPEmA43Kb0BnE9OEmjaeg = Token_OxPEmA43Kb0BnE9OEmjaeg.replace({np.nan:None})

#delete column
Token_OxPEmA43Kb0BnE9OEmjaeg = Token_OxPEmA43Kb0BnE9OEmjaeg.drop('NGC Cost Center', axis = 1)
#delete column
Token_OxPEmA43Kb0BnE9OEmjaeg = Token_OxPEmA43Kb0BnE9OEmjaeg.drop('Department', axis = 1)
#rename column from-> to {'Cost Center': 'Kostenstelle'}
Token_OxPEmA43Kb0BnE9OEmjaeg=Token_OxPEmA43Kb0BnE9OEmjaeg.rename(columns={'Cost Center': 'Kostenstelle'})

#rename column from-> to {'Department Description': 'GF-Bereich'}
Token_OxPEmA43Kb0BnE9OEmjaeg=Token_OxPEmA43Kb0BnE9OEmjaeg.rename(columns={'Department Description': 'GF-Bereich'})

#Here we try to query the Expression not @is_empty(`Profitcenter`) with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_UxVyZn7vYzuHR_3O8UtZDA = Token_UxVyZn7vYzuHR_3O8UtZDA.query('not @is_empty(`Profitcenter`)', **engine)
    except Exception:
        print(engine, "failed to query", 'not @is_empty(`Profitcenter`)', "trying next")

#Creating new Dataframe based on Token_UxVyZn7vYzuHR_3O8UtZDA
Token_LOnzgf2mk1tiailU7uarww = Token_UxVyZn7vYzuHR_3O8UtZDA.copy(True)

#Here we try to query the Expression `Profitcenter` == "P1" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_LOnzgf2mk1tiailU7uarww = Token_LOnzgf2mk1tiailU7uarww.query('`Profitcenter` == "P1"', **engine)
    except Exception:
        print(engine, "failed to query", '`Profitcenter` == "P1"', "trying next")

#Here we concate two Dataframes
Token_UxVyZn7vYzuHR_3O8UtZDA = Token_UxVyZn7vYzuHR_3O8UtZDA[~Token_UxVyZn7vYzuHR_3O8UtZDA.apply(tuple, 1).isin(Token_LOnzgf2mk1tiailU7uarww.apply(tuple, 1))]

#Creating new Dataframe based on Token_UxVyZn7vYzuHR_3O8UtZDA
Token_ESIsTOAs_Z5JMH2FrKVB5Q = Token_UxVyZn7vYzuHR_3O8UtZDA.copy(True)

#Here we try to query the Expression `Profitcenter` == "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_ESIsTOAs_Z5JMH2FrKVB5Q = Token_ESIsTOAs_Z5JMH2FrKVB5Q.query('`Profitcenter` == "P2"', **engine)
    except Exception:
        print(engine, "failed to query", '`Profitcenter` == "P2"', "trying next")

#Here we concate two Dataframes
Token_UxVyZn7vYzuHR_3O8UtZDA = Token_UxVyZn7vYzuHR_3O8UtZDA[~Token_UxVyZn7vYzuHR_3O8UtZDA.apply(tuple, 1).isin(Token_ESIsTOAs_Z5JMH2FrKVB5Q.apply(tuple, 1))]

#Creating new Dataframe based on Token_UxVyZn7vYzuHR_3O8UtZDA
Token_LR70FfGrMjzhijXWv3tPDA = Token_UxVyZn7vYzuHR_3O8UtZDA.copy(True)

#Here we try to query the Expression `Profitcenter` == "P3" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_LR70FfGrMjzhijXWv3tPDA = Token_LR70FfGrMjzhijXWv3tPDA.query('`Profitcenter` == "P3"', **engine)
    except Exception:
        print(engine, "failed to query", '`Profitcenter` == "P3"', "trying next")

#Here we concate two Dataframes
Token_UxVyZn7vYzuHR_3O8UtZDA = Token_UxVyZn7vYzuHR_3O8UtZDA[~Token_UxVyZn7vYzuHR_3O8UtZDA.apply(tuple, 1).isin(Token_LR70FfGrMjzhijXWv3tPDA.apply(tuple, 1))]

#Here we try to evaluate the Expression "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_LOnzgf2mk1tiailU7uarww["Kostenstelle"] = Token_LOnzgf2mk1tiailU7uarww.eval('"K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '"K2"', "trying next")

#Here we try to evaluate the Expression "K1" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_ESIsTOAs_Z5JMH2FrKVB5Q["Kostenstelle"] = Token_ESIsTOAs_Z5JMH2FrKVB5Q.eval('"K1"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '"K1"', "trying next")

#Here we try to evaluate the Expression "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_LR70FfGrMjzhijXWv3tPDA["Kostenstelle"] = Token_LR70FfGrMjzhijXWv3tPDA.eval('"K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '"K2"', "trying next")

#Here we concate two Dataframes
Token_LOnzgf2mk1tiailU7uarww = pd.concat([Token_LOnzgf2mk1tiailU7uarww,Token_ESIsTOAs_Z5JMH2FrKVB5Q])

#Here we concate two Dataframes
Token_LOnzgf2mk1tiailU7uarww = pd.concat([Token_LOnzgf2mk1tiailU7uarww,Token_LR70FfGrMjzhijXWv3tPDA])

#natural join on columns 
Token_OxPEmA43Kb0BnE9OEmjaeg.merge(Token_LOnzgf2mk1tiailU7uarww, how = 'inner')
#here we save the data from Token_OxPEmA43Kb0BnE9OEmjaeg to the the eine_sehr_gute_note.xlsx into the  sheet Sheet1 and dont use the index
for col in Token_OxPEmA43Kb0BnE9OEmjaeg.columns:
    if col.startswith("BACKTICK_QUOTED_STRING_"):
        Token_OxPEmA43Kb0BnE9OEmjaeg.rename(columns={col:col[23:].replace("_", " ")}, inplace=True)
Token_OxPEmA43Kb0BnE9OEmjaeg.to_excel("eine_sehr_gute_note.xlsx", sheet_name = "Sheet1", index = False)

