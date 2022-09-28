# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 02:22:10 2020

@author: HP
"""



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\latlong.csv")

k= int(input("Ingrese el numero de grupos: "))
plt.figure(figsize=(10,6))
plt.scatter(df['y'], df['x'])
plt.show()


kmeans = KMeans(n_clusters=k).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(df['y'], df['x'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:,0], centroids[:,1], c='red', s = 50)


