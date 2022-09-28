# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:14:46 2020

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\tempBarcelona.csv")
Acum = 0
Año = 1780
num= 0

nuevo = df.rename(columns={'Temp_Mitjana_Gener':'Enero', 'Temp_Mitjana_Febrer' : 'Febrero',
                           'Temp_Mitjana_Marc':'Marzo','Temp_Mitjana_Abril':'Abril',
                           'Temp_Mitjana_Maig':'Mayo','Temp_Mitjana_Juny':'Junio',
                           'Temp_Mitjana_Juliol':'Julio','Temp_Mitjana_Agost':'Agosto',
                           'Temp_Mitjana_Setembre':'Septiembre','Temp_Mitjana_Octubre':'Octubre',
                           'Temp_Mitjana_Novembre':'Noviembre','Temp_Mitjana_Desembre':'Diciembre'})


nuevo['Total'] = 0
nuevo['Total'] = nuevo['Total'].astype(object)
for index , obt in nuevo.iterrows():
    temp = [obt["Any"], obt["Enero"], obt["Febrero"], obt['Marzo'], obt['Abril'],
            obt['Mayo'], obt['Junio'], obt['Julio'], obt['Agosto'], obt['Septiembre'],
            obt['Octubre'], obt['Noviembre'], obt['Diciembre']]
    
    Year = obt['Any']
    Ene = obt['Enero']
    Feb = obt['Febrero']
    Mar = obt['Marzo']
    Abr = obt['Abril']
    May = obt['Mayo']
    Jun = obt['Junio']
    Jul = obt['Julio']
    Ago = obt['Agosto']
    Sep = obt['Septiembre']
    Oct = obt['Octubre']
    Nov = obt['Noviembre']
    Dic = obt['Diciembre']
    
    if Year == Año:
        
        Acum = Acum + Ene + Feb + Mar + Abr + May + Jun + Jul + Ago + Sep + Oct + Nov + Dic
        Acum = Acum/12
        print(Acum)
        nuevo.iat[num,13]= Acum
        num = num +1
        
    Año = Año + 1
    Acum = 0


nuevo.groupby('Any')['Total'].sum().plot(kind='bar')
plt.xlabel('Año')
plt.ylabel('Total x Año')
plt.title("Temperatura Barcelona")



