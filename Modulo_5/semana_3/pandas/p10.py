import pandas as pd
import numpy as np
'''
Para comenzar, importemos el archivo de informacion de propinas
'''
df = pd.read_csv('tips.csv')
'''Agrega una columna como indicador de presencia de registro'''
df['ones'] = 1
print("-"*100)
print(df)
'''
Preparamos un DataFrame con la agrupacion por categoria sex y 
smoker identificandola cantidad de existencia
'''
print("-"*100)
df_g = df.groupby(['sex','smoker'])[['ones']].sum()
print(df_g)
'''
Aplicamos un agrupamiento por sex en el nuevo DataFrame usando
apply por landa
'''
print("-"*100)
print(df_g.groupby('sex').apply(lambda x : x / x.sum() * 100 ))
'''
Vamos a segmentar y ordenar valores de datos 
en contenedores.'''
print("-"*100)
pd.cut(df['total_bill'],bins = 3)
print("-"*100)
print(pd.cut(df['total_bill'],bins = 3).value_counts())
'''
Creamos en el DataFrame inicial la segmentacion de valores
Con la finalidad de de convertir nuestros valores numericos 
en una categorica en una nueva columna
'''
print("-"*100)
df['total_bill_bin'] = pd.cut(df['total_bill'],bins = [3,18,35,60])
print(df)
'''
Ahora con la nueva columna podemos calcular el porcentaje 
mediante un operacion simple en time
'''
print("-"*100)
print(df.groupby(['time','total_bill_bin'])[['ones']].count())
print("-"*100)
print(df.groupby(['time','total_bill_bin'])[['ones']].count().groupby('time').apply(lambda x : x / x.sum() * 100 ))
