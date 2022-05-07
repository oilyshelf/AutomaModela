import pandas as pd
import numpy as np
#to run this code u need python 3.x with these packages installed pandas, numpy, numexpr

#here we read the data provided by the beispiel.xlsx from the sheet Tabelle1 and set the index to None
Token_VO8sQR78qwVLOpZ_TOZ4fw = pd.read_excel("beispiel.xlsx", sheet_name = 'Tabelle1')

#Here we try to evaluate the Expression Kostenstelle = "unknown" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_VO8sQR78qwVLOpZ_TOZ4fw = Token_VO8sQR78qwVLOpZ_TOZ4fw.eval('Kostenstelle = "unknown"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "unknown"', "trying next")

#Creating new Dataframe based on Token_VO8sQR78qwVLOpZ_TOZ4fw
Token_AbX0jIuQXQUpMIcAklVyOA = Token_VO8sQR78qwVLOpZ_TOZ4fw.copy(True)

#Here we try to query the Expression  Profitcenter == "P1" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_AbX0jIuQXQUpMIcAklVyOA = Token_AbX0jIuQXQUpMIcAklVyOA.query(' Profitcenter == "P1"', **engine)
    except Exception:
        print(engine, "failed to query", ' Profitcenter == "P1"', "trying next")

#Creating new Dataframe based on Token_VO8sQR78qwVLOpZ_TOZ4fw
Token_q7R9bdpGyUOGffXJ3_Z_vw = Token_VO8sQR78qwVLOpZ_TOZ4fw.copy(True)

#Here we try to query the Expression  Profitcenter == "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_q7R9bdpGyUOGffXJ3_Z_vw = Token_q7R9bdpGyUOGffXJ3_Z_vw.query(' Profitcenter == "P2"', **engine)
    except Exception:
        print(engine, "failed to query", ' Profitcenter == "P2"', "trying next")

#Creating new Dataframe based on Token_VO8sQR78qwVLOpZ_TOZ4fw
Token_pPNRlX8rmX6daJtmqHD_ZA = Token_VO8sQR78qwVLOpZ_TOZ4fw.copy(True)

#Here we try to query the Expression ~( Profitcenter == "P1") & ~( Profitcenter == "P2") with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_pPNRlX8rmX6daJtmqHD_ZA = Token_pPNRlX8rmX6daJtmqHD_ZA.query('~( Profitcenter == "P1") & ~( Profitcenter == "P2")', **engine)
    except Exception:
        print(engine, "failed to query", '~( Profitcenter == "P1") & ~( Profitcenter == "P2")', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_AbX0jIuQXQUpMIcAklVyOA = Token_AbX0jIuQXQUpMIcAklVyOA.eval('Kostenstelle = "K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K2"', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K1" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_q7R9bdpGyUOGffXJ3_Z_vw = Token_q7R9bdpGyUOGffXJ3_Z_vw.eval('Kostenstelle = "K1"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K1"', "trying next")

#Here we concate two Dataframes
Token_pPNRlX8rmX6daJtmqHD_ZA = pd.concat([Token_pPNRlX8rmX6daJtmqHD_ZA,Token_AbX0jIuQXQUpMIcAklVyOA]).drop_duplicates(keep=True)

#Here we concate two Dataframes
Token_pPNRlX8rmX6daJtmqHD_ZA = pd.concat([Token_pPNRlX8rmX6daJtmqHD_ZA,Token_q7R9bdpGyUOGffXJ3_Z_vw]).drop_duplicates(keep=True)


#here we save the data from Token_pPNRlX8rmX6daJtmqHD_ZA to the the inktest.xlsx into the  sheet Sheet1 and dont use the index
Token_pPNRlX8rmX6daJtmqHD_ZA.to_excel("inktest.xlsx", sheet_name = "Sheet1", index = False)

