# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 00:23:52 2020

@author: HP
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\Defunciones_2018\\def18.csv")

#Muerte clasificada por genero
se = pd.DataFrame(df)

datos = se['SEXO'].value_counts()

print("\nNumero de personas que fallecieron por genero, 1=Hombre,2=Mujeres y 3=No Especificado")
print(datos)

#indica cuales son las 25 principales causas de muerte en mexico y el numero de muertes de cada una

pri = pd.DataFrame(df)

causas = pri['CAUSA_DEF'].value_counts().head(26)

print("\nlas principales 25 causas de muertes con su numero total de muertes son: ")
print(causas)
print("\n Las causas relacionadas con los id son los siguientes: ")
print("I219 = Infarto agudo del miocardio sin otra especificación")
print("E116 = Diabetes mellitus no insulinodependiente, con otras complicaciones especificadas")
print("J189 = Neumonía no especificada")
print("E112 = Diabetes mellitus no insulinodependiente con complicaciones renales")
print("E117 = Diabetes mellitus no insulinodependiente con complicaciones múltiples")
print("K746 = Otras cirrosis del hígado y las no especificadas")
print("X954 = Agresión con disparo de otras armas de fuego y las no especificadas en calles y carreteras")
print("J449 = Enfermedad pulmonar obstructiva crónica no especificada")
print("K703 = Cirrosis hepática alcohólica ")
print("E146 = Diabetes mellitus no especificada con otras complicaciones especificadas")
print("J440 = Enfermedad pulmonar obstructiva crónica con infección aguda de las vías respiratorias inferiores")
print("N189 = Enfermedad renal crónica no especificada")
print("I120 = Enfermedad renal hipertensiva con insuficiencia renal")
print("I64X = Accidente vascular encefálico agudo no especificado como hemorrágico o isquémico")
print("C509 = Tumor maligno de la mama parte no especificada")
print("I110 =	Enfermedad cardíaca hipertensiva con insuficiencia cardíaca (congestiva)")
print("C349 = Tumor maligno de los bronquios o del pulmón arte no especificada")
print("I10X = Hipertensión esencial (primaria)")
print("C61X = Tumor maligno de la próstata")
print("I619 = Hemorragia intraencefálica no especificada")
print("E119 = Diabetes mellitus no insulinodependiente sin mención de complicación")
print("E142 = Diabetes mellitus no especificada con complicaciones renale")
print("N390 = Infección de vías urinarias sitio no especificado")
print("C169 = sitio no especificado parte no especificada")
print("E147 = Diabetes mellitus no especificada")
print("V892 = Persona lesionada en accidente de tránsito de vehículo de motor no especificado")

#contrasta los fallecidos 2018 contra los nacimientos 2019 por entidad

df2 = pd.read_csv("C:\\Users\\HP\\Documents\\python\\sinac2019DatosAbiertos.csv")

fall2018 = pd.DataFrame(df)

fall2018 = fall2018[fall2018.ANIO_OCUR > 2017]
fall2018 = fall2018[fall2018.ANIO_OCUR < 2019]

numf = fall2018['ANIO_OCUR'].value_counts()

print("\nNumero de fallecidos en 2018: ")
print(numf)

numn = df2['FECH_NACH'].count()

print("\nNumero de nacimientos en 2019: ")
print("2019   "+ str(numn))





