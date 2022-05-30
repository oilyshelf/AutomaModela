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
Token_ZIRsr7RGPB5ACh_4nfF8UA = None

#here we read the data provided by the ICR_Example.xlsx from the sheet Cats and set the index to None
Token_ZIRsr7RGPB5ACh_4nfF8UA = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Cats')
Token_ZIRsr7RGPB5ACh_4nfF8UA = Token_ZIRsr7RGPB5ACh_4nfF8UA.replace({np.nan:None})

#we get a subset of the dataframe with these columns ['Empfaenger', 'Object Abbreviation', 'Object Description', 'LeistArt', 'EmpfStelle', 'KKrs', 'Datum', 'Anzahl', 'ME', 'Erstellt am', 'GenehmDatum', 'Kontierungstext', 'Erfassungssystem']
Token_ZIRsr7RGPB5ACh_4nfF8UA = Token_ZIRsr7RGPB5ACh_4nfF8UA[['Empfaenger', 'Object Abbreviation', 'Object Description', 'LeistArt', 'EmpfStelle', 'KKrs', 'Datum', 'Anzahl', 'ME', 'Erstellt am', 'GenehmDatum', 'Kontierungstext', 'Erfassungssystem']]

#rename column from-> to {'EmpfStelle': 'Invoicing CC'}
Token_ZIRsr7RGPB5ACh_4nfF8UA=Token_ZIRsr7RGPB5ACh_4nfF8UA.rename(columns={'EmpfStelle': 'Invoicing CC'})

#Creating new Dataframe based on Token_ZIRsr7RGPB5ACh_4nfF8UA
Token_KIchXcaU0tz0_qqJivkBgw = Token_ZIRsr7RGPB5ACh_4nfF8UA.copy(True)

#Tokencreation
Token_YaXUtUALjkEDpsUiMgodPQ = None
#Here we try to evaluate the Expression @substr(`Kontierungstext`,1,7 ) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_KIchXcaU0tz0_qqJivkBgw["PPM_ID"] = Token_KIchXcaU0tz0_qqJivkBgw.eval('@substr(`Kontierungstext`,1,7 )', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@substr(`Kontierungstext`,1,7 )', "trying next")


#here we read the data provided by the ICR_Example.xlsx from the sheet Ppm and set the index to None
Token_YaXUtUALjkEDpsUiMgodPQ = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Ppm')
Token_YaXUtUALjkEDpsUiMgodPQ = Token_YaXUtUALjkEDpsUiMgodPQ.replace({np.nan:None})

#delete column
Token_KIchXcaU0tz0_qqJivkBgw = Token_KIchXcaU0tz0_qqJivkBgw.drop('Kontierungstext', axis = 1)
#we get a subset of the dataframe with these columns ['PPM_ID Zahl', 'geschlossen am', 'Gate', 'Status']
Token_YaXUtUALjkEDpsUiMgodPQ = Token_YaXUtUALjkEDpsUiMgodPQ[['PPM_ID Zahl', 'geschlossen am', 'Gate', 'Status']]

#Here we try to evaluate the Expression @to_int(`PPM_ID`) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_KIchXcaU0tz0_qqJivkBgw["PPM_ID"] = Token_KIchXcaU0tz0_qqJivkBgw.eval('@to_int(`PPM_ID`)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@to_int(`PPM_ID`)', "trying next")

#Here we try to query the Expression not @is_empty(`PPM_ID Zahl`) with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_YaXUtUALjkEDpsUiMgodPQ = Token_YaXUtUALjkEDpsUiMgodPQ.query('not @is_empty(`PPM_ID Zahl`)', **engine)
    except Exception:
        print(engine, "failed to query", 'not @is_empty(`PPM_ID Zahl`)', "trying next")

#Here we make an equi join two Dataframes
#rename column from-> to {'PPM_ID Zahl': 'PPM_ID'}
Token_YaXUtUALjkEDpsUiMgodPQ=Token_YaXUtUALjkEDpsUiMgodPQ.rename(columns={'PPM_ID Zahl': 'PPM_ID'})

