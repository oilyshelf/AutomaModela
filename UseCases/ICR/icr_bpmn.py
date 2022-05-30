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
Token_qUTlaTH1s6eHLgd4WbCEfA = None

#here we read the data provided by the ICR_Example.xlsx from the sheet Cats and set the index to None
Token_qUTlaTH1s6eHLgd4WbCEfA = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Cats')
Token_qUTlaTH1s6eHLgd4WbCEfA = Token_qUTlaTH1s6eHLgd4WbCEfA.replace({np.nan:None})

#we get a subset of the dataframe with these columns ['Empfaenger', 'Object Abbreviation', 'Object Description', 'LeistArt', 'EmpfStelle', 'KKrs', 'Datum', 'Anzahl', 'ME', 'Erstellt am', 'GenehmDatum', 'Kontierungstext', 'Erfassungssystem']
Token_qUTlaTH1s6eHLgd4WbCEfA = Token_qUTlaTH1s6eHLgd4WbCEfA[['Empfaenger', 'Object Abbreviation', 'Object Description', 'LeistArt', 'EmpfStelle', 'KKrs', 'Datum', 'Anzahl', 'ME', 'Erstellt am', 'GenehmDatum', 'Kontierungstext', 'Erfassungssystem']]

#rename column from-> to {'EmpfStelle': 'Invoicing CC'}
Token_qUTlaTH1s6eHLgd4WbCEfA=Token_qUTlaTH1s6eHLgd4WbCEfA.rename(columns={'EmpfStelle': 'Invoicing CC'})

#Creating new Dataframe based on Token_qUTlaTH1s6eHLgd4WbCEfA
Token_rIsZX_CPad96_RwhBp0DGA = Token_qUTlaTH1s6eHLgd4WbCEfA.copy(True)

#Tokencreation
Token_W2Wyfi8dw8oOsYjRQ5a9oA = None
#Here we try to evaluate the Expression `PPM_ID` = @substr(`Kontierungstext`,1,7 ) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_rIsZX_CPad96_RwhBp0DGA = Token_rIsZX_CPad96_RwhBp0DGA.eval('`PPM_ID` = @substr(`Kontierungstext`,1,7 )', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`PPM_ID` = @substr(`Kontierungstext`,1,7 )', "trying next")


#here we read the data provided by the ICR_Example.xlsx from the sheet Ppm and set the index to None
Token_W2Wyfi8dw8oOsYjRQ5a9oA = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Ppm')
Token_W2Wyfi8dw8oOsYjRQ5a9oA = Token_W2Wyfi8dw8oOsYjRQ5a9oA.replace({np.nan:None})

#delete column
Token_rIsZX_CPad96_RwhBp0DGA = Token_rIsZX_CPad96_RwhBp0DGA.drop('Kontierungstext', axis = 1)
#we get a subset of the dataframe with these columns ['PPM_ID Zahl', 'geschlossen am', 'Gate', 'Status']
Token_W2Wyfi8dw8oOsYjRQ5a9oA = Token_W2Wyfi8dw8oOsYjRQ5a9oA[['PPM_ID Zahl', 'geschlossen am', 'Gate', 'Status']]

#Here we try to evaluate the Expression `PPM_ID` = @to_int(`PPM_ID`) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_rIsZX_CPad96_RwhBp0DGA = Token_rIsZX_CPad96_RwhBp0DGA.eval('`PPM_ID` = @to_int(`PPM_ID`)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`PPM_ID` = @to_int(`PPM_ID`)', "trying next")

#Here we try to query the Expression not @is_empty(`PPM_ID Zahl`) with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_W2Wyfi8dw8oOsYjRQ5a9oA = Token_W2Wyfi8dw8oOsYjRQ5a9oA.query('not @is_empty(`PPM_ID Zahl`)', **engine)
    except Exception:
        print(engine, "failed to query", 'not @is_empty(`PPM_ID Zahl`)', "trying next")

