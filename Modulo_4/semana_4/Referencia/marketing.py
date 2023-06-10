'''
Supongamos que tienes un conjunto de datos que contiene 
información sobre el rendimiento de una campaña de marketing 
en diferentes canales. El conjunto de datos tiene las siguientes 
columnas: "Fecha", "Canal", "Impresiones", "Clics", "Conversiones".'''

import pandas as pd

# Crear un DataFrame con el conjunto de datos
data = {
    'Fecha': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
    'Canal': ['Email', 'Redes Sociales', 'Búsqueda', 'Anuncios', 'Directo'],
    'Impresiones': [1000, 2000, 1500, 3000, 500],
    'Clics': [100, 150, 120, 200, 50],
    'Conversiones': [10, 12, 8, 15, 5]
}

df = pd.DataFrame(data)

# Imprimir el DataFrame
print(df)

'''
Ahora, supongamos que deseas calcular algunas 
métricas clave para analizar el rendimiento 
de la campaña de marketing.
Para empezar, puedes calcular la tasa de clics 
(CTR, por sus siglas en inglés) y la tasa de conversión 
para cada canal. Puedes hacerlo mediante el 
cálculo de nuevas columnas en el DataFrame:
'''

# Calcular la tasa de clics (CTR) para cada canal
df['CTR'] = (df['Clics'] / df['Impresiones']) * 100

# Calcular la tasa de conversión para cada canal
df['Tasa de Conversión'] = (df['Conversiones'] / df['Clics']) * 100

# Imprimir el DataFrame actualizado
print(df)
