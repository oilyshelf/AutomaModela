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
Token_eysO78esAVJ6dJ6e1VfXPw = None

#here we read the data provided by the ICR_Example.xlsx from the sheet Cats and set the index to None
Token_eysO78esAVJ6dJ6e1VfXPw = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Cats')
Token_eysO78esAVJ6dJ6e1VfXPw = Token_eysO78esAVJ6dJ6e1VfXPw.replace({np.nan:None})

#we get a subset of the dataframe with these columns ['Empfaenger', 'Object Abbreviation', 'Object Description', 'LeistArt', 'EmpfStelle', 'KKrs', 'Datum', 'Anzahl', 'ME', 'Erstellt am', 'GenehmDatum', 'Kontierungstext', 'Erfassungssystem']
Token_eysO78esAVJ6dJ6e1VfXPw = Token_eysO78esAVJ6dJ6e1VfXPw[['Empfaenger', 'Object Abbreviation', 'Object Description', 'LeistArt', 'EmpfStelle', 'KKrs', 'Datum', 'Anzahl', 'ME', 'Erstellt am', 'GenehmDatum', 'Kontierungstext', 'Erfassungssystem']]

#rename column from-> to {'EmpfStelle': 'Invoicing CC'}
Token_eysO78esAVJ6dJ6e1VfXPw=Token_eysO78esAVJ6dJ6e1VfXPw.rename(columns={'EmpfStelle': 'Invoicing CC'})

#Creating new Dataframe based on Token_eysO78esAVJ6dJ6e1VfXPw
Token_augkBIIMuh0YhU_P40SZ6w = Token_eysO78esAVJ6dJ6e1VfXPw.copy(True)

#Tokencreation
Token_JLUulantn8EoaSHmC1Y0rA = None
#Here we try to evaluate the Expression @substr(`Kontierungstext`,1,7 ) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_augkBIIMuh0YhU_P40SZ6w["PPM_ID"] = Token_augkBIIMuh0YhU_P40SZ6w.eval('@substr(`Kontierungstext`,1,7 )', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@substr(`Kontierungstext`,1,7 )', "trying next")


#here we read the data provided by the ICR_Example.xlsx from the sheet Ppm and set the index to None
Token_JLUulantn8EoaSHmC1Y0rA = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Ppm')
Token_JLUulantn8EoaSHmC1Y0rA = Token_JLUulantn8EoaSHmC1Y0rA.replace({np.nan:None})

#delete column
Token_augkBIIMuh0YhU_P40SZ6w = Token_augkBIIMuh0YhU_P40SZ6w.drop('Kontierungstext', axis = 1)
#we get a subset of the dataframe with these columns ['PPM_ID Zahl', 'geschlossen am', 'Gate', 'Status']
Token_JLUulantn8EoaSHmC1Y0rA = Token_JLUulantn8EoaSHmC1Y0rA[['PPM_ID Zahl', 'geschlossen am', 'Gate', 'Status']]

#Here we try to evaluate the Expression @to_int(`PPM_ID`) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_augkBIIMuh0YhU_P40SZ6w["PPM_ID"] = Token_augkBIIMuh0YhU_P40SZ6w.eval('@to_int(`PPM_ID`)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@to_int(`PPM_ID`)', "trying next")

#Here we try to query the Expression not @is_empty(`PPM_ID Zahl`) with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_JLUulantn8EoaSHmC1Y0rA = Token_JLUulantn8EoaSHmC1Y0rA.query('not @is_empty(`PPM_ID Zahl`)', **engine)
    except Exception:
        print(engine, "failed to query", 'not @is_empty(`PPM_ID Zahl`)', "trying next")

#Here we make an equi join two Dataframes
#rename column from-> to {'PPM_ID Zahl': 'PPM_ID'}
Token_JLUulantn8EoaSHmC1Y0rA=Token_JLUulantn8EoaSHmC1Y0rA.rename(columns={'PPM_ID Zahl': 'PPM_ID'})

