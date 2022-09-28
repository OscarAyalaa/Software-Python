# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 00:20:40 2020

@author: HP
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
regr=linear_model.LinearRegression()


datos = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\2015.csv")

df=pd.DataFrame(datos)
#x=df['Happiness Score']
x=df['Happiness Rank']
y=df['Economy (GDP per Capita)']

X=x[:,np.newaxis]
print(X)
print(regr.fit(X,y))
print(regr.coef_)
m=regr.coef_[0]
b=regr.intercept_
y_p=m*X+b #valor que se predice
print('y={0}*x+{1}'.format(m,b))
print(regr.predict(X)[0:5])
print("el valor de r^2: ",r2_score(y,y_p))
plt.scatter(x,y,color='blue')
plt.plot(x,y_p,color='red')
plt.title('Regresion lineal', fontsize=16)
plt.xlabel('Indice de felicidad', fontsize=13)
plt.ylabel('Ingreso percapita', fontsize=13)


        
    
    
    
    
    

    