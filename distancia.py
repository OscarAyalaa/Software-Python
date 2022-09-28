# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 00:37:53 2020

@author: HP
"""

import pandas as pd
from math import acos, cos, sin, radians

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\Otros\\places.csv", encoding='latin1')
pri = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\Otros\\prices.csv")

#print(df.head())

print("Ingrese Una distancia maxima y una posicion dada en Latitud y Longitud ")
lat= float(input("Ingrese la latitud: "))
lon= float(input("Ingrese la longitud: "))
d= float(input("Ingrese la distancia maxima en km: "))



def distancia_puntos(punto_1, punto_2):
    punto_1 = (radians(punto_1[0]), radians(punto_1[1]))
    punto_2 = (radians(punto_2[0]), radians(punto_2[1]))

    distancia = acos(sin(punto_1[0])*sin(punto_2[0]) + cos(punto_1[0])*cos(punto_2[0])*cos(punto_1[1] - punto_2[1]))

    return distancia * 6371.01



print("\nLas gasolineras que se encuentran dentro de la distancia ingresada son: ")

for index , linha in df.iterrows():
    temp = [linha["x"], linha["y"], linha["name"], linha['place_id']]
    x = linha['x']
    y = linha['y']
    n = linha['name']
    p_id = linha['place_id']
    
    
    punto_1 = (lat, lon)
    punto_2 = (y, x)

    resultado = distancia_puntos(punto_1, punto_2)
    
    if resultado <= d:
        precio = pd.DataFrame(pri[(pri['place_id'] == p_id)])
        precio = precio.drop(['place_id'],axis=1)
        
        print("\n")
        print(' '+n+' Su distancia  es de %f Km'%resultado)
        print("El precio de la gasolina es:")
        print(precio)

    
    
    #print(n)