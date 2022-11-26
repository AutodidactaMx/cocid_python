'''https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.xs.html'''
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.1f}'.format
df = pd.read_csv('./index/poblacion.csv')
df['año'] = pd.Categorical(df['año'].apply(str))
df['pais'] = pd.Categorical(df['pais'])
df = df.set_index(['pais', 'año']).sort_index()

print(df.loc['Afghanistan', :])
print(df.loc[['Colombia'],['2015'], :])
print(df.loc['Colombia', :].loc['2015', :])
print(df.xs(['Colombia', '2015']))
print(df.xs('2015', level='año'))
print(df.xs('Colombia', level='pais'))
print(df['pop']['Colombia']['2018'])



