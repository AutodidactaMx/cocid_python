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
print(df)
'''
Para filtrar datos por medio del indice
La función iloc en Pandas se utiliza para la indexación basada en la posición entera de las filas y columnas en un DataFrame. Permite acceder y extraer datos utilizando índices numéricos en lugar de etiquetas o nombres.
data.iloc[filas, columnas]
'''
print("-"*100)
df = df.iloc[:, 1:]  # Accede a la 2 columna en adelate con todas las filas
print(df)
'''
Para la aplicacion de operaciones simples a las columas
'''
print("-"*100)
df["wind_speed^2"] = df["wind_speed"]**2 #  ** se utiliza para realizar la operación de exponenciación
df["wind_speed-sin"] = np.sin(df["wind_speed"])
df["diff_t"] = df["t1"] - df["t2"]
# df["t1"].iloc[::3] Selecciona cada tercer elemento de la columna "t1"
# Se realiza la operación de sustracción entre los elementos 
# seleccionados de la columna "t1" (cada tercer elemento) y la columna "t2".
#  La función sub realiza la resta y el argumento fill_value=100 establece un valor predeterminado de 100 para rellenar cualquier valor faltante o NaN en la operación de resta.
df["diff_t_row2"] = df["t1"].iloc[::3].sub(df["t2"], fill_value=100) 
print(df)
