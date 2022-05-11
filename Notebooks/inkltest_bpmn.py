import pandas as pd
import numpy as np
#to run this code u need python 3.x with these packages installed pandas, numpy, numexpr

#here we read the data provided by the beispiel.xlsx from the sheet Tabelle1 and set the index to None
Token_NaE4u6NXgxuan8wEwR6cdg = pd.read_excel("beispiel.xlsx", sheet_name = 'Tabelle1')
Token_NaE4u6NXgxuan8wEwR6cdg = Token_NaE4u6NXgxuan8wEwR6cdg.replace({np.nan:None})

#Here we try to evaluate the Expression `Kostenstelle` = "CC_UNKNOWN" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_NaE4u6NXgxuan8wEwR6cdg = Token_NaE4u6NXgxuan8wEwR6cdg.eval('`Kostenstelle` = "CC_UNKNOWN"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Kostenstelle` = "CC_UNKNOWN"', "trying next")

#Creating new Dataframe based on Token_NaE4u6NXgxuan8wEwR6cdg
Token_Rm_4azwFfcYneBjtborVZw = Token_NaE4u6NXgxuan8wEwR6cdg.copy(True)

#Here we try to query the Expression  Profitcenter == "P1" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_Rm_4azwFfcYneBjtborVZw = Token_Rm_4azwFfcYneBjtborVZw.query(' Profitcenter == "P1"', **engine)
    except Exception:
        print(engine, "failed to query", ' Profitcenter == "P1"', "trying next")

#Creating new Dataframe based on Token_NaE4u6NXgxuan8wEwR6cdg
Token_0fZkkubQ3qnL7fmX7xKgFA = Token_NaE4u6NXgxuan8wEwR6cdg.copy(True)

#Here we try to query the Expression  Profitcenter == "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_0fZkkubQ3qnL7fmX7xKgFA = Token_0fZkkubQ3qnL7fmX7xKgFA.query(' Profitcenter == "P2"', **engine)
    except Exception:
        print(engine, "failed to query", ' Profitcenter == "P2"', "trying next")

#Creating new Dataframe based on Token_NaE4u6NXgxuan8wEwR6cdg
Token_74OXcIk7Y9p5XFDr9f0NTw = Token_NaE4u6NXgxuan8wEwR6cdg.copy(True)

#Here we try to query the Expression ~( Profitcenter == "P1") & ~( Profitcenter == "P2") with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_74OXcIk7Y9p5XFDr9f0NTw = Token_74OXcIk7Y9p5XFDr9f0NTw.query('~( Profitcenter == "P1") & ~( Profitcenter == "P2")', **engine)
    except Exception:
        print(engine, "failed to query", '~( Profitcenter == "P1") & ~( Profitcenter == "P2")', "trying next")

#Here we try to evaluate the Expression `Kostenstelle` = "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_Rm_4azwFfcYneBjtborVZw = Token_Rm_4azwFfcYneBjtborVZw.eval('`Kostenstelle` = "K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Kostenstelle` = "K2"', "trying next")

#Here we try to evaluate the Expression `Kostenstelle` = "K1" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_0fZkkubQ3qnL7fmX7xKgFA = Token_0fZkkubQ3qnL7fmX7xKgFA.eval('`Kostenstelle` = "K1"', **engine)
    except Exception:
        print(engine, "failed to evaluate", '`Kostenstelle` = "K1"', "trying next")

#Here we concate two Dataframes
Token_Rm_4azwFfcYneBjtborVZw = pd.concat([Token_Rm_4azwFfcYneBjtborVZw,Token_0fZkkubQ3qnL7fmX7xKgFA])

#Here we concate two Dataframes
Token_Rm_4azwFfcYneBjtborVZw = pd.concat([Token_Rm_4azwFfcYneBjtborVZw,Token_74OXcIk7Y9p5XFDr9f0NTw])


#here we save the data from Token_Rm_4azwFfcYneBjtborVZw to the the inktest.xlsx into the  sheet Sheet1 and dont use the index
Token_Rm_4azwFfcYneBjtborVZw.to_excel("inktest.xlsx", sheet_name = "Sheet1", index = False)

