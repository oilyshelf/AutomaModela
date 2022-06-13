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
Token__DfThK6dK9CmFvZhecVm_Q = None

#here we read the data provided by the SalesRecords.xlsx from the sheet Sales and set the index to None
Token__DfThK6dK9CmFvZhecVm_Q = pd.read_excel("SalesRecords.xlsx", sheet_name = 'Sales')
Token__DfThK6dK9CmFvZhecVm_Q = Token__DfThK6dK9CmFvZhecVm_Q.replace({np.nan:None})

#Here we try to evaluate the Expression `Amount`-`Returns` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token__DfThK6dK9CmFvZhecVm_Q["Amount of Actual Sales"] = Token__DfThK6dK9CmFvZhecVm_Q.eval('`Amount`-`Returns`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Amount`-`Returns`', "trying next")

#Tokencreation
Token_zx8khJyb7JXot4aVgqEDmA = None
#Creating new Dataframe based on Token__DfThK6dK9CmFvZhecVm_Q
Token_mjxqiDpEXQ_DCpcuzcpBMQ = Token__DfThK6dK9CmFvZhecVm_Q.copy(True)


#here we read the data provided by the SalesRecords.xlsx from the sheet Products and set the index to None
Token_zx8khJyb7JXot4aVgqEDmA = pd.read_excel("SalesRecords.xlsx", sheet_name = 'Products')
Token_zx8khJyb7JXot4aVgqEDmA = Token_zx8khJyb7JXot4aVgqEDmA.replace({np.nan:None})

#rename column from-> to {'Name': 'Product Name'}
Token_zx8khJyb7JXot4aVgqEDmA=Token_zx8khJyb7JXot4aVgqEDmA.rename(columns={'Name': 'Product Name'})

#rename column from-> to {'Selling Price in Dollar': 'Selling Price'}
Token_zx8khJyb7JXot4aVgqEDmA=Token_zx8khJyb7JXot4aVgqEDmA.rename(columns={'Selling Price in Dollar': 'Selling Price'})

#natural join on columns 
Token_mjxqiDpEXQ_DCpcuzcpBMQ.merge(Token_zx8khJyb7JXot4aVgqEDmA, how = 'inner')
#Here we try to evaluate the Expression `Selling Price` * `Amount of Actual Sales` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_mjxqiDpEXQ_DCpcuzcpBMQ["Revenue"] = Token_mjxqiDpEXQ_DCpcuzcpBMQ.eval('`Selling Price` * `Amount of Actual Sales`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Selling Price` * `Amount of Actual Sales`', "trying next")

#Tokencreation
Token_YoI_uyRN5Amrxvvamps_xA = None
#Creating new Dataframe based on Token_mjxqiDpEXQ_DCpcuzcpBMQ
Token_a_2DcBXTwnTVVwHqpTsaDw = Token_mjxqiDpEXQ_DCpcuzcpBMQ.copy(True)


#here we read the data provided by the SalesRecords.xlsx from the sheet Stores and set the index to None
Token_YoI_uyRN5Amrxvvamps_xA = pd.read_excel("SalesRecords.xlsx", sheet_name = 'Stores')
Token_YoI_uyRN5Amrxvvamps_xA = Token_YoI_uyRN5Amrxvvamps_xA.replace({np.nan:None})

#Here we try to evaluate the Expression @split(`Store Information`, " ") with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_YoI_uyRN5Amrxvvamps_xA["Store ID"] = Token_YoI_uyRN5Amrxvvamps_xA.eval('@split(`Store Information`, " ")', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@split(`Store Information`, " ")', "trying next")

#Here we try to evaluate the Expression @substr(`Store Information`,8) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_YoI_uyRN5Amrxvvamps_xA["Store Name"] = Token_YoI_uyRN5Amrxvvamps_xA.eval('@substr(`Store Information`,8)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@substr(`Store Information`,8)', "trying next")

