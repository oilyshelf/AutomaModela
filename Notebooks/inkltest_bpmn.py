import pandas as pd
import numpy as np
#to run this code u need python 3.x with these packages installed pandas, numpy, numexpr

#here we read the data provided by the beispiel.xlsx from the sheet Tabelle1 and set the index to None
Token_fus_1Y8fARH3RHy09ihsXA = pd.read_excel("beispiel.xlsx", sheet_name = 'Tabelle1')

#Here we try to evaluate the Expression Kostenstelle = "unknown" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_fus_1Y8fARH3RHy09ihsXA = Token_fus_1Y8fARH3RHy09ihsXA.eval('Kostenstelle = "unknown"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "unknown"', "trying next")

#Creating new Dataframe based on Token_fus_1Y8fARH3RHy09ihsXA
Token_9Q3svPWZmhCzfH4OwWMPEw = Token_fus_1Y8fARH3RHy09ihsXA.copy(True)

#Here we try to query the Expression Profitcenter == "P1" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_9Q3svPWZmhCzfH4OwWMPEw = Token_9Q3svPWZmhCzfH4OwWMPEw.query('Profitcenter == "P1"', **engine)
    except Exception:
        print(engine, "failed to query", 'Profitcenter == "P1"', "trying next")

#Creating new Dataframe based on Token_fus_1Y8fARH3RHy09ihsXA
Token_zYchfRj78Yj1GOnTtn0tIA = Token_fus_1Y8fARH3RHy09ihsXA.copy(True)

#Here we try to query the Expression Profitcenter == "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_zYchfRj78Yj1GOnTtn0tIA = Token_zYchfRj78Yj1GOnTtn0tIA.query('Profitcenter == "P2"', **engine)
    except Exception:
        print(engine, "failed to query", 'Profitcenter == "P2"', "trying next")

#Creating new Dataframe based on Token_fus_1Y8fARH3RHy09ihsXA
Token_vBu912o4OI4zQhWoDmj75g = Token_fus_1Y8fARH3RHy09ihsXA.copy(True)

#Here we try to query the Expression ~(Profitcenter == "P1") & ~(Profitcenter == "P2") with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_vBu912o4OI4zQhWoDmj75g = Token_vBu912o4OI4zQhWoDmj75g.query('~(Profitcenter == "P1") & ~(Profitcenter == "P2")', **engine)
    except Exception:
        print(engine, "failed to query", '~(Profitcenter == "P1") & ~(Profitcenter == "P2")', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_9Q3svPWZmhCzfH4OwWMPEw = Token_9Q3svPWZmhCzfH4OwWMPEw.eval('Kostenstelle = "K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K2"', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K1" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_zYchfRj78Yj1GOnTtn0tIA = Token_zYchfRj78Yj1GOnTtn0tIA.eval('Kostenstelle = "K1"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K1"', "trying next")

#Here we concate two Dataframes
Token_vBu912o4OI4zQhWoDmj75g = pd.concat([Token_vBu912o4OI4zQhWoDmj75g,Token_9Q3svPWZmhCzfH4OwWMPEw]).drop_duplicates(keep=True)

#Here we concate two Dataframes
Token_vBu912o4OI4zQhWoDmj75g = pd.concat([Token_vBu912o4OI4zQhWoDmj75g,Token_zYchfRj78Yj1GOnTtn0tIA]).drop_duplicates(keep=True)

#Here we try to evaluate the Expression Demo = "läuft gut" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_vBu912o4OI4zQhWoDmj75g = Token_vBu912o4OI4zQhWoDmj75g.eval('Demo = "läuft gut"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Demo = "läuft gut"', "trying next")


#here we save the data from Token_vBu912o4OI4zQhWoDmj75g to the the inktest.xlsx into the  sheet Sheet1 and dont use the index
Token_vBu912o4OI4zQhWoDmj75g.to_excel("inktest.xlsx", sheet_name = "Sheet1", index = False)

