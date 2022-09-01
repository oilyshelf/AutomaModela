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
Token_lPPjwaXjJ9DNaV3v00S8jg = None

#here we read the data provided by the ICR_Example.xlsx from the sheet Cats and set the index to None
Token_lPPjwaXjJ9DNaV3v00S8jg = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Cats')
Token_lPPjwaXjJ9DNaV3v00S8jg = Token_lPPjwaXjJ9DNaV3v00S8jg.replace({np.nan:None})

#we get a subset of the dataframe with these columns ['Empfaenger', 'Object Abbreviation', 'Object Description', 'LeistArt', 'EmpfStelle', 'KKrs', 'Datum', 'Anzahl', 'ME', 'Erstellt am', 'GenehmDatum', 'Kontierungstext', 'Erfassungssystem']
Token_lPPjwaXjJ9DNaV3v00S8jg = Token_lPPjwaXjJ9DNaV3v00S8jg[['Empfaenger', 'Object Abbreviation', 'Object Description', 'LeistArt', 'EmpfStelle', 'KKrs', 'Datum', 'Anzahl', 'ME', 'Erstellt am', 'GenehmDatum', 'Kontierungstext', 'Erfassungssystem']]

#rename column from-> to {'EmpfStelle': 'Invoicing CC'}
Token_lPPjwaXjJ9DNaV3v00S8jg=Token_lPPjwaXjJ9DNaV3v00S8jg.rename(columns={'EmpfStelle': 'Invoicing CC'})

#Creating new Dataframe based on Token_lPPjwaXjJ9DNaV3v00S8jg
Token_sJ9_Obavim75gpuSCuzlXQ = Token_lPPjwaXjJ9DNaV3v00S8jg.copy(True)

#Tokencreation
Token_LrHm6m4LXrO1A0pTrqJcnw = None
#Here we try to evaluate the Expression @substr(`Kontierungstext`,1,7 ) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_sJ9_Obavim75gpuSCuzlXQ["PPM_ID"] = Token_sJ9_Obavim75gpuSCuzlXQ.eval('@substr(`Kontierungstext`,1,7 )', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@substr(`Kontierungstext`,1,7 )', "trying next")


#here we read the data provided by the ICR_Example.xlsx from the sheet Ppm and set the index to None
Token_LrHm6m4LXrO1A0pTrqJcnw = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Ppm')
Token_LrHm6m4LXrO1A0pTrqJcnw = Token_LrHm6m4LXrO1A0pTrqJcnw.replace({np.nan:None})

#delete column
Token_sJ9_Obavim75gpuSCuzlXQ = Token_sJ9_Obavim75gpuSCuzlXQ.drop('Kontierungstext', axis = 1)
#we get a subset of the dataframe with these columns ['PPM_ID Zahl', 'geschlossen am', 'Gate', 'Status']
Token_LrHm6m4LXrO1A0pTrqJcnw = Token_LrHm6m4LXrO1A0pTrqJcnw[['PPM_ID Zahl', 'geschlossen am', 'Gate', 'Status']]

#Here we try to evaluate the Expression @to_int(`PPM_ID`) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_sJ9_Obavim75gpuSCuzlXQ["PPM_ID"] = Token_sJ9_Obavim75gpuSCuzlXQ.eval('@to_int(`PPM_ID`)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@to_int(`PPM_ID`)', "trying next")

#Here we try to query the Expression not @is_empty(`PPM_ID Zahl`) with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_LrHm6m4LXrO1A0pTrqJcnw = Token_LrHm6m4LXrO1A0pTrqJcnw.query('not @is_empty(`PPM_ID Zahl`)', **engine)
    except Exception:
        print(engine, "failed to query", 'not @is_empty(`PPM_ID Zahl`)', "trying next")

#Here we make an equi join two Dataframes
#rename column from-> to {'PPM_ID Zahl': 'PPM_ID'}
Token_LrHm6m4LXrO1A0pTrqJcnw=Token_LrHm6m4LXrO1A0pTrqJcnw.rename(columns={'PPM_ID Zahl': 'PPM_ID'})