#Here we make an equi join two Dataframes
#rename column from-> to {'PPM_ID Zahl': 'PPM_ID'}
Token_W2Wyfi8dw8oOsYjRQ5a9oA=Token_W2Wyfi8dw8oOsYjRQ5a9oA.rename(columns={'PPM_ID Zahl': 'PPM_ID'})

Token_rIsZX_CPad96_RwhBp0DGA = Token_rIsZX_CPad96_RwhBp0DGA.merge(Token_W2Wyfi8dw8oOsYjRQ5a9oA,on="PPM_ID", how="left")

Token_rIsZX_CPad96_RwhBp0DGA.replace({np.nan: None})
#Creating new Dataframe based on Token_rIsZX_CPad96_RwhBp0DGA
Token_tBn09c1_Uhneu_e449Djgg = Token_rIsZX_CPad96_RwhBp0DGA.copy(True)

#Tokencreation
Token_8SzDAiFwZsC_6Kn_SbQWsQ = None

#here we read the data provided by the ICR_Example.xlsx from the sheet wbs and set the index to None
Token_8SzDAiFwZsC_6Kn_SbQWsQ = pd.read_excel("ICR_Example.xlsx", sheet_name = 'wbs')
Token_8SzDAiFwZsC_6Kn_SbQWsQ = Token_8SzDAiFwZsC_6Kn_SbQWsQ.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'Stat. WBS Element': 'Empfaenger'}
Token_8SzDAiFwZsC_6Kn_SbQWsQ=Token_8SzDAiFwZsC_6Kn_SbQWsQ.rename(columns={'Stat. WBS Element': 'Empfaenger'})

Token_tBn09c1_Uhneu_e449Djgg = Token_tBn09c1_Uhneu_e449Djgg.merge(Token_8SzDAiFwZsC_6Kn_SbQWsQ,on="Empfaenger", how="left")

Token_tBn09c1_Uhneu_e449Djgg.replace({np.nan: None})
#Creating new Dataframe based on Token_tBn09c1_Uhneu_e449Djgg
Token_JW54AitaX46jH0hwwM8k7Q = Token_tBn09c1_Uhneu_e449Djgg.copy(True)

#Tokencreation
Token_yE3DPOsrZo3Dj4pGSdNIng = None

#here we read the data provided by the ICR_Example.xlsx from the sheet Ngc and set the index to None
Token_yE3DPOsrZo3Dj4pGSdNIng = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Ngc')
Token_yE3DPOsrZo3Dj4pGSdNIng = Token_yE3DPOsrZo3Dj4pGSdNIng.replace({np.nan:None})

#Here we try to evaluate the Expression `NGC` = @strip(`NGC`) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_yE3DPOsrZo3Dj4pGSdNIng = Token_yE3DPOsrZo3Dj4pGSdNIng.eval('`NGC` = @strip(`NGC`)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`NGC` = @strip(`NGC`)', "trying next")

#Here we try to evaluate the Expression `Kostenstelle` = @split(`NGC`, " ") with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_yE3DPOsrZo3Dj4pGSdNIng = Token_yE3DPOsrZo3Dj4pGSdNIng.eval('`Kostenstelle` = @split(`NGC`, " ")', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Kostenstelle` = @split(`NGC`, " ")', "trying next")

#delete column
Token_yE3DPOsrZo3Dj4pGSdNIng = Token_yE3DPOsrZo3Dj4pGSdNIng.drop('NGC', axis = 1)
#Here we make an equi join two Dataframes
#rename column from-> to {'Kostenstelle': 'Invoicing CC'}
Token_yE3DPOsrZo3Dj4pGSdNIng=Token_yE3DPOsrZo3Dj4pGSdNIng.rename(columns={'Kostenstelle': 'Invoicing CC'})

Token_JW54AitaX46jH0hwwM8k7Q = Token_JW54AitaX46jH0hwwM8k7Q.merge(Token_yE3DPOsrZo3Dj4pGSdNIng,on="Invoicing CC", how="left")