Token_augkBIIMuh0YhU_P40SZ6w = Token_augkBIIMuh0YhU_P40SZ6w.merge(Token_JLUulantn8EoaSHmC1Y0rA,on="PPM_ID", how="left")

Token_augkBIIMuh0YhU_P40SZ6w.replace({np.nan: None})
#Creating new Dataframe based on Token_augkBIIMuh0YhU_P40SZ6w
Token_bunim4BrQN2m2us_rbbC0g = Token_augkBIIMuh0YhU_P40SZ6w.copy(True)

#Tokencreation
Token_Dz_ZZL_LQHncBFrF31DJSA = None

#here we read the data provided by the ICR_Example.xlsx from the sheet wbs and set the index to None
Token_Dz_ZZL_LQHncBFrF31DJSA = pd.read_excel("ICR_Example.xlsx", sheet_name = 'wbs')
Token_Dz_ZZL_LQHncBFrF31DJSA = Token_Dz_ZZL_LQHncBFrF31DJSA.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'Stat. WBS Element': 'Empfaenger'}
Token_Dz_ZZL_LQHncBFrF31DJSA=Token_Dz_ZZL_LQHncBFrF31DJSA.rename(columns={'Stat. WBS Element': 'Empfaenger'})

Token_bunim4BrQN2m2us_rbbC0g = Token_bunim4BrQN2m2us_rbbC0g.merge(Token_Dz_ZZL_LQHncBFrF31DJSA,on="Empfaenger", how="left")

Token_bunim4BrQN2m2us_rbbC0g.replace({np.nan: None})
#Creating new Dataframe based on Token_bunim4BrQN2m2us_rbbC0g
Token_AcZRFfI6gaRqrmxPKcL8zg = Token_bunim4BrQN2m2us_rbbC0g.copy(True)

#Tokencreation
Token_hDOkaOkrWwOiH_Y8Ia6Z0A = None

#here we read the data provided by the ICR_Example.xlsx from the sheet Ngc and set the index to None
Token_hDOkaOkrWwOiH_Y8Ia6Z0A = pd.read_excel("ICR_Example.xlsx", sheet_name = 'Ngc')
Token_hDOkaOkrWwOiH_Y8Ia6Z0A = Token_hDOkaOkrWwOiH_Y8Ia6Z0A.replace({np.nan:None})

#Here we try to evaluate the Expression @strip(`NGC`) with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_hDOkaOkrWwOiH_Y8Ia6Z0A["NGC"] = Token_hDOkaOkrWwOiH_Y8Ia6Z0A.eval('@strip(`NGC`)', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@strip(`NGC`)', "trying next")

#Here we try to evaluate the Expression @split(`NGC`, " ") with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_hDOkaOkrWwOiH_Y8Ia6Z0A["Kostenstelle"] = Token_hDOkaOkrWwOiH_Y8Ia6Z0A.eval('@split(`NGC`, " ")', **engine)
    except Exception:
        print(engine, "failed to evaluate", '@split(`NGC`, " ")', "trying next")

#delete column
Token_hDOkaOkrWwOiH_Y8Ia6Z0A = Token_hDOkaOkrWwOiH_Y8Ia6Z0A.drop('NGC', axis = 1)
#Here we make an equi join two Dataframes
#rename column from-> to {'Kostenstelle': 'Invoicing CC'}
Token_hDOkaOkrWwOiH_Y8Ia6Z0A=Token_hDOkaOkrWwOiH_Y8Ia6Z0A.rename(columns={'Kostenstelle': 'Invoicing CC'})

Token_AcZRFfI6gaRqrmxPKcL8zg = Token_AcZRFfI6gaRqrmxPKcL8zg.merge(Token_hDOkaOkrWwOiH_Y8Ia6Z0A,on="Invoicing CC", how="left")

Token_AcZRFfI6gaRqrmxPKcL8zg.replace({np.nan: None})
#rename column from-> to {'abbr': 'Hauptabteilung'}
Token_AcZRFfI6gaRqrmxPKcL8zg=Token_AcZRFfI6gaRqrmxPKcL8zg.rename(columns={'abbr': 'Hauptabteilung'})

