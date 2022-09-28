import pandas as pd

cancer_mama = pd.read_excel("C:\\Users\\Oscar\\Documents\\python\\breast_cancer.xlsx")
titanic = pd.read_csv("C:\\Users\\Oscar\\Documents\\python\\titanic.csv")
wine = pd.read_csv("C:\\Users\\Oscar\\Documents\\python\\red_wine.csv", sep=";")
cov = pd.read_csv("C:\\Users\\Oscar\\Documents\\python\\covid_20200430.csv")

a = cov.info()
print(a)
s = wine.describe()
print(s)
