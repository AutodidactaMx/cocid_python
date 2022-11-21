'''
Uso de funciones avanzadas con apply y lambda 
aplicadas a las columnas de data frame
'''
from ast import arg
import pandas as pd
import numpy as np

'''
Creacion de funcion que se ocupara en el DataFrame
'''
def fun_1(x):
    return x**2+1
'''
Generacion de datos por medio de numpy
'''
print("-"*100)
data = np.arange(-5, 6)
print("-"*100)
print(data.shape)
'''
Carga del archivo con la informacion a procesar
'''
df = pd.read_csv('london_merged.csv')
'''
Peparacion de columna hour en el data frame y 
la manipulacion para retirar columna timestamp
'''
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df = df.iloc[:, 1:]
'''
Aplicacion de la funcion en un dataframe por 
medio de la funcion apply
'''
print("-"*100)
df['hour_fun_1'] = df['hour'].apply(fun_1)
print(df)
'''
Creacion la nueva funcion para permitir 
parametros adicionales DataFrame
'''
print("-"*100)
def fun_2(x, a=1, b=2):
    return x**2 + a*x + b
'''
Se ejecutan de funcion nueva al DataFrame
'''
print("-"*100)
df['hour_fun_2_args'] = df['hour'].apply(fun_2, args=(20, -100))
df['hour_fun_2'] = df['hour'].apply(fun_2, a=20, b=-100)
print(df)
'''
Se ejecuta un proceso por medio de una
alternativa a la función usando lambda
'''
print("-"*100)
df['hour_fun_lambda'] = df['hour'].apply(lambda x: x + 100)
print(df)
'''
Creacion de nuevas columnas  apartir 
de funciones proporcionadas por la libreria de pandas
'''
print("-"*100)
print("Promedio de las columnas")
print(df.apply(lambda x: x.mean(),axis=0))
print("-"*100)
print("desviasion standar de las columnas")
print(df.apply(lambda x: x.std()))
print("-"*100)
print("Promedio de las filas")
print(df.apply(lambda x: x.mean(),axis=1))
print("desviasion standar de las filas")
print(df.apply(lambda x: x.std(),axis=1))
print("-"*100)
df['t1-t2_lambda_axis1'] = df.apply(lambda x: x['t1'], axis=1)
print(df['t1-t2_lambda_axis1'])

### df = df.loc[0:100,['hum','wind_speed']]