# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:05:56 2020

@author: HP
"""

import pandas as pd


df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\suicidio.csv")


#suicidios por año
a = df['year'].value_counts()
print('\n')
print('\nLos datos por año son:')
print(a)


df.groupby('year')['year'].count().plot(kind='bar') #Muestra grafica de años


#Suicidio por rango de edades

e = df['generation'].value_counts()
print('\n')
print('\nLos datos por rango de edades son:')
print(e)
e.to_csv('EdadRango.csv')

edad = pd.read_csv("C:\\Users\\HP\\Documents\\python\\EdadRango.csv")

edad.groupby('generation')['generation'].count().plot(kind='bar') #Muestra Grafica de rango de edades



#suicidios por pais
pais = df['country'].value_counts()

pais.to_csv('pais.csv')
print('\n')
print("Los datos por paises son:")
print(pais)

p = pd.read_csv("C:\\Users\\HP\\Documents\\python\\pais.csv")


p.groupby('country')['country'].count().plot(kind='bar') #Muestra grafica de paises



#en caso de que no se muestren todas a la vez comentar dos y de muestra grafica para ver la grafica deseada









