import pandas as pd
import numpy as np
#to run this code u need python 3.x with these packages installed pandas, numpy, numexpr

#here we read the data provided by the beispiel.xlsx from the sheet Tabelle1 and set the index to None
Token_ieq7lbNEVRQz_UJKJKHKUw = pd.read_excel("beispiel.xlsx", sheet_name = 'Tabelle1')
Token_ieq7lbNEVRQz_UJKJKHKUw = Token_ieq7lbNEVRQz_UJKJKHKUw.replace({np.nan:None})

#Here we try to evaluate the Expression `Kostenstelle` = "CC_UNKNOWN" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_ieq7lbNEVRQz_UJKJKHKUw = Token_ieq7lbNEVRQz_UJKJKHKUw.eval('`Kostenstelle` = "CC_UNKNOWN"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Kostenstelle` = "CC_UNKNOWN"', "trying next")

#Creating new Dataframe based on Token_ieq7lbNEVRQz_UJKJKHKUw
Token_GMnttLy2gjL25N4VvNBuSA = Token_ieq7lbNEVRQz_UJKJKHKUw.copy(True)

#Here we try to query the Expression  Profitcenter == "P1" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_GMnttLy2gjL25N4VvNBuSA = Token_GMnttLy2gjL25N4VvNBuSA.query(' Profitcenter == "P1"', **engine)
    except Exception:
        print(engine, "failed to query", ' Profitcenter == "P1"', "trying next")

#Creating new Dataframe based on Token_ieq7lbNEVRQz_UJKJKHKUw
Token_ZlOA7eIielrDSxX0_HU8LQ = Token_ieq7lbNEVRQz_UJKJKHKUw.copy(True)

#Here we try to query the Expression  Profitcenter == "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_ZlOA7eIielrDSxX0_HU8LQ = Token_ZlOA7eIielrDSxX0_HU8LQ.query(' Profitcenter == "P2"', **engine)
    except Exception:
        print(engine, "failed to query", ' Profitcenter == "P2"', "trying next")

#Creating new Dataframe based on Token_ieq7lbNEVRQz_UJKJKHKUw
Token_nzUoG6VSGwtot9NfNwlTyw = Token_ieq7lbNEVRQz_UJKJKHKUw.copy(True)

#Here we try to query the Expression ~( Profitcenter == "P1") & ~( Profitcenter == "P2") with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_nzUoG6VSGwtot9NfNwlTyw = Token_nzUoG6VSGwtot9NfNwlTyw.query('~( Profitcenter == "P1") & ~( Profitcenter == "P2")', **engine)
    except Exception:
        print(engine, "failed to query", '~( Profitcenter == "P1") & ~( Profitcenter == "P2")', "trying next")

#Here we try to evaluate the Expression `Kostenstelle` = "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_GMnttLy2gjL25N4VvNBuSA = Token_GMnttLy2gjL25N4VvNBuSA.eval('`Kostenstelle` = "K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Kostenstelle` = "K2"', "trying next")

#Here we try to evaluate the Expression `Kostenstelle` = "K1" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_ZlOA7eIielrDSxX0_HU8LQ = Token_ZlOA7eIielrDSxX0_HU8LQ.eval('`Kostenstelle` = "K1"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Kostenstelle` = "K1"', "trying next")

#Here we concate two Dataframes
Token_GMnttLy2gjL25N4VvNBuSA = pd.concat([Token_GMnttLy2gjL25N4VvNBuSA,Token_ZlOA7eIielrDSxX0_HU8LQ])

#Here we concate two Dataframes
Token_GMnttLy2gjL25N4VvNBuSA = pd.concat([Token_GMnttLy2gjL25N4VvNBuSA,Token_nzUoG6VSGwtot9NfNwlTyw])


#here we save the data from Token_GMnttLy2gjL25N4VvNBuSA to the the inktest.xlsx into the  sheet Sheet1 and dont use the index
Token_GMnttLy2gjL25N4VvNBuSA.to_excel("inktest.xlsx", sheet_name = "Sheet1", index = False)

