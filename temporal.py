# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:51:50 2020

@author: acer
"""

import pandas as pd


df = pd.read_csv("C:\\Users\\acer\\Documents\\python\\DaosFiltrados.csv")

m = df['MONTH'].value_counts()
#d = df['DAY'].value_counts()

print(m)
#print(d)

m.to_csv("mesrep.csv")