Token_JW54AitaX46jH0hwwM8k7Q.replace({np.nan: None})
#rename column from-> to {'abbr': 'Hauptabteilung'}
Token_JW54AitaX46jH0hwwM8k7Q=Token_JW54AitaX46jH0hwwM8k7Q.rename(columns={'abbr': 'Hauptabteilung'})

#Creating new Dataframe based on Token_JW54AitaX46jH0hwwM8k7Q
Token_1S899DABbXVxjzBNJQ5VIA = Token_JW54AitaX46jH0hwwM8k7Q.copy(True)

#Tokencreation
Token_9Ri89pcfQo4q_vJxk4H38g = None

#here we read the data provided by the ICR_Example.xlsx from the sheet stundensatz and set the index to None
Token_9Ri89pcfQo4q_vJxk4H38g = pd.read_excel("ICR_Example.xlsx", sheet_name = 'stundensatz')
Token_9Ri89pcfQo4q_vJxk4H38g = Token_9Ri89pcfQo4q_vJxk4H38g.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_9Ri89pcfQo4q_vJxk4H38g=Token_9Ri89pcfQo4q_vJxk4H38g.rename(columns={'abt.': 'Hauptabteilung'})

Token_1S899DABbXVxjzBNJQ5VIA = Token_1S899DABbXVxjzBNJQ5VIA.merge(Token_9Ri89pcfQo4q_vJxk4H38g,on="Hauptabteilung", how="left")

Token_1S899DABbXVxjzBNJQ5VIA.replace({np.nan: None})
#Here we try to evaluate the Expression `Stundensatz` = 0.0 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_1S899DABbXVxjzBNJQ5VIA = Token_1S899DABbXVxjzBNJQ5VIA.eval('`Stundensatz` = 0.0', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Stundensatz` = 0.0', "trying next")

#Creating new Dataframe based on Token_1S899DABbXVxjzBNJQ5VIA
Token_AywWYghoUuHxre14QqZHIA = Token_1S899DABbXVxjzBNJQ5VIA.copy(True)

#Here we try to query the Expression `KKrs` == "DE04" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_AywWYghoUuHxre14QqZHIA = Token_AywWYghoUuHxre14QqZHIA.query('`KKrs` == "DE04"', **engine)
    except Exception:
        print(engine, "failed to query", '`KKrs` == "DE04"', "trying next")

#Here we concate two Dataframes
Token_1S899DABbXVxjzBNJQ5VIA = Token_1S899DABbXVxjzBNJQ5VIA[~Token_1S899DABbXVxjzBNJQ5VIA.apply(tuple, 1).isin(Token_AywWYghoUuHxre14QqZHIA.apply(tuple, 1))]

#Here we try to evaluate the Expression `Stundensatz` = `DE04` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_AywWYghoUuHxre14QqZHIA = Token_AywWYghoUuHxre14QqZHIA.eval('`Stundensatz` = `DE04`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Stundensatz` = `DE04`', "trying next")

#delete column
Token_AywWYghoUuHxre14QqZHIA = Token_AywWYghoUuHxre14QqZHIA.drop('DE37', axis = 1)
#delete column
Token_AywWYghoUuHxre14QqZHIA = Token_AywWYghoUuHxre14QqZHIA.drop('DE04', axis = 1)
#delete column
Token_AywWYghoUuHxre14QqZHIA = Token_AywWYghoUuHxre14QqZHIA.drop('DE41', axis = 1)
#Creating new Dataframe based on Token_AywWYghoUuHxre14QqZHIA
Token_ATo9bmSy7TQeyKm0HAmxMg = Token_AywWYghoUuHxre14QqZHIA.copy(True)

#Tokencreation
Token_jdNh4GuOHU_HeIiMJlstrQ = None

#here we read the data provided by the ICR_Example.xlsx from the sheet cc_mapping and set the index to None
Token_jdNh4GuOHU_HeIiMJlstrQ = pd.read_excel("ICR_Example.xlsx", sheet_name = 'cc_mapping')
Token_jdNh4GuOHU_HeIiMJlstrQ = Token_jdNh4GuOHU_HeIiMJlstrQ.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'From': 'KKrs'}
Token_jdNh4GuOHU_HeIiMJlstrQ=Token_jdNh4GuOHU_HeIiMJlstrQ.rename(columns={'From': 'KKrs'})

