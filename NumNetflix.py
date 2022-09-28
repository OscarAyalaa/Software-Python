# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:30:26 2020

@author: HP
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\netflix_titles.csv")

a = pd.DataFrame(df)

buscar = int(input("Ingrese el año del que se quiere obtener los datos: "))

a = a[a.release_year == buscar]
dfNuevo = a[['title', 'duration']].copy()

datos = a["type"].value_counts()
print("\nEl numero total de series y peliculas en el año "+str(buscar)+" es:")
print(datos)
print("\n")
print("El numero de temporadas y de minutos de las peliculas son :")
print(dfNuevo)
