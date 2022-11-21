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
df['Date'].dt.strftime("%Y%m%d").astype(int)
print(df)
'''
Para filtrar datos por medio del indice
'''
print("-"*100)
df = df.iloc[:, 1:]
print(df)
'''
Para la aplicacion de operaciones simples a las columas
'''
print("-"*100)
df["wind_speed^2"] = df["wind_speed"]**2
df["wind_speed-sin"] = np.sin(df["wind_speed"])
df["diff_t"] = df["t1"] - df["t2"]
df["diff_t_row2"] = df["t1"].iloc[::3].sub(df["t2"], fill_value=100)
print(df)
