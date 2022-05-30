'''
Realizar operaciones matematicas en df
realizar operaciones en la misma columna de df usando las libreria de np
'''
import pandas as pd
import numpy as np
'''Carga dela rchivo'''
df = pd.read_csv('london_merged.csv')
print("-"*100)
print(df)
print("-"*100)
print(df.dtypes)
print("-"*100)
'''Cambio de tipo de dato'''
df['timestamp'] = pd.to_datetime(df['timestamp'])
print(df.dtypes)
df['hour'] = df['timestamp'].dt.hour
print("-"*100)
print(df)
print("-"*100)
df = df.iloc[:,1:]
print(df)
print("-"*100)
df["wind_speed^2"]=df["wind_speed"]**2
df["wind_speed-sin"]=np.sin(df["wind_speed"])
df["diff_t"] = df["t1"] - df["t2"]
df["diff_t_row2"] = df["t1"].iloc[::3].sub(df["t2"],fill_value = 100)
print(df)

