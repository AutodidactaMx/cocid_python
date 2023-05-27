import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.1f}'.format
df = pd.read_csv('./index/poblacion.csv')
df['año'] = pd.Categorical(df['año'].apply(str))
df['pais'] = pd.Categorical(df['pais'])
df = df.set_index(['pais', 'año']).sort_index()

print(df.unstack('año'))
print(df.unstack('pais'))
print(df.sum(level='año'))
print(df.count(level='año'))
print(df.mean(level='año'))

