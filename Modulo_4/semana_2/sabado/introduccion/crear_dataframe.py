#Crear un DataFrame en Pandas:
import pandas as pd
import numpy as np

# Crear un DataFrame a partir de un diccionario de listas
data = {'Nombre': ['Juan', 'María', 'Carlos', 'Luis'],
        'Edad': [25, 31, 18, 42],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}
df = pd.DataFrame(data)
print(df)