Token_sJ9_Obavim75gpuSCuzlXQ = Token_sJ9_Obavim75gpuSCuzlXQ.merge(Token_LrHm6m4LXrO1A0pTrqJcnw,on="PPM_ID", how="left")

Token_sJ9_Obavim75gpuSCuzlXQ.replace({np.nan: None})
#Creating new Dataframe based on Token_sJ9_Obavim75gpuSCuzlXQ
Token_K0Wqci8nCcDyXN_FbF5ZOA = Token_sJ9_Obavim75gpuSCuzlXQ.copy(True)

#Tokencreation
Token_0Y02NUgfLITXwfKYTSZMPw = None

#here we read the data provided by the ICR_Example.xlsx from the sheet wbs and set the index to None
Token_0Y02NUgfLITXwfKYTSZMPw = pd.read_excel("ICR_Example.xlsx", sheet_name = 'wbs')
Token_0Y02NUgfLITXwfKYTSZMPw = Token_0Y02NUgfLITXwfKYTSZMPw.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'Stat. WBS Element': 'Empfaenger'}
Token_0Y02NUgfLITXwfKYTSZMPw=Token_0Y02NUgfLITXwfKYTSZMPw.rename(columns={'Stat. WBS Element': 'Empfaenger'})

Token_K0Wqci8nCcDyXN_FbF5ZOA = Token_K0Wqci8nCcDyXN_FbF5ZOA.merge(Token_0Y02NUgfLITXwfKYTSZMPw,on="Empfaenger", how="left")

Token_K0Wqci8nCcDyXN_FbF5ZOA.replace({np.nan: None})
#Creating new Dataframe based on Token_K0Wqci8nCcDyXN_FbF5ZOA
Token_uQK8tC47HNF9sFy6HPe_mA = Token_K0Wqci8nCcDyXN_FbF5ZOA.copy(True)

#Tokencreation
Token_qPyxhG5WSOcLyaYl328TpQ = None

#here we read the data provided by the ICR_Example.xlsx from the sheet Ngc and set the index to None
Token_qPyxhG5WSOcLyaYl328TpQ = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Ngc')
Token_qPyxhG5WSOcLyaYl328TpQ = Token_qPyxhG5WSOcLyaYl328TpQ.replace({np.nan:None})

#Here we try to evaluate the Expression @strip(`NGC`) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_qPyxhG5WSOcLyaYl328TpQ["NGC"] = Token_qPyxhG5WSOcLyaYl328TpQ.eval('@strip(`NGC`)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@strip(`NGC`)', "trying next")

#Here we try to evaluate the Expression @split(`NGC`, " ") with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_qPyxhG5WSOcLyaYl328TpQ["Kostenstelle"] = Token_qPyxhG5WSOcLyaYl328TpQ.eval('@split(`NGC`, " ")', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@split(`NGC`, " ")', "trying next")

#delete column
Token_qPyxhG5WSOcLyaYl328TpQ = Token_qPyxhG5WSOcLyaYl328TpQ.drop('NGC', axis = 1)
#Here we make an equi join two Dataframes
#rename column from-> to {'Kostenstelle': 'Invoicing CC'}
Token_qPyxhG5WSOcLyaYl328TpQ=Token_qPyxhG5WSOcLyaYl328TpQ.rename(columns={'Kostenstelle': 'Invoicing CC'})

Token_uQK8tC47HNF9sFy6HPe_mA = Token_uQK8tC47HNF9sFy6HPe_mA.merge(Token_qPyxhG5WSOcLyaYl328TpQ,on="Invoicing CC", how="left")

Token_uQK8tC47HNF9sFy6HPe_mA.replace({np.nan: None})
#rename column from-> to {'abbr': 'Hauptabteilung'}
Token_uQK8tC47HNF9sFy6HPe_mA=Token_uQK8tC47HNF9sFy6HPe_mA.rename(columns={'abbr': 'Hauptabteilung'})

