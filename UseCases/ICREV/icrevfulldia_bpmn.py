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
Token_DRjE2EkYMDvJL28EIMMjAQ = None
#Tokencreation
Token_n15pq_cPbso4mpONFYdITw = None
#Tokencreation
Token_rjYBI2SpXB_vU04xb_eg_g = None

#here we read the data provided by the ICREV_EXample.xlsx from the sheet SAP and set the index to None
Token_n15pq_cPbso4mpONFYdITw = pd.read_excel("ICREV_EXample.xlsx", sheet_name = 'SAP')
Token_n15pq_cPbso4mpONFYdITw = Token_n15pq_cPbso4mpONFYdITw.replace({np.nan:None})

#Here we try to query the Expression not @is_empty(`Profitcenter`) with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_n15pq_cPbso4mpONFYdITw = Token_n15pq_cPbso4mpONFYdITw.query('not @is_empty(`Profitcenter`)', **engine)
    except Exception:
        print(engine, "failed to query", 'not @is_empty(`Profitcenter`)', "trying next")

#Here we try to evaluate the Expression "CC_Unknown" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_n15pq_cPbso4mpONFYdITw["Kostenstelle"] = Token_n15pq_cPbso4mpONFYdITw.eval('"CC_Unknown"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '"CC_Unknown"', "trying next")


#here we read the data provided by the ICREV_EXample.xlsx from the sheet Mapping and set the index to None
Token_rjYBI2SpXB_vU04xb_eg_g = pd.read_excel("ICREV_EXample.xlsx", sheet_name = 'Mapping')
Token_rjYBI2SpXB_vU04xb_eg_g = Token_rjYBI2SpXB_vU04xb_eg_g.replace({np.nan:None})

#we get a subset of the dataframe with these columns ['Cost Center', 'Department Description']
Token_rjYBI2SpXB_vU04xb_eg_g = Token_rjYBI2SpXB_vU04xb_eg_g[['Cost Center', 'Department Description']]

#rename column from-> to {'Cost Center': 'Kostenstelle'}
Token_rjYBI2SpXB_vU04xb_eg_g=Token_rjYBI2SpXB_vU04xb_eg_g.rename(columns={'Cost Center': 'Kostenstelle'})

#rename column from-> to {'Department Description': 'GF-Bereich'}
Token_rjYBI2SpXB_vU04xb_eg_g=Token_rjYBI2SpXB_vU04xb_eg_g.rename(columns={'Department Description': 'GF-Bereich'})

#Creating new Dataframe based on Token_n15pq_cPbso4mpONFYdITw
Token_E300ZNlJDWvlj56i4MNrsw = Token_n15pq_cPbso4mpONFYdITw.copy(True)

#Here we try to query the Expression `Profitcenter` == "DE21DUMMY" or `Profitcenter` == "DE21ADMIN" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_E300ZNlJDWvlj56i4MNrsw = Token_E300ZNlJDWvlj56i4MNrsw.query('`Profitcenter` == "DE21DUMMY" or `Profitcenter` == "DE21ADMIN"', **engine)
    except Exception:
        print(engine, "failed to query", '`Profitcenter` == "DE21DUMMY" or `Profitcenter` == "DE21ADMIN"', "trying next")

#Here we concate two Dataframes
Token_n15pq_cPbso4mpONFYdITw = Token_n15pq_cPbso4mpONFYdITw[~Token_n15pq_cPbso4mpONFYdITw.apply(tuple, 1).isin(Token_E300ZNlJDWvlj56i4MNrsw.apply(tuple, 1))]

#Creating new Dataframe based on Token_n15pq_cPbso4mpONFYdITw
Token_XZHyfZsAPgl84O0g0cgoYQ = Token_n15pq_cPbso4mpONFYdITw.copy(True)

#Here we try to query the Expression `Profitcenter` == "DE04DUMMY" or `Profitcenter` == "DE04ADMIN" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_XZHyfZsAPgl84O0g0cgoYQ = Token_XZHyfZsAPgl84O0g0cgoYQ.query('`Profitcenter` == "DE04DUMMY" or `Profitcenter` == "DE04ADMIN"', **engine)
    except Exception:
        print(engine, "failed to query", '`Profitcenter` == "DE04DUMMY" or `Profitcenter` == "DE04ADMIN"', "trying next")

#Here we concate two Dataframes
Token_n15pq_cPbso4mpONFYdITw = Token_n15pq_cPbso4mpONFYdITw[~Token_n15pq_cPbso4mpONFYdITw.apply(tuple, 1).isin(Token_XZHyfZsAPgl84O0g0cgoYQ.apply(tuple, 1))]

#Creating new Dataframe based on Token_n15pq_cPbso4mpONFYdITw
Token_DltAGo2BTlpMMhsbWJ_tzA = Token_n15pq_cPbso4mpONFYdITw.copy(True)

#Here we try to query the Expression @contains(`Profitcenter`, "P", 5) with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_DltAGo2BTlpMMhsbWJ_tzA = Token_DltAGo2BTlpMMhsbWJ_tzA.query('@contains(`Profitcenter`, "P", 5)', **engine)
    except Exception:
        print(engine, "failed to query", '@contains(`Profitcenter`, "P", 5)', "trying next")

#Here we concate two Dataframes
Token_n15pq_cPbso4mpONFYdITw = Token_n15pq_cPbso4mpONFYdITw[~Token_n15pq_cPbso4mpONFYdITw.apply(tuple, 1).isin(Token_DltAGo2BTlpMMhsbWJ_tzA.apply(tuple, 1))]