#Creating new Dataframe based on Token_AcZRFfI6gaRqrmxPKcL8zg
Token_T_L4haCaBRy2I7hKoyBhCQ = Token_AcZRFfI6gaRqrmxPKcL8zg.copy(True)

#Tokencreation
Token_tqaF6kf4IGW4qnFedIUd7Q = None

#here we read the data provided by the ICR_Example.xlsx from the sheet stundensatz and set the index to None
Token_tqaF6kf4IGW4qnFedIUd7Q = pd.read_excel("ICR_Example.xlsx", sheet_name = 'stundensatz')
Token_tqaF6kf4IGW4qnFedIUd7Q = Token_tqaF6kf4IGW4qnFedIUd7Q.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_tqaF6kf4IGW4qnFedIUd7Q=Token_tqaF6kf4IGW4qnFedIUd7Q.rename(columns={'abt.': 'Hauptabteilung'})

Token_T_L4haCaBRy2I7hKoyBhCQ = Token_T_L4haCaBRy2I7hKoyBhCQ.merge(Token_tqaF6kf4IGW4qnFedIUd7Q,on="Hauptabteilung", how="left")

Token_T_L4haCaBRy2I7hKoyBhCQ.replace({np.nan: None})
#Here we try to evaluate the Expression 0.0 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_T_L4haCaBRy2I7hKoyBhCQ["Stundensatz"] = Token_T_L4haCaBRy2I7hKoyBhCQ.eval('0.0', **engine)
    except Exception:
        print(engine, "failed to evaluate", '0.0', "trying next")

#Creating new Dataframe based on Token_T_L4haCaBRy2I7hKoyBhCQ
Token_DcrMZ98h2vQIyxXBzVbdwg = Token_T_L4haCaBRy2I7hKoyBhCQ.copy(True)

#Here we try to query the Expression `KKrs` == "DE04" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_DcrMZ98h2vQIyxXBzVbdwg = Token_DcrMZ98h2vQIyxXBzVbdwg.query('`KKrs` == "DE04"', **engine)
    except Exception:
        print(engine, "failed to query", '`KKrs` == "DE04"', "trying next")

#Here we concate two Dataframes
Token_T_L4haCaBRy2I7hKoyBhCQ = Token_T_L4haCaBRy2I7hKoyBhCQ[~Token_T_L4haCaBRy2I7hKoyBhCQ.apply(tuple, 1).isin(Token_DcrMZ98h2vQIyxXBzVbdwg.apply(tuple, 1))]

#Here we try to evaluate the Expression `DE04` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_DcrMZ98h2vQIyxXBzVbdwg["Stundensatz"] = Token_DcrMZ98h2vQIyxXBzVbdwg.eval('`DE04`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`DE04`', "trying next")

#delete column
Token_DcrMZ98h2vQIyxXBzVbdwg = Token_DcrMZ98h2vQIyxXBzVbdwg.drop('DE37', axis = 1)
#delete column
Token_DcrMZ98h2vQIyxXBzVbdwg = Token_DcrMZ98h2vQIyxXBzVbdwg.drop('DE04', axis = 1)
#delete column
Token_DcrMZ98h2vQIyxXBzVbdwg = Token_DcrMZ98h2vQIyxXBzVbdwg.drop('DE41', axis = 1)
#Creating new Dataframe based on Token_DcrMZ98h2vQIyxXBzVbdwg
Token_dJMQlhyA6pNaj0HXn9HLUg = Token_DcrMZ98h2vQIyxXBzVbdwg.copy(True)

#Tokencreation
Token_5JTMYJsanQLkKWm8JpQEfw = None

#here we read the data provided by the ICR_Example.xlsx from the sheet cc_mapping and set the index to None
Token_5JTMYJsanQLkKWm8JpQEfw = pd.read_excel("ICR_Example.xlsx", sheet_name = 'cc_mapping')
Token_5JTMYJsanQLkKWm8JpQEfw = Token_5JTMYJsanQLkKWm8JpQEfw.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'From': 'KKrs'}
Token_5JTMYJsanQLkKWm8JpQEfw=Token_5JTMYJsanQLkKWm8JpQEfw.rename(columns={'From': 'KKrs'})