Token_ATo9bmSy7TQeyKm0HAmxMg = Token_ATo9bmSy7TQeyKm0HAmxMg.merge(Token_jdNh4GuOHU_HeIiMJlstrQ,on="KKrs", how="left")

Token_ATo9bmSy7TQeyKm0HAmxMg.replace({np.nan: None})
#Creating new Dataframe based on Token_ATo9bmSy7TQeyKm0HAmxMg
Token_7goy5jXg_781YWOoLefupg = Token_ATo9bmSy7TQeyKm0HAmxMg.copy(True)

#Tokencreation
Token_SeX6WgWX_BMylTzVmnfx4Q = None

#here we read the data provided by the ICR_Example.xlsx from the sheet cc and set the index to None
Token_SeX6WgWX_BMylTzVmnfx4Q = pd.read_excel("ICR_Example.xlsx", sheet_name = 'cc')
Token_SeX6WgWX_BMylTzVmnfx4Q = Token_SeX6WgWX_BMylTzVmnfx4Q.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_SeX6WgWX_BMylTzVmnfx4Q=Token_SeX6WgWX_BMylTzVmnfx4Q.rename(columns={'abt.': 'Hauptabteilung'})

Token_7goy5jXg_781YWOoLefupg = Token_7goy5jXg_781YWOoLefupg.merge(Token_SeX6WgWX_BMylTzVmnfx4Q,on="Hauptabteilung", how="left")

Token_7goy5jXg_781YWOoLefupg.replace({np.nan: None})
#Here we try to evaluate the Expression `Purchasing Cost Center` = " " with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_7goy5jXg_781YWOoLefupg = Token_7goy5jXg_781YWOoLefupg.eval('`Purchasing Cost Center` = " "', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Purchasing Cost Center` = " "', "trying next")

#Creating new Dataframe based on Token_7goy5jXg_781YWOoLefupg
Token_EFpglMbsgui4wADO_lZUrw = Token_7goy5jXg_781YWOoLefupg.copy(True)

#Here we try to query the Expression `To` == "DE37" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_EFpglMbsgui4wADO_lZUrw = Token_EFpglMbsgui4wADO_lZUrw.query('`To` == "DE37"', **engine)
    except Exception:
        print(engine, "failed to query", '`To` == "DE37"', "trying next")

#Here we concate two Dataframes
Token_7goy5jXg_781YWOoLefupg = Token_7goy5jXg_781YWOoLefupg[~Token_7goy5jXg_781YWOoLefupg.apply(tuple, 1).isin(Token_EFpglMbsgui4wADO_lZUrw.apply(tuple, 1))]

#Here we try to evaluate the Expression `Purchasing Cost Center` = `DE37` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_EFpglMbsgui4wADO_lZUrw = Token_EFpglMbsgui4wADO_lZUrw.eval('`Purchasing Cost Center` = `DE37`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Purchasing Cost Center` = `DE37`', "trying next")

#delete column
Token_EFpglMbsgui4wADO_lZUrw = Token_EFpglMbsgui4wADO_lZUrw.drop('DE37', axis = 1)
#delete column
Token_EFpglMbsgui4wADO_lZUrw = Token_EFpglMbsgui4wADO_lZUrw.drop('DE04', axis = 1)
#delete column
Token_EFpglMbsgui4wADO_lZUrw = Token_EFpglMbsgui4wADO_lZUrw.drop('DE41', axis = 1)
#delete column
Token_EFpglMbsgui4wADO_lZUrw = Token_EFpglMbsgui4wADO_lZUrw.drop('To', axis = 1)
#Creating new Dataframe based on Token_EFpglMbsgui4wADO_lZUrw
Token_4iv9qi0_w3n6a4mx6WtbdQ = Token_EFpglMbsgui4wADO_lZUrw.copy(True)

