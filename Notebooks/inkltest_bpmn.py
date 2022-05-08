import pandas as pd
import numpy as np
#to run this code u need python 3.x with these packages installed pandas, numpy, numexpr

#here we read the data provided by the beispiel.xlsx from the sheet Tabelle1 and set the index to None
Token_HtPUmRAUu25fhI2b0HQ8Zw = pd.read_excel("beispiel.xlsx", sheet_name = 'Tabelle1')

#Here we try to evaluate the Expression Kostenstelle = "unknown" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_HtPUmRAUu25fhI2b0HQ8Zw = Token_HtPUmRAUu25fhI2b0HQ8Zw.eval('Kostenstelle = "unknown"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "unknown"', "trying next")

#Creating new Dataframe based on Token_HtPUmRAUu25fhI2b0HQ8Zw
Token_l2cQulOoi3lvZ37fpldYNQ = Token_HtPUmRAUu25fhI2b0HQ8Zw.copy(True)

#Here we try to query the Expression  Profitcenter == "P1" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_l2cQulOoi3lvZ37fpldYNQ = Token_l2cQulOoi3lvZ37fpldYNQ.query(' Profitcenter == "P1"', **engine)
    except Exception:
        print(engine, "failed to query", ' Profitcenter == "P1"', "trying next")

#Creating new Dataframe based on Token_HtPUmRAUu25fhI2b0HQ8Zw
Token_TGfHdInnt3pLt5tUmFQvWQ = Token_HtPUmRAUu25fhI2b0HQ8Zw.copy(True)

#Here we try to query the Expression  Profitcenter == "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_TGfHdInnt3pLt5tUmFQvWQ = Token_TGfHdInnt3pLt5tUmFQvWQ.query(' Profitcenter == "P2"', **engine)
    except Exception:
        print(engine, "failed to query", ' Profitcenter == "P2"', "trying next")

#Creating new Dataframe based on Token_HtPUmRAUu25fhI2b0HQ8Zw
Token_TdhmfaWyirwTyahqWCISfA = Token_HtPUmRAUu25fhI2b0HQ8Zw.copy(True)

#Here we try to query the Expression ~( Profitcenter == "P1") & ~( Profitcenter == "P2") with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_TdhmfaWyirwTyahqWCISfA = Token_TdhmfaWyirwTyahqWCISfA.query('~( Profitcenter == "P1") & ~( Profitcenter == "P2")', **engine)
    except Exception:
        print(engine, "failed to query", '~( Profitcenter == "P1") & ~( Profitcenter == "P2")', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_l2cQulOoi3lvZ37fpldYNQ = Token_l2cQulOoi3lvZ37fpldYNQ.eval('Kostenstelle = "K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K2"', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K1" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_TGfHdInnt3pLt5tUmFQvWQ = Token_TGfHdInnt3pLt5tUmFQvWQ.eval('Kostenstelle = "K1"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K1"', "trying next")

#Here we concate two Dataframes
Token_l2cQulOoi3lvZ37fpldYNQ = pd.concat([Token_l2cQulOoi3lvZ37fpldYNQ,Token_TGfHdInnt3pLt5tUmFQvWQ]).drop_duplicates(keep=True)

#Here we concate two Dataframes
Token_l2cQulOoi3lvZ37fpldYNQ = pd.concat([Token_l2cQulOoi3lvZ37fpldYNQ,Token_TdhmfaWyirwTyahqWCISfA]).drop_duplicates(keep=True)


#here we save the data from Token_l2cQulOoi3lvZ37fpldYNQ to the the inktest.xlsx into the  sheet Sheet1 and dont use the index
Token_l2cQulOoi3lvZ37fpldYNQ.to_excel("inktest.xlsx", sheet_name = "Sheet1", index = False)

