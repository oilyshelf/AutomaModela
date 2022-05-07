import pandas as pd
import numpy as np
#to run this code u need python 3.x with these packages installed pandas, numpy, numexpr

#here we read the data provided by the beispiel.xlsx from the sheet Tabelle1 and set the index to None
Token_dI1zSjX3LBgfophZUIUjGg = pd.read_excel("beispiel.xlsx", sheet_name = 'Tabelle1')

#Here we try to evaluate the Expression Kostenstelle = "unknown" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_dI1zSjX3LBgfophZUIUjGg = Token_dI1zSjX3LBgfophZUIUjGg.eval('Kostenstelle = "unknown"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "unknown"', "trying next")

#Creating new Dataframe based on Token_dI1zSjX3LBgfophZUIUjGg
Token_E6AHBUva6yTsM873mk5QcQ = Token_dI1zSjX3LBgfophZUIUjGg.copy(True)

#Here we try to query the Expression Profitcenter == "P1" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_E6AHBUva6yTsM873mk5QcQ = Token_E6AHBUva6yTsM873mk5QcQ.query('Profitcenter == "P1"', **engine)
    except Exception:
        print(engine, "failed to query", 'Profitcenter == "P1"', "trying next")

#Creating new Dataframe based on Token_dI1zSjX3LBgfophZUIUjGg
Token_hB99vJepuu2E_PZ00y06ZQ = Token_dI1zSjX3LBgfophZUIUjGg.copy(True)

#Here we try to query the Expression Profitcenter == "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_hB99vJepuu2E_PZ00y06ZQ = Token_hB99vJepuu2E_PZ00y06ZQ.query('Profitcenter == "P2"', **engine)
    except Exception:
        print(engine, "failed to query", 'Profitcenter == "P2"', "trying next")

#Creating new Dataframe based on Token_dI1zSjX3LBgfophZUIUjGg
Token_DhZLUXEiXLByiPeJrpd22Q = Token_dI1zSjX3LBgfophZUIUjGg.copy(True)

#Here we try to query the Expression ~(Profitcenter == "P1") & ~(Profitcenter == "P2") with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_DhZLUXEiXLByiPeJrpd22Q = Token_DhZLUXEiXLByiPeJrpd22Q.query('~(Profitcenter == "P1") & ~(Profitcenter == "P2")', **engine)
    except Exception:
        print(engine, "failed to query", '~(Profitcenter == "P1") & ~(Profitcenter == "P2")', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_E6AHBUva6yTsM873mk5QcQ = Token_E6AHBUva6yTsM873mk5QcQ.eval('Kostenstelle = "K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K2"', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K1" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_hB99vJepuu2E_PZ00y06ZQ = Token_hB99vJepuu2E_PZ00y06ZQ.eval('Kostenstelle = "K1"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K1"', "trying next")

#Here we concate two Dataframes
Token_DhZLUXEiXLByiPeJrpd22Q = pd.concat([Token_DhZLUXEiXLByiPeJrpd22Q,Token_E6AHBUva6yTsM873mk5QcQ]).drop_duplicates(keep=True)

#Here we concate two Dataframes
Token_DhZLUXEiXLByiPeJrpd22Q = pd.concat([Token_DhZLUXEiXLByiPeJrpd22Q,Token_hB99vJepuu2E_PZ00y06ZQ]).drop_duplicates(keep=True)

#Here we try to evaluate the Expression Demo = "läuft gut" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_DhZLUXEiXLByiPeJrpd22Q = Token_DhZLUXEiXLByiPeJrpd22Q.eval('Demo = "läuft gut"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Demo = "läuft gut"', "trying next")


#here we save the data from Token_DhZLUXEiXLByiPeJrpd22Q to the the inktest.xlsx into the  sheet Sheet1 and dont use the index
Token_DhZLUXEiXLByiPeJrpd22Q.to_excel("inktest.xlsx", sheet_name = "Sheet1", index = False)