#Creating new Dataframe based on Token_n15pq_cPbso4mpONFYdITw
Token_kerPCjXqeKOArL5BUgHLHg = Token_n15pq_cPbso4mpONFYdITw.copy(True)

#Here we try to query the Expression @starts_with(`Profitcenter`, "DE37") with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_kerPCjXqeKOArL5BUgHLHg = Token_kerPCjXqeKOArL5BUgHLHg.query('@starts_with(`Profitcenter`, "DE37")', **engine)
    except Exception:
        print(engine, "failed to query", '@starts_with(`Profitcenter`, "DE37")', "trying next")

#Here we concate two Dataframes
Token_n15pq_cPbso4mpONFYdITw = Token_n15pq_cPbso4mpONFYdITw[~Token_n15pq_cPbso4mpONFYdITw.apply(tuple, 1).isin(Token_kerPCjXqeKOArL5BUgHLHg.apply(tuple, 1))]

#Creating new Dataframe based on Token_n15pq_cPbso4mpONFYdITw
Token_QFvrzsRzCz_GJCNY5zBMyA = Token_n15pq_cPbso4mpONFYdITw.copy(True)

#Here we try to query the Expression not @contains(`Profitcenter`, "P", 5) and not @contains(`Profitcenter`, "R", 4) with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_QFvrzsRzCz_GJCNY5zBMyA = Token_QFvrzsRzCz_GJCNY5zBMyA.query('not @contains(`Profitcenter`, "P", 5) and not @contains(`Profitcenter`, "R", 4)', **engine)
    except Exception:
        print(engine, "failed to query", 'not @contains(`Profitcenter`, "P", 5) and not @contains(`Profitcenter`, "R", 4)', "trying next")

#Here we concate two Dataframes
Token_n15pq_cPbso4mpONFYdITw = Token_n15pq_cPbso4mpONFYdITw[~Token_n15pq_cPbso4mpONFYdITw.apply(tuple, 1).isin(Token_QFvrzsRzCz_GJCNY5zBMyA.apply(tuple, 1))]

#Here we try to evaluate the Expression "DE21101110" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_E300ZNlJDWvlj56i4MNrsw["Kostenstelle"] = Token_E300ZNlJDWvlj56i4MNrsw.eval('"DE21101110"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '"DE21101110"', "trying next")

#Here we try to evaluate the Expression "DE04109819" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_XZHyfZsAPgl84O0g0cgoYQ["Kostenstelle"] = Token_XZHyfZsAPgl84O0g0cgoYQ.eval('"DE04109819"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '"DE04109819"', "trying next")

#Here we try to evaluate the Expression @replace_all(`Profitcenter`, "P", "0") with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_DltAGo2BTlpMMhsbWJ_tzA["Kostenstelle"] = Token_DltAGo2BTlpMMhsbWJ_tzA.eval('@replace_all(`Profitcenter`, "P", "0")', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@replace_all(`Profitcenter`, "P", "0")', "trying next")

#Here we try to evaluate the Expression `Profitcenter` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_kerPCjXqeKOArL5BUgHLHg["Kostenstelle"] = Token_kerPCjXqeKOArL5BUgHLHg.eval('`Profitcenter`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Profitcenter`', "trying next")

#Here we try to evaluate the Expression `Profitcenter` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_QFvrzsRzCz_GJCNY5zBMyA["Kostenstelle"] = Token_QFvrzsRzCz_GJCNY5zBMyA.eval('`Profitcenter`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Profitcenter`', "trying next")

#Here we concate two Dataframes
Token_E300ZNlJDWvlj56i4MNrsw = pd.concat([Token_E300ZNlJDWvlj56i4MNrsw,Token_XZHyfZsAPgl84O0g0cgoYQ])

#Here we concate two Dataframes
Token_E300ZNlJDWvlj56i4MNrsw = pd.concat([Token_E300ZNlJDWvlj56i4MNrsw,Token_DltAGo2BTlpMMhsbWJ_tzA])

#Here we concate two Dataframes
Token_E300ZNlJDWvlj56i4MNrsw = pd.concat([Token_E300ZNlJDWvlj56i4MNrsw,Token_kerPCjXqeKOArL5BUgHLHg])

#Here we concate two Dataframes
Token_E300ZNlJDWvlj56i4MNrsw = pd.concat([Token_E300ZNlJDWvlj56i4MNrsw,Token_QFvrzsRzCz_GJCNY5zBMyA])

#Here we innerjoin on Kostenstelle two Dataframes
Token_rjYBI2SpXB_vU04xb_eg_g = Token_rjYBI2SpXB_vU04xb_eg_g.merge(Token_E300ZNlJDWvlj56i4MNrsw, on = "Kostenstelle",  how="inner")

#here we save the data from Token_rjYBI2SpXB_vU04xb_eg_g to the the output_icrev.xlsx into the  sheet Sheet1 and dont use the index
for col in Token_rjYBI2SpXB_vU04xb_eg_g.columns:
    if col.startswith("BACKTICK_QUOTED_STRING_"):
        Token_rjYBI2SpXB_vU04xb_eg_g.rename(columns={col:col[23:].replace("_", " ")}, inplace=True)
Token_rjYBI2SpXB_vU04xb_eg_g.to_excel("output_icrev.xlsx", sheet_name = "Sheet1", index = False)

