'''Es muy usual que los registros de una base de datos aparezcan más de una vez, 
así que veamos cómo pandas puede ayudarnos a lidiar con estos casos. Para comenzar, importemos pandas y
creemos un DataFrame con dos columnas y algunos datos repetidos.'''
import pandas as pd
import numpy as np

df = pd.DataFrame({'a': ['w'] * 4 + ['x'] * 3 + ['y'] * 2 + ['z']+['v'], 
                   'b': [1, 1, 1, 1, 2, 2, 2, 3, 3, 4,5]})
print(df)
'''Para encontrar los registros duplicados usamos duplicated , 
que marca con True aquellos casos de filas duplicadas:'''
print(df.duplicated())
'''Podemos usar keep='first' para marcar solo la primera ocurrencia
o keep='last' para marcar la última:'''
print(df.duplicated(keep='first'))
print(df.duplicated(keep='last'))
'''Identificados los casos duplicados, podemos usar este 
resultado para filtrar y seleccionar aquellos que no tienen un registro duplicado:
'''
print('-'*100)
print(df[~ df.duplicated()])
'''Si quisieras dejar el primer registro de los duplicados o el último, 
recuerda usar keep='first' o keep='last'. Remarco el hecho de que usé negación '~' para ver los registros no duplicados.
Y si me interesara ver cuáles son los registros duplicados, podemos usar keep=False:'''
print('-'*100)
print(df.duplicated(keep=False))
print('-'*100)
print(df[df.duplicated(keep=False)])
'''Por último, puedes usar el comando 'drop_duplicates' para eliminar los duplicados.
Por defecto, la función guarda el primer resultado keep='first':'''
print('-'*100)
print(df.drop_duplicates())
'''Y si quieres solo borrar duplicados teniendo en 
cuenta una sola columna, lo puedes hacer mediante una lista nombrando las columnas donde vas a eliminar los duplicados, en este caso, ['a']:
'''
print('-'*100)
print(df.drop_duplicates(['a'],keep='last'))
