'''
Pandas cuenta con una gran funcionalidad a la hora de interactuar con texto, 
es super versatil si estas interesado en crear modelos de análisis de lenguaje natural.
Comencemos cargando nuestra librería y creando un diccionario con nombres de personas.
'''
import pandas as pd
import numpy as np

data = {'names':['Sara Moreno 34',
                 'jUAn GOMez 23',
                 'CArlos mArtinez 89',
                 'Alfredo VelaZques 3',
                 'luis Mora 56',
                 '@freddier #platzi 10',pd.NA]}


df = pd.DataFrame(data)
'''
Para usar las funciones asociadas a texto usamos str en nuestro DataFrame
'''
print("-"*100)
print(df['names'].str.lower())
'''
Para mayúsculas igualmente:
'''
print("-"*100)
print(df['names'].str.upper())
'''
Si queremos solo la primera letra en mayúscula:
'''
print("-"*100)
print(df['names'].str.capitalize())
'''
Para contar la longitud de nuestro texto usamos:
'''
print("-"*100)
print(df['names'].str.len())
'''
Para dividir el texto por espacios usamos split y definimos el carácter por
el que queremos dividir, en este caso, un espacio vacío ' ' o '#':
'''
print("-"*100)
print(df['names'].str.split(' '))
print("-"*100)
print(df['names'].str.split('#'))
'''
Para seleccionar los primeros o últimos 5 caracteres usamos:
'''
print("-"*100)
print(df['names'].str[:5])
print("-"*100)
print(df['names'].str[-5:])
'''
Podemos reemplazar una secuencia de caracteres por otra mediante:
'''
print("-"*100)
print(df['names'].str.replace('Alfredo','Antonio'))
'''
También podemos buscar una secuencia de texto en específico, en este caso,
'ara':
'''
print("-"*100)
print(df['names'].str.findall('ara'))
'''
También podemos crear un filtro basándonos en una secuencia de texto en
específico, en este caso, las filas que tengan 'or':
'''
print("-"*100)
print(df['names'].str.contains('or'))
'''
Así mismo, podemos contar el número de ocurrencias de un caracter en específico,
por ejemplo, cuántas veces aparece la letra 'a':
'''
print("-"*100)
print(df['names'].str.lower().str.count('a'))
'''
Existen comandos más avanzados usando Regex, por ejemplo, si quiero extraer los
caracteres numéricos:
'''
print("-"*100)
print(df['names'].str.extract('([0-9]+)', expand=False))
'''
O, por ejemplo, si quiero extraer las menciones '@xxxx' del texto:
'''
print("-"*100)
print(df['names'].str.replace('@[^\s]+',''))
