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
Token_ZjrPfoOMjq8THFmtB5ZiHg = None

#here we read the data provided by the SalesRecords.xlsx from the sheet Sales and set the index to None
Token_ZjrPfoOMjq8THFmtB5ZiHg = pd.read_excel("SalesRecords.xlsx", sheet_name = 'Sales')
Token_ZjrPfoOMjq8THFmtB5ZiHg = Token_ZjrPfoOMjq8THFmtB5ZiHg.replace({np.nan:None})

#Here we try to evaluate the Expression `Amount`-`Returns` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_ZjrPfoOMjq8THFmtB5ZiHg[Amount of Actual Sales] = Token_ZjrPfoOMjq8THFmtB5ZiHg.eval('`Amount`-`Returns`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Amount`-`Returns`', "trying next")

#Tokencreation
Token_6UzFDGscEAh3mDtYCpqSPw = None
#Creating new Dataframe based on Token_ZjrPfoOMjq8THFmtB5ZiHg
Token_rM3KaAIDx9GuQtT5kqUOjw = Token_ZjrPfoOMjq8THFmtB5ZiHg.copy(True)


#here we read the data provided by the SalesRecords.xlsx from the sheet Products and set the index to None
Token_6UzFDGscEAh3mDtYCpqSPw = pd.read_excel("SalesRecords.xlsx", sheet_name = 'Products')
Token_6UzFDGscEAh3mDtYCpqSPw = Token_6UzFDGscEAh3mDtYCpqSPw.replace({np.nan:None})

#rename column from-> to {'Name': 'Product Name'}
Token_6UzFDGscEAh3mDtYCpqSPw=Token_6UzFDGscEAh3mDtYCpqSPw.rename(columns={'Name': 'Product Name'})

#rename column from-> to {'Selling Price in Dollar': 'Selling Price'}
Token_6UzFDGscEAh3mDtYCpqSPw=Token_6UzFDGscEAh3mDtYCpqSPw.rename(columns={'Selling Price in Dollar': 'Selling Price'})

#natural join on columns 
Token_rM3KaAIDx9GuQtT5kqUOjw.merge(Token_6UzFDGscEAh3mDtYCpqSPw, how = 'inner')
#Here we try to evaluate the Expression `Selling Price` * `Amount of Actual Sales` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_rM3KaAIDx9GuQtT5kqUOjw[Revenue] = Token_rM3KaAIDx9GuQtT5kqUOjw.eval('`Selling Price` * `Amount of Actual Sales`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Selling Price` * `Amount of Actual Sales`', "trying next")

#Tokencreation
Token_9eqm0SsC1eloREYFpCmCCA = None
#Creating new Dataframe based on Token_rM3KaAIDx9GuQtT5kqUOjw
Token_uScFajcg67OAvq8C2VG0pQ = Token_rM3KaAIDx9GuQtT5kqUOjw.copy(True)


#here we read the data provided by the SalesRecords.xlsx from the sheet Stores and set the index to None
Token_9eqm0SsC1eloREYFpCmCCA = pd.read_excel("SalesRecords.xlsx", sheet_name = 'Stores')
Token_9eqm0SsC1eloREYFpCmCCA = Token_9eqm0SsC1eloREYFpCmCCA.replace({np.nan:None})

#Here we try to evaluate the Expression @split(`Store Information`, " ") with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_9eqm0SsC1eloREYFpCmCCA[Store ID] = Token_9eqm0SsC1eloREYFpCmCCA.eval('@split(`Store Information`, " ")', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@split(`Store Information`, " ")', "trying next")

#Here we try to evaluate the Expression @substr(`Store Information`,8) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_9eqm0SsC1eloREYFpCmCCA[Store Name] = Token_9eqm0SsC1eloREYFpCmCCA.eval('@substr(`Store Information`,8)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@substr(`Store Information`,8)', "trying next")

