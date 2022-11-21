'''
En esta práctica se realizarán operaciones básicas en un data frame 
aplicada a columnas apoyándonos con la librería de nummpy.  
'''
import pandas as pd
import numpy as np
'''
Carga del archivo con la informacion a procesar
'''
df = pd.read_csv('london_merged.csv')
print(df)
'''
Para mostrar tipo de dato del DataFrame:
'''
print("-"*100)
print(df.dtypes)
'''
Cambio de Tipo de Dato
'''
print("-"*100)
df['timestamp'] = pd.to_datetime(df['timestamp'])
print(df.dtypes)
'''
Para la creacion de una nueva columna en el DataFrame
'''
print("-"*100)
df['hour'] = df['timestamp'].dt.hour
df['e'] = df['timestamp'].dt.strftime("%Y%m%d")
print(df)