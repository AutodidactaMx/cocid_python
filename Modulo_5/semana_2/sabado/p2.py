'''
Uso de funciones avanzadas con apply y lambda
'''
from ast import arg
import pandas as pd
import numpy as np


def fun_1(x):
    return x**2+1
    
def fun_2(x, a=1,b=2):
    return x**2 + a*x + b
    
    
##print(fun_1(10))

data = np.arange(-5,6)
##print(data.shape)
##print(fun_1(data))

df = pd.read_csv('london_merged.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df = df.iloc[:,1:]

df['hour_fun_1'] = df['hour'].apply(fun_1)
#3print(df)
##print(fun_2(10,a = 200, b=100))

df['hour_fun_2_args'] = df['hour'].apply(fun_2, args= (20,-100))
df['hour_fun_2'] = df['hour'].apply(fun_2, a=20,b=-100)
#print(df)

df['hour_fun_lambda'] = df['hour'].apply(lambda x: x + 100)
##print(df)
##print("Promedio de las columnas")
#print(df.apply(lambda x: x.mean()))
##print("desviasion standar de las columnas")
#print(df.apply(lambda x: x.std()))

##print("Promedio de las filas")
#print(df.apply(lambda x: x.mean(),axis=1))
##print("desviasion standar de las filas")
##print(df.apply(lambda x: x.std(),axis=1))

df['t1-t2_lambda_axis1'] = df.apply(lambda x: x['t1'],axis=1)
print( df['t1-t2_lambda_axis1'])


