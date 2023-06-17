import pandas as pd
import numpy as np
'''
Para comenzar, importemos el archivo de informacion de propinas
'''
df = pd.read_csv('tips.csv')
'''
Analizamos la informacion con la descripcion 
generar que ofrece DataFrame
'''
print(df.describe(include='all'))
'''
Calculamos el proceentaje de los dias de cantidad de 
audiencia en ventas
'''
print("-"*100)
print(df['day'].value_counts() / df['day'].value_counts().sum() * 100)
'''
Clasificaremos las propinas por sexo agregando una columna 
de porcentaje de propinas 
'''
print("-"*100)
print(df.groupby('sex').mean())
print("-"*100)
df['tip_%'] = df['tip']/df['total_bill']
print(df)
'''
Analizara el impacto en propinas categorizadas por 
sexo revisando la media y mediana
'''
print("-"*100)
print(df.groupby('sex').mean())
print("-"*100)
print(df.groupby('sex').median())
print("-"*100)
print(df.groupby('sex')[['total_bill','tip_%']].describe())
print("-"*100)
'''
Aplicamos el calculo estadistico por funciones 
ocupando el apply y en su caso agregar mas de una funcion ocupando el aggregate
'''
def mean_eurtousd(x):
    return np.mean(x)*1.12
print(df.groupby(['sex','time'])[['total_bill','tip_%']].apply(mean_eurtousd))
print("-"*100)
print(df.groupby(['sex','time'])[['total_bill','tip_%']].apply(np.std))
print("-"*100)
print(df.groupby(['sex','time'])[['total_bill','tip_%']].apply(lambda x : np.mean(x) * 1.2))
print("-"*100)
print(df.groupby(['sex','time'])[['total_bill','tip_%']].aggregate([np.mean,np.std,np.max]))
print("-"*100)
dict_agg = {'tip':[min,max],'total_bill':[np.mean,mean_eurtousd]}
print(df.groupby(['sex','time'])[['total_bill','tip']].aggregate(dict_agg))



