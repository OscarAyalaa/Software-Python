# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:52:47 2020

@author: HP
"""

import pandas as pd

#Elabora una lista deacuerdo al ingreso per capita para un año dado

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\gdp.csv")

a = pd.DataFrame(df)

buscar = int(input("Ingrese el año del que se quiere obtener los datos: "))

a = a[a.Year == buscar]

orden = a.sort_values('GDP per capita, PPP (constant 2011 international $)',ascending=False)

buscar = str(buscar)
print("\nlista del per capita de los paises deacuerdo año "+buscar)
print(orden)

orden.to_csv('PercapitaXAño.csv')