Token_KIchXcaU0tz0_qqJivkBgw = Token_KIchXcaU0tz0_qqJivkBgw.merge(Token_YaXUtUALjkEDpsUiMgodPQ,on="PPM_ID", how="left")

Token_KIchXcaU0tz0_qqJivkBgw.replace({np.nan: None})
#Creating new Dataframe based on Token_KIchXcaU0tz0_qqJivkBgw
Token_KBFcrViqWsctUFKjbjexjw = Token_KIchXcaU0tz0_qqJivkBgw.copy(True)

#Tokencreation
Token_8EHUqCBq6gWOwz4IFNitWw = None

#here we read the data provided by the ICR_Example.xlsx from the sheet wbs and set the index to None
Token_8EHUqCBq6gWOwz4IFNitWw = pd.read_excel("ICR_Example.xlsx", sheet_name = 'wbs')
Token_8EHUqCBq6gWOwz4IFNitWw = Token_8EHUqCBq6gWOwz4IFNitWw.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'Stat. WBS Element': 'Empfaenger'}
Token_8EHUqCBq6gWOwz4IFNitWw=Token_8EHUqCBq6gWOwz4IFNitWw.rename(columns={'Stat. WBS Element': 'Empfaenger'})

Token_KBFcrViqWsctUFKjbjexjw = Token_KBFcrViqWsctUFKjbjexjw.merge(Token_8EHUqCBq6gWOwz4IFNitWw,on="Empfaenger", how="left")

Token_KBFcrViqWsctUFKjbjexjw.replace({np.nan: None})
#Creating new Dataframe based on Token_KBFcrViqWsctUFKjbjexjw
Token_jCPlLglVCVQko_smbh8sMQ = Token_KBFcrViqWsctUFKjbjexjw.copy(True)

#Tokencreation
Token_hpBhQUWBu5yuBxOXeTPdJg = None

#here we read the data provided by the ICR_Example.xlsx from the sheet Ngc and set the index to None
Token_hpBhQUWBu5yuBxOXeTPdJg = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Ngc')
Token_hpBhQUWBu5yuBxOXeTPdJg = Token_hpBhQUWBu5yuBxOXeTPdJg.replace({np.nan:None})

#Here we try to evaluate the Expression @strip(`NGC`) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_hpBhQUWBu5yuBxOXeTPdJg["NGC"] = Token_hpBhQUWBu5yuBxOXeTPdJg.eval('@strip(`NGC`)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@strip(`NGC`)', "trying next")

#Here we try to evaluate the Expression @split(`NGC`, " ") with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_hpBhQUWBu5yuBxOXeTPdJg["Kostenstelle"] = Token_hpBhQUWBu5yuBxOXeTPdJg.eval('@split(`NGC`, " ")', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@split(`NGC`, " ")', "trying next")

#delete column
Token_hpBhQUWBu5yuBxOXeTPdJg = Token_hpBhQUWBu5yuBxOXeTPdJg.drop('NGC', axis = 1)
#Here we make an equi join two Dataframes
#rename column from-> to {'Kostenstelle': 'Invoicing CC'}
Token_hpBhQUWBu5yuBxOXeTPdJg=Token_hpBhQUWBu5yuBxOXeTPdJg.rename(columns={'Kostenstelle': 'Invoicing CC'})

Token_jCPlLglVCVQko_smbh8sMQ = Token_jCPlLglVCVQko_smbh8sMQ.merge(Token_hpBhQUWBu5yuBxOXeTPdJg,on="Invoicing CC", how="left")

Token_jCPlLglVCVQko_smbh8sMQ.replace({np.nan: None})
#rename column from-> to {'abbr': 'Hauptabteilung'}
Token_jCPlLglVCVQko_smbh8sMQ=Token_jCPlLglVCVQko_smbh8sMQ.rename(columns={'abbr': 'Hauptabteilung'})

