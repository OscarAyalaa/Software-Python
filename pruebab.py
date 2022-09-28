# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 00:50:03 2020

@author: HP
"""

import pandas as pd
from math import acos, cos, sin, radians
#from math import sqrt

"""
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

def calcular_distancia(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

punto1 = Punto(19.4978, -99.1269)
punto2 = Punto(23.6345, 23.6345)

print(calcular_distancia(punto1, punto2))"""


""" latitud longitud distancia
def distancia_puntos(punto_1, punto_2):
    punto_1 = (radians(punto_1[0]), radians(punto_1[1]))
    punto_2 = (radians(punto_2[0]), radians(punto_2[1]))

    distancia = acos(sin(punto_1[0])*sin(punto_2[0]) + cos(punto_1[0])*cos(punto_2[0])*cos(punto_1[1] - punto_2[1]))

    return distancia * 6371.01


if __name__ == "__main__":
    punto_1 = (19.4978, -99.1269)
    punto_2 = (23.6345, -103.64)

    resultado = distancia_puntos(punto_1, punto_2)

    print(resultado) """
    
pri = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\Otros\\prices.csv")

#print(pri.head())

""" busqueda ne 
clave = 11703

pri = pd.DataFrame(pri[(pri['place_id'] == clave)])

pri = pri.drop(['place_id'],axis=1)

print(pri)  """



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
        
        print(' '+n+' Su distancia  es de %f Km'%resultado)
        

    
    
    #print(n)




    
    

    
        