import pandas as pd
import numpy as np
#to run this code u need python 3.x with these packages installed pandas, numpy, numexpr

#here we read the data provided by the beispiel.xlsx from the sheet Tabelle1 and set the index to None
Token_KuPVLm14k_ytHoxfapD27A = pd.read_excel("beispiel.xlsx", sheet_name = 'Tabelle1')

#Here we try to evaluate the Expression Kostenstelle = "unknown" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_KuPVLm14k_ytHoxfapD27A = Token_KuPVLm14k_ytHoxfapD27A.eval('Kostenstelle = "unknown"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "unknown"', "trying next")

#Creating new Dataframe based on Token_KuPVLm14k_ytHoxfapD27A
Token_vjluOJwPVwjQM8G_OegF_w = Token_KuPVLm14k_ytHoxfapD27A.copy(True)

#Here we try to query the Expression Profitcenter == "P1" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_vjluOJwPVwjQM8G_OegF_w = Token_vjluOJwPVwjQM8G_OegF_w.query('Profitcenter == "P1"', **engine)
    except Exception:
        print(engine, "failed to query", 'Profitcenter == "P1"', "trying next")

#Creating new Dataframe based on Token_KuPVLm14k_ytHoxfapD27A
Token_LydPKuhaHg6VGJI09Hy_pw = Token_KuPVLm14k_ytHoxfapD27A.copy(True)

#Here we try to query the Expression Profitcenter == "P2" with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_LydPKuhaHg6VGJI09Hy_pw = Token_LydPKuhaHg6VGJI09Hy_pw.query('Profitcenter == "P2"', **engine)
    except Exception:
        print(engine, "failed to query", 'Profitcenter == "P2"', "trying next")

#Creating new Dataframe based on Token_KuPVLm14k_ytHoxfapD27A
Token_hgyulBaIApjsQZyA8qQ0yQ = Token_KuPVLm14k_ytHoxfapD27A.copy(True)

#Here we try to query the Expression ~(Profitcenter == "P1") & ~(Profitcenter == "P2") with diffrent engines
for engine in [{'engine': 'numexpr'}, {'engine': 'python'}]:
    try:
        Token_hgyulBaIApjsQZyA8qQ0yQ = Token_hgyulBaIApjsQZyA8qQ0yQ.query('~(Profitcenter == "P1") & ~(Profitcenter == "P2")', **engine)
    except Exception:
        print(engine, "failed to query", '~(Profitcenter == "P1") & ~(Profitcenter == "P2")', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K2" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_vjluOJwPVwjQM8G_OegF_w = Token_vjluOJwPVwjQM8G_OegF_w.eval('Kostenstelle = "K2"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K2"', "trying next")

#Here we try to evaluate the Expression Kostenstelle = "K1" with diffrent engines
for engine in [{}, {'engine': 'python'}]:
    try:
        Token_LydPKuhaHg6VGJI09Hy_pw = Token_LydPKuhaHg6VGJI09Hy_pw.eval('Kostenstelle = "K1"', **engine)
    except Exception:
        print(engine, "failed to evaluate", 'Kostenstelle = "K1"', "trying next")

#Here we concate two Dataframes
Token_hgyulBaIApjsQZyA8qQ0yQ = pd.concat([Token_hgyulBaIApjsQZyA8qQ0yQ,Token_vjluOJwPVwjQM8G_OegF_w])

#Here we concate two Dataframes
Token_hgyulBaIApjsQZyA8qQ0yQ = pd.concat([Token_hgyulBaIApjsQZyA8qQ0yQ,Token_LydPKuhaHg6VGJI09Hy_pw])


#here we save the data from Token_hgyulBaIApjsQZyA8qQ0yQ to the the inktest.xlsx into the  sheet Sheet1 and dont use the index
Token_hgyulBaIApjsQZyA8qQ0yQ.to_excel("inktest.xlsx", sheet_name = "Sheet1", index = False)

