# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 01:01:45 2020

@author: Oscar
"""

import pandas as pd



df = pd.read_csv("C:\\Users\\Oscar\\Documents\\python\\sinac2019DatosAbiertos.csv")

print("\nlos sigientes datos son los nombres de las columnas: ")
print("\n")
print(list(df))
df = df[df.ENT_NACM < 33]
print("\n")
col = input("Introducir el nombre de la columna para ver las ocurrencias de cada dato: ")
datos = df[col].value_counts()
print(datos)


 

datos.to_csv('Ocurrencias.csv')