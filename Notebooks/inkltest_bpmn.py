import pandas as pd
import numpy as np
#to run this code u need python 3.x with these packages installed pandas, numpy, numexpr

#here we read the data provided by the beispiel.xlsx from the sheet Tabelle1 and set the index to None
Token_VIu_VIgrOMVvdEGsRfnN9A = pd.read_excel("beispiel.xlsx", sheet_name = 'Tabelle1')

#Here we try to evaluate the Expression Kostenstelle = "unknown" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_VIu_VIgrOMVvdEGsRfnN9A = Token_VIu_VIgrOMVvdEGsRfnN9A.eval('Kostenstelle = "unknown"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "unknown"', "trying next")

#Creating new Dataframe based on Token_VIu_VIgrOMVvdEGsRfnN9A
Token_a5QfkB9oR3Rv8A5rEPZC5g = Token_VIu_VIgrOMVvdEGsRfnN9A.copy(True)

#Here we try to query the Expression Profitcenter == "P1" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_a5QfkB9oR3Rv8A5rEPZC5g = Token_a5QfkB9oR3Rv8A5rEPZC5g.query('Profitcenter == "P1"', **engine)
    except Exception:
        print(engine, "failed to query", 'Profitcenter == "P1"', "trying next")

#Creating new Dataframe based on Token_VIu_VIgrOMVvdEGsRfnN9A
Token_BaCpVJyfZDwgWLd8dwPUAA = Token_VIu_VIgrOMVvdEGsRfnN9A.copy(True)

#Here we try to query the Expression Profitcenter == "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_BaCpVJyfZDwgWLd8dwPUAA = Token_BaCpVJyfZDwgWLd8dwPUAA.query('Profitcenter == "P2"', **engine)
    except Exception:
        print(engine, "failed to query", 'Profitcenter == "P2"', "trying next")

#Creating new Dataframe based on Token_VIu_VIgrOMVvdEGsRfnN9A
Token_h7QIAt9_jJnBedCMmd1K_w = Token_VIu_VIgrOMVvdEGsRfnN9A.copy(True)

#Here we try to query the Expression Profitcenter != "P1" and Profitcenter != "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_h7QIAt9_jJnBedCMmd1K_w = Token_h7QIAt9_jJnBedCMmd1K_w.query('Profitcenter != "P1" and Profitcenter != "P2"', **engine)
    except Exception:
        print(engine, "failed to query", 'Profitcenter != "P1" and Profitcenter != "P2"', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_a5QfkB9oR3Rv8A5rEPZC5g = Token_a5QfkB9oR3Rv8A5rEPZC5g.eval('Kostenstelle = "K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K2"', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K1" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_BaCpVJyfZDwgWLd8dwPUAA = Token_BaCpVJyfZDwgWLd8dwPUAA.eval('Kostenstelle = "K1"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K1"', "trying next")

#Here we concate two Dataframes
Token_h7QIAt9_jJnBedCMmd1K_w = pd.concat([Token_h7QIAt9_jJnBedCMmd1K_w,Token_a5QfkB9oR3Rv8A5rEPZC5g])

#Here we concate two Dataframes
Token_h7QIAt9_jJnBedCMmd1K_w = pd.concat([Token_h7QIAt9_jJnBedCMmd1K_w,Token_BaCpVJyfZDwgWLd8dwPUAA])


#here we save the data from Token_h7QIAt9_jJnBedCMmd1K_w to the the inktest.xlsx into the  sheet Sheet1 and dont use the index
Token_h7QIAt9_jJnBedCMmd1K_w.to_excel("inktest.xlsx", sheet_name = "Sheet1", index = False)

