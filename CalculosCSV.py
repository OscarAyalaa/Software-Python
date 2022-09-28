# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 19:43:38 2020

@author: Oscar
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\Oscar\\Documents\\python\\ArregladoCsv.csv")
df=df.drop(['Unnamed: 0'], axis=1)
print(df)
print(list(df))
print('\n')


#solo para modificacciones sin  alterar el original por si acaso
nu = pd.DataFrame(df)
print("Promedio de extension:", nu['Extension'].mean())
print("Maximo de extension:", nu['Extension'].max())
print("Minimo de extension:", nu['Extension'].min())
print("Desviacion estandar:", nu['Extension'].std())
print('\n')
print("Promedio de habitantes:", nu['Hab2015'].mean())
print("Maximo de habitantes:", nu['Hab2015'].max())
print("Minimo de habitantes:", nu['Hab2015'].min())
print("Desviacion estandar:", nu['Hab2015'].std())





