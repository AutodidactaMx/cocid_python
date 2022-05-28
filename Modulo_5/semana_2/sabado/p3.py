'''
Manejo de Data Frame con indices retomando que el indice nos
permite encontrar la informacion deun archivo para darnos las coordenadas
utilizando la estructura de los datos para aplciar funciones matematicas a varios niveles
'''
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.1f}'.format

df = pd.read_csv('poblacion.csv')
#print(df)
df['year'] = pd.Categorical(df['year'].apply(str))
#print(df.dtypes)
idx_filtro = df['Country'].isin(['Armenia','Colombia'])
#print(idx_filtro)
df_filtro_country = df[idx_filtro]
#print(df_filtro_country)

#df_filtro_country = df_filtro_country.set_index(['Country','year'])
#print(df_filtro_country)
df_filtro_country =df_filtro_country.set_index(['Country','year']).sort_index()
#print(df_filtro_country.loc['Colombia',:])
#print(df_filtro_country.loc['Colombia',:].loc['2015',:])
#print(df_filtro_country.xs(['Colombia','2015']))

#print(df_filtro_country.xs('2015',level='year'))
#print(df_filtro_country.xs('Colombia',level='Country'))


df_countries =df.set_index(['Country','year']).sort_index(ascending= [True,True])
#print(df_countries)

ids = pd.IndexSlice

#print(df_countries.loc[ids['Albania':'Azerbaijan','2015':'2016'],:].sort_index())

#print(df_countries.index.get_level_values(0))
#print(df_countries.index.get_level_values(1))

#print(df_countries['pop']['Colombia']['2018'])

#Calculo de la suma de poblacion a nivel de indice del anio
#print(df_countries.sum(level='year'))

print(df_filtro_country.unstack('year'))
print(df_filtro_country.unstack('Country'))



