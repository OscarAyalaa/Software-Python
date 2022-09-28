# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 00:25:10 2020

@author: Oscar
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\flights.csv")

df.set_index("ORIGIN_AIRPORT", inplace = True)

datos = df.loc['LAX']

#print(datos)

datos.to_csv("DatosSoloUno.csv")

v = pd.read_csv("C:\\Users\\HP\\Documents\\python\\DatosSoloUno.csv")

v.set_index("ORIGIN_AIRPORT", inplace = True)

cal = pd.DataFrame(v)

cal = cal.replace(np.nan,"0")

cal1 = cal.loc[df['DEPARTURE_DELAY'] >3, ['DAY']]
cal1 = cal1.loc[df['DEPARTURE_DELAY'] <121, ['DAY']]
cal2 = cal.loc[df['DEPARTURE_DELAY'] >3, ['MONTH']]
cal2 = cal2.loc[df['DEPARTURE_DELAY'] <121, ['MONRH']]

m = cal2['MONTH'].value_counts()
d = cal1['DAY'].value_counts()

print(m)
print(d)




