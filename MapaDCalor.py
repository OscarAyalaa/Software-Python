# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 17:58:54 2020

@author: HP
"""

import folium
from folium.plugins import HeatMap
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt

locais = []

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\Otros\\places.csv", encoding='latin1')

#Para ver el mapa de calor abrir el archivo html que se generara donde se guarde el ejecutavle

print('El numero de id relacionados a una gasolinera es:')
print(df.place_id.count())

mapa = folium.Map(location=[19.4978, -99.1269], zoom_start=5)

"""
df1 = df.drop(['name'],axis=1)
df1 = df1.drop(['cre_id'], axis=1)


print(df1.head())

mapa = sns.heatmap(df1,cmap="flag") """

for index , linha in df.iterrows():
    temp = [linha["y"], linha["x"]]
    locais.append(temp)
    
HeatMap(locais, radius=50).add_to(mapa)

mapa.save('mapa.html')


    










