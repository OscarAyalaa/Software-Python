# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 22:14:20 2020

@author: Oscar
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\Oscar\\Documents\\python\\PesoEst.csv")
df=df.drop(['Unnamed: 0'], axis=1)
print(df)

cal = pd.DataFrame(df)

cal = cal.replace(np.nan,"0")

cal = cal[cal.TALLAH < 55]  #la estatura normal de un recien nacido es 45 y 55
cal = cal[cal.TALLAH > 45]

cal = cal[cal.PESOH < 4300] #el peso normal de un recien nacido va de 2400 y 4300
cal = cal[cal.PESOH > 2400]


print("Promedio de la estatura: ", cal['TALLAH'].mean())
print("Maximo de la estatura: ", cal['TALLAH'].max())
print("Minimo de la estatura: ", cal['TALLAH'].min())
print("Desviacion estandar de la estatura: ", cal['TALLAH'].std())
print("\n")
print("Promedio del peso: ", cal['PESOH'].mean())
print("Maximo del peso: ", cal['PESOH'].max())
print("Minimo del peso: ", cal['PESOH'].min())
print("Desviacion estandar del peso: ", cal['PESOH'].std())