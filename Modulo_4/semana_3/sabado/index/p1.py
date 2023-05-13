'''
Manejo de Data Frame con indices retomando que el índice nos 
permite encontrar la información de un archivo para darnos las coordenadas 
utilizando la estructura de los datos para aplicar funciones matemáticas a varios niveles
'''
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.1f}'.format
print("-"*100)
df = pd.read_csv('./index/poblacion.csv')
print(df.head(2))
print("-"*100)
print(df.dtypes)
'''
Los categóricos son un tipo de datos de pandas correspondientes a variables categóricas en estadísticas. 
Una variable categórica toma un número limitado, y generalmente fijo, de valores posibles. 
Algunos ejemplos son el sexo, la clase social, el tipo de sangre,
 el país de pertenencia, el tiempo de observación o la calificación a través de escalas de Likert.
'''
df['año'] = pd.Categorical(df['año'].apply(str))
df['pais'] = pd.Categorical(df['pais'])

print(df.head(2))

print(df.dtypes)