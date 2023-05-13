import pandas as pd
# importing numpy as np
import numpy as np
 
# Lista
dict = {'Primero Puntaje':[100, 90, np.nan, 95],
        'Sgundo Puntaje': [30, np.nan, 45, 56],
        'Tercero Puntaje':[52, 40, 80, 98],
        'Cuarto Puntaje':[np.nan, np.nan, np.nan, 65]}
 
# Creando un marco de datos desde el diccionario
df = pd.DataFrame(dict)

print(df.dropna())