#delete column
Token_9eqm0SsC1eloREYFpCmCCA = Token_9eqm0SsC1eloREYFpCmCCA.drop('Store Information', axis = 1)
#natural join on columns 
Token_uScFajcg67OAvq8C2VG0pQ.merge(Token_9eqm0SsC1eloREYFpCmCCA, how = 'inner')
#Creating new Dataframe based on Token_uScFajcg67OAvq8C2VG0pQ
Token_wJciW0wXFcYdkaIZX6uqAg = Token_uScFajcg67OAvq8C2VG0pQ.copy(True)

#Tokencreation
Token_FEJIbbTAme_h8AdNOeajaA = None

#here we read the data provided by the SalesRecords.xlsx from the sheet Taxes and set the index to None
Token_FEJIbbTAme_h8AdNOeajaA = pd.read_excel("SalesRecords.xlsx", sheet_name = 'Taxes')
Token_FEJIbbTAme_h8AdNOeajaA = Token_FEJIbbTAme_h8AdNOeajaA.replace({np.nan:None})

#delete column
Token_FEJIbbTAme_h8AdNOeajaA = Token_FEJIbbTAme_h8AdNOeajaA.drop('Country', axis = 1)
#Here we cross two Dataframes
Token_wJciW0wXFcYdkaIZX6uqAg = Token_wJciW0wXFcYdkaIZX6uqAg.merge(Token_FEJIbbTAme_h8AdNOeajaA, how = "cross")

#Here we try to evaluate the Expression 0 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_wJciW0wXFcYdkaIZX6uqAg[Taxesrate] = Token_wJciW0wXFcYdkaIZX6uqAg.eval('0', **engine)
    except Exception:
        print(engine, "failed to evaluate", '0', "trying next")

#Creating new Dataframe based on Token_wJciW0wXFcYdkaIZX6uqAg
Token_VXVkd7y0txn2s0UDy0jUTw = Token_wJciW0wXFcYdkaIZX6uqAg.copy(True)

#Here we try to query the Expression `Country` == "Germany" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_VXVkd7y0txn2s0UDy0jUTw = Token_VXVkd7y0txn2s0UDy0jUTw.query('`Country` == "Germany"', **engine)
    except Exception:
        print(engine, "failed to query", '`Country` == "Germany"', "trying next")

#Here we concate two Dataframes
Token_wJciW0wXFcYdkaIZX6uqAg = Token_wJciW0wXFcYdkaIZX6uqAg[~Token_wJciW0wXFcYdkaIZX6uqAg.apply(tuple, 1).isin(Token_VXVkd7y0txn2s0UDy0jUTw.apply(tuple, 1))]

#Creating new Dataframe based on Token_wJciW0wXFcYdkaIZX6uqAg
Token_3_k_II7wrFVAKl998Z5PgQ = Token_wJciW0wXFcYdkaIZX6uqAg.copy(True)

#Here we try to query the Expression `Country` == "USA" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_3_k_II7wrFVAKl998Z5PgQ = Token_3_k_II7wrFVAKl998Z5PgQ.query('`Country` == "USA"', **engine)
    except Exception:
        print(engine, "failed to query", '`Country` == "USA"', "trying next")

#Here we concate two Dataframes
Token_wJciW0wXFcYdkaIZX6uqAg = Token_wJciW0wXFcYdkaIZX6uqAg[~Token_wJciW0wXFcYdkaIZX6uqAg.apply(tuple, 1).isin(Token_3_k_II7wrFVAKl998Z5PgQ.apply(tuple, 1))]

#Creating new Dataframe based on Token_wJciW0wXFcYdkaIZX6uqAg
Token_iVAayOZFCoEfUgXwlzqerA = Token_wJciW0wXFcYdkaIZX6uqAg.copy(True)

#Here we try to query the Expression `Country` == "France" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_iVAayOZFCoEfUgXwlzqerA = Token_iVAayOZFCoEfUgXwlzqerA.query('`Country` == "France"', **engine)
    except Exception:
        print(engine, "failed to query", '`Country` == "France"', "trying next")