Token_dJMQlhyA6pNaj0HXn9HLUg = Token_dJMQlhyA6pNaj0HXn9HLUg.merge(Token_5JTMYJsanQLkKWm8JpQEfw,on="KKrs", how="left")

Token_dJMQlhyA6pNaj0HXn9HLUg.replace({np.nan: None})
#Creating new Dataframe based on Token_dJMQlhyA6pNaj0HXn9HLUg
Token_GwCuyXczAnveMSTpnJQV1w = Token_dJMQlhyA6pNaj0HXn9HLUg.copy(True)

#Tokencreation
Token_2N5wnMJ7vNqpHtJ1ci5Fzg = None

#here we read the data provided by the ICR_Example.xlsx from the sheet cc and set the index to None
Token_2N5wnMJ7vNqpHtJ1ci5Fzg = pd.read_excel("ICR_Example.xlsx", sheet_name = 'cc')
Token_2N5wnMJ7vNqpHtJ1ci5Fzg = Token_2N5wnMJ7vNqpHtJ1ci5Fzg.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_2N5wnMJ7vNqpHtJ1ci5Fzg=Token_2N5wnMJ7vNqpHtJ1ci5Fzg.rename(columns={'abt.': 'Hauptabteilung'})

Token_GwCuyXczAnveMSTpnJQV1w = Token_GwCuyXczAnveMSTpnJQV1w.merge(Token_2N5wnMJ7vNqpHtJ1ci5Fzg,on="Hauptabteilung", how="left")

Token_GwCuyXczAnveMSTpnJQV1w.replace({np.nan: None})
#Here we try to evaluate the Expression " " with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_GwCuyXczAnveMSTpnJQV1w["Purchasing Cost Center"] = Token_GwCuyXczAnveMSTpnJQV1w.eval('" "', **engine)
    except Exception:
        print(engine, "failed to evaluate", '" "', "trying next")

#Creating new Dataframe based on Token_GwCuyXczAnveMSTpnJQV1w
Token_uCYVNJvkWtdX1_hk0GXSuQ = Token_GwCuyXczAnveMSTpnJQV1w.copy(True)

#Here we try to query the Expression `To` == "DE37" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_uCYVNJvkWtdX1_hk0GXSuQ = Token_uCYVNJvkWtdX1_hk0GXSuQ.query('`To` == "DE37"', **engine)
    except Exception:
        print(engine, "failed to query", '`To` == "DE37"', "trying next")

#Here we concate two Dataframes
Token_GwCuyXczAnveMSTpnJQV1w = Token_GwCuyXczAnveMSTpnJQV1w[~Token_GwCuyXczAnveMSTpnJQV1w.apply(tuple, 1).isin(Token_uCYVNJvkWtdX1_hk0GXSuQ.apply(tuple, 1))]

#Here we try to evaluate the Expression `DE37` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_uCYVNJvkWtdX1_hk0GXSuQ["Purchasing Cost Center"] = Token_uCYVNJvkWtdX1_hk0GXSuQ.eval('`DE37`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`DE37`', "trying next")

#delete column
Token_uCYVNJvkWtdX1_hk0GXSuQ = Token_uCYVNJvkWtdX1_hk0GXSuQ.drop('DE37', axis = 1)
#delete column
Token_uCYVNJvkWtdX1_hk0GXSuQ = Token_uCYVNJvkWtdX1_hk0GXSuQ.drop('DE04', axis = 1)
#delete column
Token_uCYVNJvkWtdX1_hk0GXSuQ = Token_uCYVNJvkWtdX1_hk0GXSuQ.drop('DE41', axis = 1)
#delete column
Token_uCYVNJvkWtdX1_hk0GXSuQ = Token_uCYVNJvkWtdX1_hk0GXSuQ.drop('To', axis = 1)
#Creating new Dataframe based on Token_uCYVNJvkWtdX1_hk0GXSuQ
Token_L6_Pe7WkREbiAfgup434og = Token_uCYVNJvkWtdX1_hk0GXSuQ.copy(True)