#Creating new Dataframe based on Token_jCPlLglVCVQko_smbh8sMQ
Token_GC_QpjwDRcYXnqBn8WnJUQ = Token_jCPlLglVCVQko_smbh8sMQ.copy(True)

#Tokencreation
Token_EnNghffWNvz_zE1L3AH0aA = None

#here we read the data provided by the ICR_Example.xlsx from the sheet stundensatz and set the index to None
Token_EnNghffWNvz_zE1L3AH0aA = pd.read_excel("ICR_Example.xlsx", sheet_name = 'stundensatz')
Token_EnNghffWNvz_zE1L3AH0aA = Token_EnNghffWNvz_zE1L3AH0aA.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_EnNghffWNvz_zE1L3AH0aA=Token_EnNghffWNvz_zE1L3AH0aA.rename(columns={'abt.': 'Hauptabteilung'})

Token_GC_QpjwDRcYXnqBn8WnJUQ = Token_GC_QpjwDRcYXnqBn8WnJUQ.merge(Token_EnNghffWNvz_zE1L3AH0aA,on="Hauptabteilung", how="left")

Token_GC_QpjwDRcYXnqBn8WnJUQ.replace({np.nan: None})
#Here we try to evaluate the Expression 0.0 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_GC_QpjwDRcYXnqBn8WnJUQ["Stundensatz"] = Token_GC_QpjwDRcYXnqBn8WnJUQ.eval('0.0', **engine)
    except Exception:
        print(engine, "failed to evaluate", '0.0', "trying next")

#Creating new Dataframe based on Token_GC_QpjwDRcYXnqBn8WnJUQ
Token_nyovnBiHhD3r0NwtrY_VGg = Token_GC_QpjwDRcYXnqBn8WnJUQ.copy(True)

#Here we try to query the Expression `KKrs` == "DE04" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_nyovnBiHhD3r0NwtrY_VGg = Token_nyovnBiHhD3r0NwtrY_VGg.query('`KKrs` == "DE04"', **engine)
    except Exception:
        print(engine, "failed to query", '`KKrs` == "DE04"', "trying next")

#Here we concate two Dataframes
Token_GC_QpjwDRcYXnqBn8WnJUQ = Token_GC_QpjwDRcYXnqBn8WnJUQ[~Token_GC_QpjwDRcYXnqBn8WnJUQ.apply(tuple, 1).isin(Token_nyovnBiHhD3r0NwtrY_VGg.apply(tuple, 1))]

#Here we try to evaluate the Expression `DE04` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_nyovnBiHhD3r0NwtrY_VGg["Stundensatz"] = Token_nyovnBiHhD3r0NwtrY_VGg.eval('`DE04`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`DE04`', "trying next")

#delete column
Token_nyovnBiHhD3r0NwtrY_VGg = Token_nyovnBiHhD3r0NwtrY_VGg.drop('DE37', axis = 1)
#delete column
Token_nyovnBiHhD3r0NwtrY_VGg = Token_nyovnBiHhD3r0NwtrY_VGg.drop('DE04', axis = 1)
#delete column
Token_nyovnBiHhD3r0NwtrY_VGg = Token_nyovnBiHhD3r0NwtrY_VGg.drop('DE41', axis = 1)
#Creating new Dataframe based on Token_nyovnBiHhD3r0NwtrY_VGg
Token_DG8Br84HvqYgF439BmVzdA = Token_nyovnBiHhD3r0NwtrY_VGg.copy(True)

#Tokencreation
Token_O6J5vM3CfntTR_tzRD_7jQ = None

#here we read the data provided by the ICR_Example.xlsx from the sheet cc_mapping and set the index to None
Token_O6J5vM3CfntTR_tzRD_7jQ = pd.read_excel("ICR_Example.xlsx", sheet_name = 'cc_mapping')
Token_O6J5vM3CfntTR_tzRD_7jQ = Token_O6J5vM3CfntTR_tzRD_7jQ.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'From': 'KKrs'}
Token_O6J5vM3CfntTR_tzRD_7jQ=Token_O6J5vM3CfntTR_tzRD_7jQ.rename(columns={'From': 'KKrs'})

