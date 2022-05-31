'''
Se aprendio a agupar dataframe en una categoria y crear funciones par aaplicarlas
'''
import pandas as pd
import numpy as np

df = pd.read_csv('diamonds.csv')
print(df)
'''
Agrupacion categorical aplicandoherramientas 
estadisticas de todo el DataFrame completo o por columna
'''
print(df.groupby('cut').mean())
print(df.groupby('cut').median())
print(df.groupby('cut')['carat'].max())
print(df.groupby('cut')['carat'].min())

'''
Iteracion de la agrupacion por corte
'''
for k, v in df.groupby('cut') :
    gb = v['price'].mean()
    print(f'Cut {k}, Price avg {gb}')
    
'''
Agrupacion por corte y coloro calculando 
el minimo de la columna de precio
'''
print(df.groupby(['cut','color'])['price'].min().to_frame())
'''
Agregacion de funciones aplicadas a la agrupacion 
por medio de la funcion aggregate
'''
print(df.groupby(['cut','color'])['price'].aggregate(['mean','median','std']))
'''
Aplicacion de funcion en agrupacion
'''
def mean_k(x):
    return np.mean(x)/1000
print(df.groupby(['cut','color'])['price'].aggregate(['mean','median','std',mean_k]))
'''
Aplciacion de funciones por medion de 
indicacion de aplicacion
'''
dict_agg = {'carat':[min,max],'price':[np.mean,mean_k]}
print(df.groupby(['cut','color']).aggregate(dict_agg))
'''
Aplicacion de filtri por agrupacion
'''
def f_filter(x):
    return mean_k(x['price']) > 4

print(df.groupby('cut').filter(f_filter))
print(df.groupby('cut').filter(f_filter).unique())