# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:23:00 2020

@author: HP
"""

import pandas as pd


df = pd.read_csv("C:\\Users\\HP\\Documents\\python\\Archivos\\Golf.csv")

print(df)

AcumN = 0
AcumY = 0
ClimN = 0
ClimY = 0
TempN = 0
TempY = 0
HumN = 0
HumY = 0
WinY = 0
WinN = 0

fdat = df.shape[0]
                                       #Tuve que cambiar False por Falsee y True por truee ya que lo tomaba en cuenta
print("Probabilidad de jugar Golf")
print("\n Ingrese posteriormente los datos a evaluar Ejemplo: Rainy, Hot, Normal y Falsee")
n = 4

x = []

for i in range(n):
    dato = input("Ingresa el nombre del dato "+str(i+1)+": ")
    x.append(dato) 
    
for index , obt in df.iterrows():
    temp = [obt["OUTLOOK"], obt["TEMPERATURE"],obt["HUMIDITY"], obt["WINDY"], obt['PLAY GOLF']]
    
    clim = obt['OUTLOOK']
    temp = obt['TEMPERATURE']
    hum = obt['HUMIDITY']
    win = obt['WINDY']
    play = obt['PLAY GOLF']
    
    if(play == "No"):
        AcumN = AcumN+1
    else:
        AcumY = AcumY+1
    
    if(clim == x[0] and play == "No"):
        ClimN = ClimN+1
        
    elif(clim == x[0] and play == "Yes"):
        ClimY = ClimY+1
    
    if(temp == x[1] and play == "No"):
        TempN = TempN+1
        
    elif(temp == x[1] and play == "Yes"):
        TempY = TempY+1
    
    if(hum == x[2] and play == "No"):
        HumN = HumN+1
        
    elif(hum == x[2] and play == "Yes"):
        HumY = HumY+1
    
    if(win == x[3] and play == "No"):
        WinN = WinN+1
        
    elif(win == x[3] and play == "Yes"):
        WinY = WinY+1

ProY = (AcumY/fdat)*(ClimY/AcumY)*(TempY/AcumY)*(HumY/AcumY)*(WinY/AcumY)
ProN = (AcumN/fdat)*(ClimN/AcumN)*(TempN/AcumN)*(HumN/AcumN)*(WinN/AcumN)

SumP = ProY+ProN

jugarY = ProY/SumP
jugarN = ProN/SumP

print("\nLa probabilida de hugar Golf con los Datos: "+x[0]+", "+x[1]+", "+x[2]+", "+x[3])
print("\nLa probabilidad de Si jugar es de :"+str(jugarY))
print("\nLa probabilidad de No jugar es de :"+str(jugarN))
    


        
        
        
        


        
        
    
    