#Here we concate two Dataframes
Token_wJciW0wXFcYdkaIZX6uqAg = Token_wJciW0wXFcYdkaIZX6uqAg[~Token_wJciW0wXFcYdkaIZX6uqAg.apply(tuple, 1).isin(Token_iVAayOZFCoEfUgXwlzqerA.apply(tuple, 1))]

#Here we try to evaluate the Expression `Germany` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_VXVkd7y0txn2s0UDy0jUTw[Taxesrate] = Token_VXVkd7y0txn2s0UDy0jUTw.eval('`Germany`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Germany`', "trying next")

#Here we try to evaluate the Expression `USA` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_3_k_II7wrFVAKl998Z5PgQ[Taxesrate] = Token_3_k_II7wrFVAKl998Z5PgQ.eval('`USA`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`USA`', "trying next")

#Here we try to evaluate the Expression `France` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_iVAayOZFCoEfUgXwlzqerA[Taxesrate] = Token_iVAayOZFCoEfUgXwlzqerA.eval('`France`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`France`', "trying next")

#Here we concate two Dataframes
Token_VXVkd7y0txn2s0UDy0jUTw = pd.concat([Token_VXVkd7y0txn2s0UDy0jUTw,Token_3_k_II7wrFVAKl998Z5PgQ])

#Here we concate two Dataframes
Token_VXVkd7y0txn2s0UDy0jUTw = pd.concat([Token_VXVkd7y0txn2s0UDy0jUTw,Token_iVAayOZFCoEfUgXwlzqerA])

#Here we try to evaluate the Expression `Taxesrate`/100 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_VXVkd7y0txn2s0UDy0jUTw[Taxesrate] = Token_VXVkd7y0txn2s0UDy0jUTw.eval('`Taxesrate`/100', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Taxesrate`/100', "trying next")

#Here we try to evaluate the Expression `Revenue` * (1-`Taxesrate`) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_VXVkd7y0txn2s0UDy0jUTw[Revenue after Taxes] = Token_VXVkd7y0txn2s0UDy0jUTw.eval('`Revenue` * (1-`Taxesrate`)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Revenue` * (1-`Taxesrate`)', "trying next")

#Here we try to evaluate the Expression `Amount of Actual Sales` * `Production Cost in Dollar` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_VXVkd7y0txn2s0UDy0jUTw[Production Cost Total] = Token_VXVkd7y0txn2s0UDy0jUTw.eval('`Amount of Actual Sales` * `Production Cost in Dollar`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Amount of Actual Sales` * `Production Cost in Dollar`', "trying next")

#Here we try to evaluate the Expression `Revenue after Taxes` - `Production Cost Total` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_VXVkd7y0txn2s0UDy0jUTw[Profit] = Token_VXVkd7y0txn2s0UDy0jUTw.eval('`Revenue after Taxes` - `Production Cost Total`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Revenue after Taxes` - `Production Cost Total`', "trying next")

#we get a subset of the dataframe with these columns ['Store Name', 'Product Name', 'Selling Price', 'Amount of Actual Sales', 'Revenue', 'Revenue after Taxes', 'Profit']
Token_VXVkd7y0txn2s0UDy0jUTw = Token_VXVkd7y0txn2s0UDy0jUTw[['Store Name', 'Product Name', 'Selling Price', 'Amount of Actual Sales', 'Revenue', 'Revenue after Taxes', 'Profit']]

#here we save the data from Token_VXVkd7y0txn2s0UDy0jUTw to the the Store_Performance_2022.xlsx into the  sheet Sheet1 and dont use the index
for col in Token_VXVkd7y0txn2s0UDy0jUTw.columns:
    if col.startswith("BACKTICK_QUOTED_STRING_"):
        Token_VXVkd7y0txn2s0UDy0jUTw.rename(columns={col:col[23:].replace("_", " ")}, inplace=True)
Token_VXVkd7y0txn2s0UDy0jUTw.to_excel("Store_Performance_2022.xlsx", sheet_name = "Sheet1", index = False)

