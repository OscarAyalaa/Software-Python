# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 01:02:30 2020

@author: Oscar
"""

import pandas as pd
import numpy as np


df = pd.read_csv("C:\\Users\\Oscar\\Documents\\python\\sinac2019DatosAbiertos.csv")

#print(df.loc['15':,'FECH_NACH'])

#dato = df.loc[df['ENT_NACM'] == 15, ['FECH_NACH']]
#print (dato)
#datos = dato['FECH_NACH'].value_counts()
#print(datos)
#datos.to_csv("Nac_mex.csv")


colum = df.iloc[:,35:37]
print(colum)
colum.to_csv("PesoEst.csv")




pes = pd.read_csv("C:\\Users\\Oscar\\Documents\\python\\PesoEst.csv")
pes = pes.drop(['Unnamed: 0'], axis=1)


cal = pd.DataFrame(pes)

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


est = pd.DataFrame(df)
est = est[est.ENT_NACM < 33]   # se pone menor a 33 para que tome los 32 estados


datos = est['ENT_NACM'].value_counts()
print(datos)
#datos.to_csv('NacEst.csv')

sem = pd.DataFrame(df)

sem.FECH_NACH = pd.to_datetime(sem.FECH_NACH)

print(sem.FECH_NACH)

grouper = pd.Grouper(key='FECH_NACH', freq='W')
sem["FECH_NACH"] = sem.groupby(grouper).grouper.group_info[0] + 1

#print(sem["week"])
 
semanas = sem["FECH_NACH"]
print(semanas)



semanas.to_csv('SemanasMex.csv')

nuevo = pd.read_csv("C:\\Users\\Oscar\\Documents\\python\\SemanasMex.csv")
s = nuevo['FECH_NACH'].value_counts()
print(s)

s.to_csv('f.csv')
 