#delete column
Token_YoI_uyRN5Amrxvvamps_xA = Token_YoI_uyRN5Amrxvvamps_xA.drop('Store Information', axis = 1)
#natural join on columns 
Token_a_2DcBXTwnTVVwHqpTsaDw.merge(Token_YoI_uyRN5Amrxvvamps_xA, how = 'inner')
#Creating new Dataframe based on Token_a_2DcBXTwnTVVwHqpTsaDw
Token_I8szL5PxNOfwu4B39g8N7w = Token_a_2DcBXTwnTVVwHqpTsaDw.copy(True)

#Tokencreation
Token_irswc3UV23Y1jwh_ZQ2K1A = None

#here we read the data provided by the SalesRecords.xlsx from the sheet Taxes and set the index to None
Token_irswc3UV23Y1jwh_ZQ2K1A = pd.read_excel("SalesRecords.xlsx", sheet_name = 'Taxes')
Token_irswc3UV23Y1jwh_ZQ2K1A = Token_irswc3UV23Y1jwh_ZQ2K1A.replace({np.nan:None})

#delete column
Token_irswc3UV23Y1jwh_ZQ2K1A = Token_irswc3UV23Y1jwh_ZQ2K1A.drop('Country', axis = 1)
#Here we cross two Dataframes
Token_I8szL5PxNOfwu4B39g8N7w = Token_I8szL5PxNOfwu4B39g8N7w.merge(Token_irswc3UV23Y1jwh_ZQ2K1A, how = "cross")

#Here we try to evaluate the Expression 0 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_I8szL5PxNOfwu4B39g8N7w["Taxesrate"] = Token_I8szL5PxNOfwu4B39g8N7w.eval('0', **engine)
    except Exception:
        print(engine, "failed to evaluate", '0', "trying next")

#Creating new Dataframe based on Token_I8szL5PxNOfwu4B39g8N7w
Token__3Iard0HjUEPSdegTyPEOw = Token_I8szL5PxNOfwu4B39g8N7w.copy(True)

#Here we try to query the Expression `Country` == "Germany" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token__3Iard0HjUEPSdegTyPEOw = Token__3Iard0HjUEPSdegTyPEOw.query('`Country` == "Germany"', **engine)
    except Exception:
        print(engine, "failed to query", '`Country` == "Germany"', "trying next")

#Here we concate two Dataframes
Token_I8szL5PxNOfwu4B39g8N7w = Token_I8szL5PxNOfwu4B39g8N7w[~Token_I8szL5PxNOfwu4B39g8N7w.apply(tuple, 1).isin(Token__3Iard0HjUEPSdegTyPEOw.apply(tuple, 1))]

#Creating new Dataframe based on Token_I8szL5PxNOfwu4B39g8N7w
Token_urOAOgDjBPGXURABZCt43A = Token_I8szL5PxNOfwu4B39g8N7w.copy(True)

#Here we try to query the Expression `Country` == "USA" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_urOAOgDjBPGXURABZCt43A = Token_urOAOgDjBPGXURABZCt43A.query('`Country` == "USA"', **engine)
    except Exception:
        print(engine, "failed to query", '`Country` == "USA"', "trying next")

#Here we concate two Dataframes
Token_I8szL5PxNOfwu4B39g8N7w = Token_I8szL5PxNOfwu4B39g8N7w[~Token_I8szL5PxNOfwu4B39g8N7w.apply(tuple, 1).isin(Token_urOAOgDjBPGXURABZCt43A.apply(tuple, 1))]

#Creating new Dataframe based on Token_I8szL5PxNOfwu4B39g8N7w
Token_EyQ76eBn1iNj0XkzIDH1SQ = Token_I8szL5PxNOfwu4B39g8N7w.copy(True)

#Here we try to query the Expression `Country` == "France" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_EyQ76eBn1iNj0XkzIDH1SQ = Token_EyQ76eBn1iNj0XkzIDH1SQ.query('`Country` == "France"', **engine)
    except Exception:
        print(engine, "failed to query", '`Country` == "France"', "trying next")