#Tokencreation
Token_hxvXyywZ3tPGrRS_36pWFw = None

#here we read the data provided by the ICR_Example.xlsx from the sheet ap and set the index to None
Token_hxvXyywZ3tPGrRS_36pWFw = pd.read_excel("ICR_Example.xlsx", sheet_name = 'ap')
Token_hxvXyywZ3tPGrRS_36pWFw = Token_hxvXyywZ3tPGrRS_36pWFw.replace({np.nan:None})

#Here we make an equi join two Dataframes
#rename column from-> to {'abt.': 'Hauptabteilung'}
Token_hxvXyywZ3tPGrRS_36pWFw=Token_hxvXyywZ3tPGrRS_36pWFw.rename(columns={'abt.': 'Hauptabteilung'})

Token_L6_Pe7WkREbiAfgup434og = Token_L6_Pe7WkREbiAfgup434og.merge(Token_hxvXyywZ3tPGrRS_36pWFw,on="Hauptabteilung", how="left")

Token_L6_Pe7WkREbiAfgup434og.replace({np.nan: None})
#Here we try to evaluate the Expression 0.0 with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_L6_Pe7WkREbiAfgup434og["AP Fachbereich"] = Token_L6_Pe7WkREbiAfgup434og.eval('0.0', **engine)
    except Exception:
        print(engine, "failed to evaluate", '0.0', "trying next")

#Creating new Dataframe based on Token_L6_Pe7WkREbiAfgup434og
Token_Lqu8QnxJYd7tMFBocrS8Vg = Token_L6_Pe7WkREbiAfgup434og.copy(True)

#Here we try to query the Expression `KKrs` == "DE04" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_Lqu8QnxJYd7tMFBocrS8Vg = Token_Lqu8QnxJYd7tMFBocrS8Vg.query('`KKrs` == "DE04"', **engine)
    except Exception:
        print(engine, "failed to query", '`KKrs` == "DE04"', "trying next")

#Here we concate two Dataframes
Token_L6_Pe7WkREbiAfgup434og = Token_L6_Pe7WkREbiAfgup434og[~Token_L6_Pe7WkREbiAfgup434og.apply(tuple, 1).isin(Token_Lqu8QnxJYd7tMFBocrS8Vg.apply(tuple, 1))]

#Here we try to evaluate the Expression `DE04` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_Lqu8QnxJYd7tMFBocrS8Vg["AP Fachbereich"] = Token_Lqu8QnxJYd7tMFBocrS8Vg.eval('`DE04`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`DE04`', "trying next")

#delete column
Token_Lqu8QnxJYd7tMFBocrS8Vg = Token_Lqu8QnxJYd7tMFBocrS8Vg.drop('DE37', axis = 1)
#delete column
Token_Lqu8QnxJYd7tMFBocrS8Vg = Token_Lqu8QnxJYd7tMFBocrS8Vg.drop('DE04', axis = 1)
#Here we try to evaluate the Expression `Anzahl` * `Stundensatz` with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_Lqu8QnxJYd7tMFBocrS8Vg["Gesamt"] = Token_Lqu8QnxJYd7tMFBocrS8Vg.eval('`Anzahl` * `Stundensatz`', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Anzahl` * `Stundensatz`', "trying next")

#here we save the data from Token_Lqu8QnxJYd7tMFBocrS8Vg to the the icr.xlsx into the  sheet Sheet1 and dont use the index
for col in Token_Lqu8QnxJYd7tMFBocrS8Vg.columns:
    if col.startswith("BACKTICK_QUOTED_STRING_"):
        Token_Lqu8QnxJYd7tMFBocrS8Vg.rename(columns={col:col[23:].replace("_", " ")}, inplace=True)
Token_Lqu8QnxJYd7tMFBocrS8Vg.to_excel("icr.xlsx", sheet_name = "Sheet1", index = False)

