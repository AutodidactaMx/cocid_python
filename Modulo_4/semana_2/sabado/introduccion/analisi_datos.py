# Análisis de datos en Pandas:
import pandas as pd

data = {'Nombre': ['Juan', 'María', 'Carlos', 'Luis'],
        'Edad': [25, 31, 18, 42],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}
df = pd.DataFrame(data)

# Obtener estadísticas resumidas del DataFrame
estadisticas = df.describe()
print(estadisticas)

# Agrupar los datos por una columna y calcular la media de otra columna
agrupado = df.groupby('Ciudad')['Edad'].mean()
print(agrupado)

# Crear un gráfico de barras a partir de los datos
df.plot(x='Nombre', y='Edad', kind='bar')