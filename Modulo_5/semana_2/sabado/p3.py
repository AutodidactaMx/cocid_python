'''
Manejo de Data Frame con indices retomando que el índice nos 
permite encontrar la información de un archivo para darnos las coordenadas 
utilizando la estructura de los datos para aplicar funciones matemáticas a varios niveles
'''
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.1f}'.format
print("-"*100)
df = pd.read_csv('poblacion.csv')
print(df)
print("-"*100)
df['year'] = pd.Categorical(df['year'].apply(str))
print(df.dtypes)
print("-"*100)
idx_filtro = df['Country'].isin(['Armenia', 'Colombia'])
print(idx_filtro)
print("-"*100)
df_filtro_country = df[idx_filtro]
print(df_filtro_country)
print("-"*100)
df_filtro_country = df_filtro_country.set_index(
    ['Country', 'year']).sort_index()
print(df_filtro_country.loc['Colombia', :])
print("-"*100)
print("-"*100)
print(df_filtro_country.loc['Colombia', :].loc['2015', :])
print("-"*100)
print(df_filtro_country.xs(['Colombia', '2015']))
print("-"*100)
print(df_filtro_country.xs('2015', level='year'))
print("-"*100)
print(df_filtro_country.xs('Colombia', level='Country'))

print("-"*100)
df_countries = df.set_index(
    ['Country', 'year']).sort_index(ascending=[True, True])
print(df_countries)
print("-"*100)
ids = pd.IndexSlice
print(df_countries.loc[ids['Albania':'Azerbaijan',
      '2015':'2016'], :].sort_index())
print("-"*100)
print(df_countries.index.get_level_values(0))
print("-"*100)
print(df_countries.index.get_level_values(1))
print("-"*100)
print(df_countries['pop']['Colombia']['2018'])
print("-"*100)
print(df_countries.sum(level='year'))
print("-"*100)
print(df_filtro_country.unstack('year'))
print("-"*100)
print(df_filtro_country.unstack('Country'))
