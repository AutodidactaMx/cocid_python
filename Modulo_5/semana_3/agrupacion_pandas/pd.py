import pandas as pd
import numpy as np
df = pd.read_csv('poblacion.csv')
pd.options.display.float_format = '{:,.1f}'.format
df = pd.read_csv('poblacion.csv')
df['year'] = pd.Categorical(df['year'].apply(str))

idx_filtro = df['Country'].isin(['Mexico','Panama'])
df_filtro_country = df[idx_filtro]

df_filtro_country =df_filtro_country.set_index(['Country','year']).sort_index(ascending= [False,True])

print(df_filtro_country.unstack('Country'))
ids = pd.IndexSlice
print(df_filtro_country.loc[ids['Albania':'Azerbaijan','2015':'2016'],:].sort_index())


