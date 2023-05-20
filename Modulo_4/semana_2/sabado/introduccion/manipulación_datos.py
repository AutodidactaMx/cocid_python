#Manipulación de datos en Pandas:
import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Carlos', 'Luis'],
        'Edad': [25, 31, 18, 42],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}
df = pd.DataFrame(data)
# Seleccionar una columna específica del DataFrame
columna = df['Nombre']
print(columna)

# Filtrar el DataFrame según una condición
filtro = df[df['Edad'] > 30]
print(filtro)

# Agregar una nueva columna al DataFrame
df['Genero'] = ['M', 'F', 'M', 'M']
print(df)

# Eliminar una columna del DataFrame
df = df.drop('Ciudad', axis=1)
print(df)