#Creating new Dataframe based on Token_uQK8tC47HNF9sFy6HPe_mA
Token_zXx3oBkpKGkaV65_weaLAA = Token_uQK8tC47HNF9sFy6HPe_mA.copy(True)

#Tokencreation
Token_dhYRlS8wyQg7W2J3REAVDg = None

#here we read the data provided by the ICR_Example.xlsx from the sheet stundensatz and set the index to None
Token_dhYRlS8wyQg7W2J3REAVDg = pd.read_excel("ICR_Example.xlsx", sheet_name = 'stundensatz')
Token_dhYRlS8wyQg7W2J3REAVDg = Token_dhYRlS8wyQg7W2J3REAVDg.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_dhYRlS8wyQg7W2J3REAVDg=Token_dhYRlS8wyQg7W2J3REAVDg.rename(columns={'abt.': 'Hauptabteilung'})

Token_zXx3oBkpKGkaV65_weaLAA = Token_zXx3oBkpKGkaV65_weaLAA.merge(Token_dhYRlS8wyQg7W2J3REAVDg,on="Hauptabteilung", how="left")

Token_zXx3oBkpKGkaV65_weaLAA.replace({np.nan: None})
#Here we try to evaluate the Expression 0.0 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_zXx3oBkpKGkaV65_weaLAA["Stundensatz"] = Token_zXx3oBkpKGkaV65_weaLAA.eval('0.0', **engine)
    except Exception:
        print(engine, "failed to evaluate", '0.0', "trying next")

#Creating new Dataframe based on Token_zXx3oBkpKGkaV65_weaLAA
Token_tisNbd7q6JBp1z_pp1QO9g = Token_zXx3oBkpKGkaV65_weaLAA.copy(True)

#Here we try to query the Expression `KKrs` == "DE04" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_tisNbd7q6JBp1z_pp1QO9g = Token_tisNbd7q6JBp1z_pp1QO9g.query('`KKrs` == "DE04"', **engine)
    except Exception:
        print(engine, "failed to query", '`KKrs` == "DE04"', "trying next")

#Here we concate two Dataframes
Token_zXx3oBkpKGkaV65_weaLAA = Token_zXx3oBkpKGkaV65_weaLAA[~Token_zXx3oBkpKGkaV65_weaLAA.apply(tuple, 1).isin(Token_tisNbd7q6JBp1z_pp1QO9g.apply(tuple, 1))]

#Here we try to evaluate the Expression `DE04` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_tisNbd7q6JBp1z_pp1QO9g["Stundensatz"] = Token_tisNbd7q6JBp1z_pp1QO9g.eval('`DE04`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`DE04`', "trying next")

#delete column
Token_tisNbd7q6JBp1z_pp1QO9g = Token_tisNbd7q6JBp1z_pp1QO9g.drop('DE37', axis = 1)
#delete column
Token_tisNbd7q6JBp1z_pp1QO9g = Token_tisNbd7q6JBp1z_pp1QO9g.drop('DE04', axis = 1)
#delete column
Token_tisNbd7q6JBp1z_pp1QO9g = Token_tisNbd7q6JBp1z_pp1QO9g.drop('DE41', axis = 1)
#Creating new Dataframe based on Token_tisNbd7q6JBp1z_pp1QO9g
Token_X1wSWx4xIl72E6BFWaE8Qg = Token_tisNbd7q6JBp1z_pp1QO9g.copy(True)

#Tokencreation
Token_YpZ6B4dfYaKhJih2D9zdjQ = None

#here we read the data provided by the ICR_Example.xlsx from the sheet cc_mapping and set the index to None
Token_YpZ6B4dfYaKhJih2D9zdjQ = pd.read_excel("ICR_Example.xlsx", sheet_name = 'cc_mapping')
Token_YpZ6B4dfYaKhJih2D9zdjQ = Token_YpZ6B4dfYaKhJih2D9zdjQ.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'From': 'KKrs'}
Token_YpZ6B4dfYaKhJih2D9zdjQ=Token_YpZ6B4dfYaKhJih2D9zdjQ.rename(columns={'From': 'KKrs'})