Token_DG8Br84HvqYgF439BmVzdA = Token_DG8Br84HvqYgF439BmVzdA.merge(Token_O6J5vM3CfntTR_tzRD_7jQ,on="KKrs", how="left")

Token_DG8Br84HvqYgF439BmVzdA.replace({np.nan: None})
#Creating new Dataframe based on Token_DG8Br84HvqYgF439BmVzdA
Token_dS_0yh2vrs6AnONYdQG6vQ = Token_DG8Br84HvqYgF439BmVzdA.copy(True)

#Tokencreation
Token_d3MT0U8o7wlq6aAsxbBXqw = None

#here we read the data provided by the ICR_Example.xlsx from the sheet cc and set the index to None
Token_d3MT0U8o7wlq6aAsxbBXqw = pd.read_excel("ICR_Example.xlsx", sheet_name = 'cc')
Token_d3MT0U8o7wlq6aAsxbBXqw = Token_d3MT0U8o7wlq6aAsxbBXqw.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_d3MT0U8o7wlq6aAsxbBXqw=Token_d3MT0U8o7wlq6aAsxbBXqw.rename(columns={'abt.': 'Hauptabteilung'})

Token_dS_0yh2vrs6AnONYdQG6vQ = Token_dS_0yh2vrs6AnONYdQG6vQ.merge(Token_d3MT0U8o7wlq6aAsxbBXqw,on="Hauptabteilung", how="left")

Token_dS_0yh2vrs6AnONYdQG6vQ.replace({np.nan: None})
#Here we try to evaluate the Expression " " with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_dS_0yh2vrs6AnONYdQG6vQ["Purchasing Cost Center"] = Token_dS_0yh2vrs6AnONYdQG6vQ.eval('" "', **engine)
    except Exception:
        print(engine, "failed to evaluate", '" "', "trying next")

#Creating new Dataframe based on Token_dS_0yh2vrs6AnONYdQG6vQ
Token_ie5NbLXnCM1QMQbeftI2dg = Token_dS_0yh2vrs6AnONYdQG6vQ.copy(True)

#Here we try to query the Expression `To` == "DE37" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_ie5NbLXnCM1QMQbeftI2dg = Token_ie5NbLXnCM1QMQbeftI2dg.query('`To` == "DE37"', **engine)
    except Exception:
        print(engine, "failed to query", '`To` == "DE37"', "trying next")

#Here we concate two Dataframes
Token_dS_0yh2vrs6AnONYdQG6vQ = Token_dS_0yh2vrs6AnONYdQG6vQ[~Token_dS_0yh2vrs6AnONYdQG6vQ.apply(tuple, 1).isin(Token_ie5NbLXnCM1QMQbeftI2dg.apply(tuple, 1))]

#Here we try to evaluate the Expression `DE37` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_ie5NbLXnCM1QMQbeftI2dg["Purchasing Cost Center"] = Token_ie5NbLXnCM1QMQbeftI2dg.eval('`DE37`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`DE37`', "trying next")

#delete column
Token_ie5NbLXnCM1QMQbeftI2dg = Token_ie5NbLXnCM1QMQbeftI2dg.drop('DE37', axis = 1)
#delete column
Token_ie5NbLXnCM1QMQbeftI2dg = Token_ie5NbLXnCM1QMQbeftI2dg.drop('DE04', axis = 1)
#delete column
Token_ie5NbLXnCM1QMQbeftI2dg = Token_ie5NbLXnCM1QMQbeftI2dg.drop('DE41', axis = 1)
#delete column
Token_ie5NbLXnCM1QMQbeftI2dg = Token_ie5NbLXnCM1QMQbeftI2dg.drop('To', axis = 1)
#Creating new Dataframe based on Token_ie5NbLXnCM1QMQbeftI2dg
Token_7sNjYFys9smD8Q6HuB6_8g = Token_ie5NbLXnCM1QMQbeftI2dg.copy(True)

