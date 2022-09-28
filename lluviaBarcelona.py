# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:05:17 2020

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\lluviaBarcelona.csv")
Acum = 0
Año = 1786
num= 0

nuevo = df.rename(columns={'Precip_Acum_Gener':'Enero', 'Precip_Acum_Febrer' : 'Febrero',
                           'Precip_Acum_Marc':'Marzo','Precip_Acum_Abril':'Abril',
                           'Precip_Acum_Maig':'Mayo','Precip_Acum_Juny':'Junio',
                           'Precip_Acum_Juliol':'Julio','Precip_Acum_Agost':'Agosto',
                           'Precip_Acum_Setembre':'Septiembre','Precip_Acum_Octubre':'Octubre',
                           'Precip_Acum_Novembre':'Noviembre','Precip_Acum_Desembre':'Diciembre'})


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
        print(Acum)
        nuevo.iat[num,13]= Acum
        num = num +1
        
    Año = Año + 1
    Acum = 0


nuevo.groupby('Any')['Total'].sum().plot(kind='bar')
plt.xlabel('Año')
plt.ylabel('Total x Año')
plt.title("LLuvia Barcelona")



"""df = df.drop(['Any'], axis=1)
df.loc[:,'Total x Año']= df.sum(axis=1)
print(df)"""
    
    





""""
a = pd.DataFrame(df)
print(df)

#df.groupby('any')['Num'].sum().plot(kind='bar')

buscar = 1786

a = a[a.Any == buscar]

print(a)

 """
    
    

        
