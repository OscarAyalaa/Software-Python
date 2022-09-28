# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:58:20 2020

@author: HP
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\Defunciones_2018\\def18.csv")

#Perosnas muertas por H,D,M,A
h = pd.DataFrame(df)

h = h[h.EDAD > 1000]
h = h[h.EDAD < 1024]

datos = h['EDAD'].value_counts()
cont = h['EDAD'].count()
print("\nNumero de ocurrencias de personas muertas en Determinada Hora: ")
print(datos)
print("\nNumero de personas muertas registradas por hora:")
print(cont)

d = pd.DataFrame(df)

d = d[d.EDAD > 2000]
d = d[d.EDAD < 2030]

datosD = d['EDAD'].value_counts()
contD = d['EDAD'].count()
print("\nNumero de personas muertas en Determinado Dia: ")
print(datosD)
print("\nNumero de personas muertas registradas por dia: ")
print(contD)

m = pd.DataFrame(df)

m = m[m.EDAD > 3000]
m = m[m.EDAD < 3012]


datosM = m['EDAD'].value_counts()
contM = m['EDAD'].count()

print("\nNumero de personas muertas en determinado Mes: ")
print(datosM)
print("\nNumero de personas muertas registradas por mes:")
print(contM)

a = pd.DataFrame(df)


a = a[a.EDAD > 4000]
a = a[a.EDAD < 4121]

datosA = a['EDAD'].value_counts()
contA = a['EDAD'].count()
print("\nNumero de personas muertas en determinado Año: ")
print(datosA)
print("\nNumero de personas muertas registradas por año: ")
print(contA)

#indica el promedio de edad de las personas que fallecen y tienen almenos 1 año de edad

promed1 = pd.DataFrame(df)

promed1 = promed1[promed1.EDAD > 4000] 
promed1 = promed1[promed1.EDAD < 4120]

promEd = a['EDAD'].mean()
print("\nEl promedio de edad de personas fallecidas con almenos 1 año de edad es: ")
promEd = promEd - 4000
print(promEd)

#indica numero de muertes por lustro: 0 a menos 5 años, 5 años a menos de 10

lustro = pd.DataFrame(df)

inicio = 4000
final = 4006

k=0
p=5

for i in range(1,25):
    lustro = pd.DataFrame(df)
    
    lustro = lustro[lustro.EDAD > inicio]
    lustro = lustro[lustro.EDAD < final]
    
    inicio = inicio+5
    final = final+5
    
    
    muer = lustro['EDAD'].count()
    
    print("\nDe "+ str(k)+ " a "+ str(p)+" el numero de muertes es: "+ str(muer))
    k= k+5
    p= p+5
    
    
    
    
    
    

    


