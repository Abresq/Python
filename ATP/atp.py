# encoding: utf-8

import pandas as pd
datos = pd.read_csv('atp_data.csv')
print (datos.info())  #Esto saca informacion del data set

print(datos.iloc[0:5]) #Esto imprime las primeras cinco FILAS
print(datos.iloc[:,0:2]) #Esto imprime las primeras 2 COLUMNAS
print(datos.iloc[[0,1,2,3,4],[1,2,3,9]])
