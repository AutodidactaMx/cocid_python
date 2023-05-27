'''https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.xs.html'''
import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.1f}'.format
df = pd.read_csv('./index/poblacion.csv')
print(df.head(5))
print("-"*100)
df['año'] = pd.Categorical(df['año'].apply(str))
df['pais'] = pd.Categorical(df['pais'])
print("-"*100)
print(df.head(5))
print("-"*100)
df = df.set_index(['pais', 'año']).sort_index()
print("-"*100)
print(df.head(5))
print("-"*100)
print(df.loc['Afghanistan', :])
print("-"*100)
print(df.loc[['Colombia'],['2015'], :])
print("-"*100)
print(df.loc['Colombia', :].loc['2015', :])
print("-"*100)
print(df.xs(['Colombia', '2015']))
print("-"*100)
print(df.xs('2015', level='año'))
print("-"*100)
print(df.xs('Colombia', level='pais'))



