# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 15:26:38 2020

@author: Oscar
"""
import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\Oscar\\Documents\\python\\mex.csv', encoding='latin1')
df=df.dropna(how = 'all') #En caso de que un rengolo este todo vacio lo elimina

for column  in df.columns:
    df[column] = df[column].str.replace('ÿ',"")
    df[column] = df[column].str.replace(r'\W',"") #todo lo que no sea numero o letra lo remplaxa con un caracter vacio
    df[column] = df[column].str.replace('á',"a") #quitar acentos
    df[column] = df[column].str.replace('é',"e")
    df[column] = df[column].str.replace('í',"i")
    df[column] = df[column].str.replace('ó',"o")
    df[column] = df[column].str.replace('ú',"u")
df = df.replace(np.nan,"0")  # En caso de que exita un camo que tenga nan como valor
print(df)
print('\n'*2)
df.to_csv('ArregladoCsv.csv')

#
#Copiar los renglones que satisfacen un criterio a otro archivo csv
# buscara los patrones de tosdos los datos similares y extraera la informacion

nuevo = pd.DataFrame(df)
print("Escribe el criterio para extraer los datos en un archivo csv")
col = input("Sobre que columna se quiere buscar: "  )
nuevo.set_index(""+col,inplace=True)
buscar = input("Escribe el dato para buscar su informacion: ")
print("\n")
print("Buscando todos los datos relacionados con "+buscar)

print(nuevo.loc[''+buscar])
b = nuevo.loc[''+buscar]
b.to_csv('Busqueda.csv')
