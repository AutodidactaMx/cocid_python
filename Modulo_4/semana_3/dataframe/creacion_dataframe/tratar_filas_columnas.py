# Import pandas package
import pandas as pd

# Definir un diccionario que contenga datos de empleados
data = {'Nombre': ['Jesus', 'Pedro', 'Rodrigo', 'Jorge'],
        'Edad': [27, 24, 22, 32],
        'Direccion': ['Morelos', 'Acapulco', 'Cancun', 'Ciudad de mexico']
        }

# Convertir el diccionario en DataFrame
df = pd.DataFrame(data)

# seleccionar dos columnas
print(df[['Nombre', 'Direccion']])