Token_X1wSWx4xIl72E6BFWaE8Qg = Token_X1wSWx4xIl72E6BFWaE8Qg.merge(Token_YpZ6B4dfYaKhJih2D9zdjQ,on="KKrs", how="left")

Token_X1wSWx4xIl72E6BFWaE8Qg.replace({np.nan: None})
#Creating new Dataframe based on Token_X1wSWx4xIl72E6BFWaE8Qg
Token_SVK5oHk2rmBePOfCE6MU2g = Token_X1wSWx4xIl72E6BFWaE8Qg.copy(True)

#Tokencreation
Token_SeDlaCyueLYMkWBXnPJX_w = None

#here we read the data provided by the ICR_Example.xlsx from the sheet cc and set the index to None
Token_SeDlaCyueLYMkWBXnPJX_w = pd.read_excel("ICR_Example.xlsx", sheet_name = 'cc')
Token_SeDlaCyueLYMkWBXnPJX_w = Token_SeDlaCyueLYMkWBXnPJX_w.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_SeDlaCyueLYMkWBXnPJX_w=Token_SeDlaCyueLYMkWBXnPJX_w.rename(columns={'abt.': 'Hauptabteilung'})

Token_SVK5oHk2rmBePOfCE6MU2g = Token_SVK5oHk2rmBePOfCE6MU2g.merge(Token_SeDlaCyueLYMkWBXnPJX_w,on="Hauptabteilung", how="left")

Token_SVK5oHk2rmBePOfCE6MU2g.replace({np.nan: None})
#Here we try to evaluate the Expression " " with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_SVK5oHk2rmBePOfCE6MU2g["Purchasing Cost Center"] = Token_SVK5oHk2rmBePOfCE6MU2g.eval('" "', **engine)
    except Exception:
        print(engine, "failed to evaluate", '" "', "trying next")

#Creating new Dataframe based on Token_SVK5oHk2rmBePOfCE6MU2g
Token_hneu4EHqdDporn5yoaTmfA = Token_SVK5oHk2rmBePOfCE6MU2g.copy(True)

#Here we try to query the Expression `To` == "DE37" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_hneu4EHqdDporn5yoaTmfA = Token_hneu4EHqdDporn5yoaTmfA.query('`To` == "DE37"', **engine)
    except Exception:
        print(engine, "failed to query", '`To` == "DE37"', "trying next")

#Here we concate two Dataframes
Token_SVK5oHk2rmBePOfCE6MU2g = Token_SVK5oHk2rmBePOfCE6MU2g[~Token_SVK5oHk2rmBePOfCE6MU2g.apply(tuple, 1).isin(Token_hneu4EHqdDporn5yoaTmfA.apply(tuple, 1))]

#Here we try to evaluate the Expression `DE37` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_hneu4EHqdDporn5yoaTmfA["Purchasing Cost Center"] = Token_hneu4EHqdDporn5yoaTmfA.eval('`DE37`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`DE37`', "trying next")

#delete column
Token_hneu4EHqdDporn5yoaTmfA = Token_hneu4EHqdDporn5yoaTmfA.drop('DE37', axis = 1)
#delete column
Token_hneu4EHqdDporn5yoaTmfA = Token_hneu4EHqdDporn5yoaTmfA.drop('DE04', axis = 1)
#delete column
Token_hneu4EHqdDporn5yoaTmfA = Token_hneu4EHqdDporn5yoaTmfA.drop('DE41', axis = 1)
#delete column
Token_hneu4EHqdDporn5yoaTmfA = Token_hneu4EHqdDporn5yoaTmfA.drop('To', axis = 1)
#Creating new Dataframe based on Token_hneu4EHqdDporn5yoaTmfA
Token_HrfQzBL19x6GMYwJZbyTQA = Token_hneu4EHqdDporn5yoaTmfA.copy(True)

