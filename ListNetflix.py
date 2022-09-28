# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:18:29 2020

@author: HP
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\netflix_titles.csv")

#print(df.head())

nuevo = pd.DataFrame(df)


nuevo.set_index("country",inplace=True)


print("Escribir el nombre del pais que se quiere conocer las listas con los datos")
buscar = input("si se quiere mas de un pais agregar ua ',' despues de cada pais:\n ")

b = nuevo.loc[''+buscar]


producciones = b["title"]  #Producciones por pais
directores = b["director"] #directores por pais
actrises = b["cast"]  #actrices por pais

numpro = producciones.count()

print("\nLista de producciones de "+buscar+ " con un total de "+str(numpro)+" registros\n")
print(producciones)
print("\n")
print("Lista de directores")
print(directores)
print("\n")
print("Lista de actices")
print(actrises)