#Tokencreation
Token_K21cnq2VD81yJTrFzkBWew = None

#here we read the data provided by the ICR_Example.xlsx from the sheet ap and set the index to None
Token_K21cnq2VD81yJTrFzkBWew = pd.read_excel("ICR_Example.xlsx", sheet_name = 'ap')
Token_K21cnq2VD81yJTrFzkBWew = Token_K21cnq2VD81yJTrFzkBWew.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_K21cnq2VD81yJTrFzkBWew=Token_K21cnq2VD81yJTrFzkBWew.rename(columns={'abt.': 'Hauptabteilung'})

Token_4iv9qi0_w3n6a4mx6WtbdQ = Token_4iv9qi0_w3n6a4mx6WtbdQ.merge(Token_K21cnq2VD81yJTrFzkBWew,on="Hauptabteilung", how="left")

Token_4iv9qi0_w3n6a4mx6WtbdQ.replace({np.nan: None})
#Here we try to evaluate the Expression `AP Fachbereich` = 0.0 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_4iv9qi0_w3n6a4mx6WtbdQ = Token_4iv9qi0_w3n6a4mx6WtbdQ.eval('`AP Fachbereich` = 0.0', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`AP Fachbereich` = 0.0', "trying next")

#Creating new Dataframe based on Token_4iv9qi0_w3n6a4mx6WtbdQ
Token_I5Ou7Fqj1LkJSGErBD3ybQ = Token_4iv9qi0_w3n6a4mx6WtbdQ.copy(True)

#Here we try to query the Expression `KKrs` == "DE04" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_I5Ou7Fqj1LkJSGErBD3ybQ = Token_I5Ou7Fqj1LkJSGErBD3ybQ.query('`KKrs` == "DE04"', **engine)
    except Exception:
        print(engine, "failed to query", '`KKrs` == "DE04"', "trying next")

#Here we concate two Dataframes
Token_4iv9qi0_w3n6a4mx6WtbdQ = Token_4iv9qi0_w3n6a4mx6WtbdQ[~Token_4iv9qi0_w3n6a4mx6WtbdQ.apply(tuple, 1).isin(Token_I5Ou7Fqj1LkJSGErBD3ybQ.apply(tuple, 1))]

#Here we try to evaluate the Expression `AP Fachbereich` = `DE04` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_I5Ou7Fqj1LkJSGErBD3ybQ = Token_I5Ou7Fqj1LkJSGErBD3ybQ.eval('`AP Fachbereich` = `DE04`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`AP Fachbereich` = `DE04`', "trying next")

#delete column
Token_I5Ou7Fqj1LkJSGErBD3ybQ = Token_I5Ou7Fqj1LkJSGErBD3ybQ.drop('DE37', axis = 1)
#delete column
Token_I5Ou7Fqj1LkJSGErBD3ybQ = Token_I5Ou7Fqj1LkJSGErBD3ybQ.drop('DE04', axis = 1)
#Here we try to evaluate the Expression `Gesamt` = `Anzahl` * `Stundensatz` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_I5Ou7Fqj1LkJSGErBD3ybQ = Token_I5Ou7Fqj1LkJSGErBD3ybQ.eval('`Gesamt` = `Anzahl` * `Stundensatz`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Gesamt` = `Anzahl` * `Stundensatz`', "trying next")

#here we save the data from Token_I5Ou7Fqj1LkJSGErBD3ybQ to the the icr.xlsx into the  sheet Sheet1 and dont use the index
for col in Token_I5Ou7Fqj1LkJSGErBD3ybQ.columns:
    if col.startswith("BACKTICK_QUOTED_STRING_"):
        Token_I5Ou7Fqj1LkJSGErBD3ybQ.rename(columns={col:col[23:].replace("_", " ")}, inplace=True)
Token_I5Ou7Fqj1LkJSGErBD3ybQ.to_excel("icr.xlsx", sheet_name = "Sheet1", index = False)