#Tokencreation
Token_4ekL7APr32XwrQl5lN9_9Q = None

#here we read the data provided by the ICR_Example.xlsx from the sheet ap and set the index to None
Token_4ekL7APr32XwrQl5lN9_9Q = pd.read_excel("ICR_Example.xlsx", sheet_name = 'ap')
Token_4ekL7APr32XwrQl5lN9_9Q = Token_4ekL7APr32XwrQl5lN9_9Q.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_4ekL7APr32XwrQl5lN9_9Q=Token_4ekL7APr32XwrQl5lN9_9Q.rename(columns={'abt.': 'Hauptabteilung'})

Token_7sNjYFys9smD8Q6HuB6_8g = Token_7sNjYFys9smD8Q6HuB6_8g.merge(Token_4ekL7APr32XwrQl5lN9_9Q,on="Hauptabteilung", how="left")

Token_7sNjYFys9smD8Q6HuB6_8g.replace({np.nan: None})
#Here we try to evaluate the Expression 0.0 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_7sNjYFys9smD8Q6HuB6_8g["AP Fachbereich"] = Token_7sNjYFys9smD8Q6HuB6_8g.eval('0.0', **engine)
    except Exception:
        print(engine, "failed to evaluate", '0.0', "trying next")

#Creating new Dataframe based on Token_7sNjYFys9smD8Q6HuB6_8g
Token_Sm1Ti18YWNKQ5IeAOe9pPA = Token_7sNjYFys9smD8Q6HuB6_8g.copy(True)

#Here we try to query the Expression `KKrs` == "DE04" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_Sm1Ti18YWNKQ5IeAOe9pPA = Token_Sm1Ti18YWNKQ5IeAOe9pPA.query('`KKrs` == "DE04"', **engine)
    except Exception:
        print(engine, "failed to query", '`KKrs` == "DE04"', "trying next")

#Here we concate two Dataframes
Token_7sNjYFys9smD8Q6HuB6_8g = Token_7sNjYFys9smD8Q6HuB6_8g[~Token_7sNjYFys9smD8Q6HuB6_8g.apply(tuple, 1).isin(Token_Sm1Ti18YWNKQ5IeAOe9pPA.apply(tuple, 1))]

#Here we try to evaluate the Expression `DE04` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_Sm1Ti18YWNKQ5IeAOe9pPA["AP Fachbereich"] = Token_Sm1Ti18YWNKQ5IeAOe9pPA.eval('`DE04`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`DE04`', "trying next")

#delete column
Token_Sm1Ti18YWNKQ5IeAOe9pPA = Token_Sm1Ti18YWNKQ5IeAOe9pPA.drop('DE37', axis = 1)
#delete column
Token_Sm1Ti18YWNKQ5IeAOe9pPA = Token_Sm1Ti18YWNKQ5IeAOe9pPA.drop('DE04', axis = 1)
#Here we try to evaluate the Expression `Anzahl` * `Stundensatz` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_Sm1Ti18YWNKQ5IeAOe9pPA["Gesamt"] = Token_Sm1Ti18YWNKQ5IeAOe9pPA.eval('`Anzahl` * `Stundensatz`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Anzahl` * `Stundensatz`', "trying next")

#here we save the data from Token_Sm1Ti18YWNKQ5IeAOe9pPA to the the icr.xlsx into the  sheet Sheet1 and dont use the index
for col in Token_Sm1Ti18YWNKQ5IeAOe9pPA.columns:
    if col.startswith("BACKTICK_QUOTED_STRING_"):
        Token_Sm1Ti18YWNKQ5IeAOe9pPA.rename(columns={col:col[23:].replace("_", " ")}, inplace=True)
Token_Sm1Ti18YWNKQ5IeAOe9pPA.to_excel("icr.xlsx", sheet_name = "Sheet1", index = False)