#Tokencreation
Token_JFp3ggfIGvZeuFDRc_iDSA = None

#here we read the data provided by the ICR_Example.xlsx from the sheet ap and set the index to None
Token_JFp3ggfIGvZeuFDRc_iDSA = pd.read_excel("ICR_Example.xlsx", sheet_name = 'ap')
Token_JFp3ggfIGvZeuFDRc_iDSA = Token_JFp3ggfIGvZeuFDRc_iDSA.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_JFp3ggfIGvZeuFDRc_iDSA=Token_JFp3ggfIGvZeuFDRc_iDSA.rename(columns={'abt.': 'Hauptabteilung'})

Token_HrfQzBL19x6GMYwJZbyTQA = Token_HrfQzBL19x6GMYwJZbyTQA.merge(Token_JFp3ggfIGvZeuFDRc_iDSA,on="Hauptabteilung", how="left")

Token_HrfQzBL19x6GMYwJZbyTQA.replace({np.nan: None})
#Here we try to evaluate the Expression 0.0 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_HrfQzBL19x6GMYwJZbyTQA["AP Fachbereich"] = Token_HrfQzBL19x6GMYwJZbyTQA.eval('0.0', **engine)
    except Exception:
        print(engine, "failed to evaluate", '0.0', "trying next")

#Creating new Dataframe based on Token_HrfQzBL19x6GMYwJZbyTQA
Token_fbKUJQyQ4lvaaUSDhFflmQ = Token_HrfQzBL19x6GMYwJZbyTQA.copy(True)

#Here we try to query the Expression `KKrs` == "DE04" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_fbKUJQyQ4lvaaUSDhFflmQ = Token_fbKUJQyQ4lvaaUSDhFflmQ.query('`KKrs` == "DE04"', **engine)
    except Exception:
        print(engine, "failed to query", '`KKrs` == "DE04"', "trying next")

#Here we concate two Dataframes
Token_HrfQzBL19x6GMYwJZbyTQA = Token_HrfQzBL19x6GMYwJZbyTQA[~Token_HrfQzBL19x6GMYwJZbyTQA.apply(tuple, 1).isin(Token_fbKUJQyQ4lvaaUSDhFflmQ.apply(tuple, 1))]

#Here we try to evaluate the Expression `DE04` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_fbKUJQyQ4lvaaUSDhFflmQ["AP Fachbereich"] = Token_fbKUJQyQ4lvaaUSDhFflmQ.eval('`DE04`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`DE04`', "trying next")

#delete column
Token_fbKUJQyQ4lvaaUSDhFflmQ = Token_fbKUJQyQ4lvaaUSDhFflmQ.drop('DE37', axis = 1)
#delete column
Token_fbKUJQyQ4lvaaUSDhFflmQ = Token_fbKUJQyQ4lvaaUSDhFflmQ.drop('DE04', axis = 1)
#Here we try to evaluate the Expression `Anzahl` * `Stundensatz` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_fbKUJQyQ4lvaaUSDhFflmQ["Gesamt"] = Token_fbKUJQyQ4lvaaUSDhFflmQ.eval('`Anzahl` * `Stundensatz`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Anzahl` * `Stundensatz`', "trying next")

#here we save the data from Token_fbKUJQyQ4lvaaUSDhFflmQ to the the icr.xlsx into the  sheet Sheet1 and dont use the index
for col in Token_fbKUJQyQ4lvaaUSDhFflmQ.columns:
    if col.startswith("BACKTICK_QUOTED_STRING_"):
        Token_fbKUJQyQ4lvaaUSDhFflmQ.rename(columns={col:col[23:].replace("_", " ")}, inplace=True)
Token_fbKUJQyQ4lvaaUSDhFflmQ.to_excel("icr.xlsx", sheet_name = "Sheet1", index = False)

