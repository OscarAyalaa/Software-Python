# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:22:46 2020

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

#Muestra en una grafica el comportamiento del ingreso per capita para un pais en los
#años que hay datos

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\gdp.csv")

print(df)

nuevo = pd.DataFrame(df)

nuevo.set_index("Entity",inplace=True)

buscar = input("Escribe el pais del que se quiere la grafica: ")

print(nuevo.loc[''+buscar])

b = nuevo.loc[''+buscar]

b.groupby('Year')['GDP per capita, PPP (constant 2011 international $)'].sum().plot(kind='bar',legend='Reverse')
plt.xlabel('Años de '+buscar)
plt.ylabel('Ingreso per capita')



