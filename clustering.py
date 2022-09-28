# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 22:32:10 2020

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


m = int(input("\n¿Cuantos puntos quiere generar?: "))
k = int(input("\n¿Cuantos grupos quiere generar?: "))

Data = np.random.randint(0, 100, size = m)
  
df = pd.DataFrame(Data, columns=['x'])
n= np.random.randint(0,100, size = m)

df['y']  = n

print(df)

plt.scatter(df['x'], df['y'])
plt.show()


kmeans = KMeans(n_clusters=k).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:,0], centroids[:,1], c='red', s = 50)


