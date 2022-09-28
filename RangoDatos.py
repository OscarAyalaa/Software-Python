# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 08:10:22 2020

@author: Oscar
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\Oscar\\Documents\\python\\Archivos\\flights.csv")

print("\n")
print("Selecciona el rango de datos que quieres obtener")
m = int(input("Cual es el valor de rango inicial: "))
n = int(input("Cual es el valor del rango final: "))
n = n+1
d = df.iloc[m:n]
print(df.iloc[m:n])
d.to_csv("RangoDatos.csv")


#En caso de querer tener un rango de  columnas
#colum = df.iloc[:,35:37]
#print(colum)
#colum.to_csv("colRan.csv")

