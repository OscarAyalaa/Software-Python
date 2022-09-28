# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:24:54 2020

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\Casos_covid.csv")

nuevo = pd.DataFrame(df)

nuevo = nuevo.drop(['Lat','Long','Province/State'], axis=1)
nuevo = nuevo.replace(np.nan,"0")


nuevo.set_index("Country/Region",inplace=True)

print("\nDatos de contagios de VOVID, por fecha de oleada")
buscar = input("\nIntroduce el nombre del pais: ")

b = nuevo.loc[''+buscar]

print(b)

b.to_csv('Covid_pais.csv')

pais = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Covid_pais.csv")

pais2 = pais.rename(columns={'Unnamed: 0':'fecha', ''+buscar : 'Num'})

print("\nEhemplo de como introducir feccha M/DD/AA -> 1/22/20")
ola1 = input("\nIntroduce fecha de la primera oleada: ")
ola2 = input("\nIntroduce fecha de la segunda oleada: ")

h = pais2[(pais2['fecha'] >= ''+ola1) & (pais2['fecha'] <= ''+ola2)]

print(h)

h.groupby('fecha')['Num'].sum().plot(kind='bar')
plt.xlabel('fecha')
plt.ylabel('Numero de Casos')
plt.title("Casos de covid")












