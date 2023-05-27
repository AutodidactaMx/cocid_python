'''https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.xs.html'''
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.1f}'.format
df = pd.read_csv('./index/poblacion.csv')
df['año'] = pd.Categorical(df['año'].apply(str))
df['pais'] = pd.Categorical(df['pais'])
print("-"*100)
print(df.head(5))
print("-"*100)
# Sintaxis básica de loc
print(df.loc[1:5,'año'])
print("-"*100)
# Selección por etiquetas de índice
print(df.loc[1])
print("-"*100)
# Selección por nombres de columnas
print(df.loc[:,'pais'])
# Selección de filas y columnas simultáneamente
print(df.loc[2:5,'pais':'año'])