#Here we concate two Dataframes
Token_I8szL5PxNOfwu4B39g8N7w = Token_I8szL5PxNOfwu4B39g8N7w[~Token_I8szL5PxNOfwu4B39g8N7w.apply(tuple, 1).isin(Token_EyQ76eBn1iNj0XkzIDH1SQ.apply(tuple, 1))]

#Here we try to evaluate the Expression `Germany` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token__3Iard0HjUEPSdegTyPEOw["Taxesrate"] = Token__3Iard0HjUEPSdegTyPEOw.eval('`Germany`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Germany`', "trying next")

#Here we try to evaluate the Expression `USA` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_urOAOgDjBPGXURABZCt43A["Taxesrate"] = Token_urOAOgDjBPGXURABZCt43A.eval('`USA`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`USA`', "trying next")

#Here we try to evaluate the Expression `France` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_EyQ76eBn1iNj0XkzIDH1SQ["Taxesrate"] = Token_EyQ76eBn1iNj0XkzIDH1SQ.eval('`France`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`France`', "trying next")

#Here we concate two Dataframes
Token__3Iard0HjUEPSdegTyPEOw = pd.concat([Token__3Iard0HjUEPSdegTyPEOw,Token_urOAOgDjBPGXURABZCt43A])

#Here we concate two Dataframes
Token__3Iard0HjUEPSdegTyPEOw = pd.concat([Token__3Iard0HjUEPSdegTyPEOw,Token_EyQ76eBn1iNj0XkzIDH1SQ])

#Here we try to evaluate the Expression `Taxesrate`/100 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token__3Iard0HjUEPSdegTyPEOw["Taxesrate"] = Token__3Iard0HjUEPSdegTyPEOw.eval('`Taxesrate`/100', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Taxesrate`/100', "trying next")

#Here we try to evaluate the Expression `Revenue` * (1-`Taxesrate`) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token__3Iard0HjUEPSdegTyPEOw["Revenue after Taxes"] = Token__3Iard0HjUEPSdegTyPEOw.eval('`Revenue` * (1-`Taxesrate`)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Revenue` * (1-`Taxesrate`)', "trying next")

#Here we try to evaluate the Expression `Amount of Actual Sales` * `Production Cost in Dollar` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token__3Iard0HjUEPSdegTyPEOw["Production Cost Total"] = Token__3Iard0HjUEPSdegTyPEOw.eval('`Amount of Actual Sales` * `Production Cost in Dollar`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Amount of Actual Sales` * `Production Cost in Dollar`', "trying next")

#Here we try to evaluate the Expression `Revenue after Taxes` - `Production Cost Total` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token__3Iard0HjUEPSdegTyPEOw["Profit"] = Token__3Iard0HjUEPSdegTyPEOw.eval('`Revenue after Taxes` - `Production Cost Total`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Revenue after Taxes` - `Production Cost Total`', "trying next")

#we get a subset of the dataframe with these columns ['Store Name', 'Product Name', 'Selling Price', 'Amount of Actual Sales', 'Revenue', 'Revenue after Taxes', 'Profit']
Token__3Iard0HjUEPSdegTyPEOw = Token__3Iard0HjUEPSdegTyPEOw[['Store Name', 'Product Name', 'Selling Price', 'Amount of Actual Sales', 'Revenue', 'Revenue after Taxes', 'Profit']]

#here we save the data from Token__3Iard0HjUEPSdegTyPEOw to the the Store_Performance_2022.xlsx into the  sheet Sheet1 and dont use the index
for col in Token__3Iard0HjUEPSdegTyPEOw.columns:
    if col.startswith("BACKTICK_QUOTED_STRING_"):
        Token__3Iard0HjUEPSdegTyPEOw.rename(columns={col:col[23:].replace("_", " ")}, inplace=True)
Token__3Iard0HjUEPSdegTyPEOw.to_excel("Store_Performance_2022.xlsx", sheet_name = "Sheet1", index = False)

