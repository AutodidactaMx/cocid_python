import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.1f}'.format
df = pd.read_csv('./index/poblacion.csv')


df = df.set_index(['pais', 'año']).sort_index()
print(df.index.get_level_values(0))
print(df.index.get_level_values(1))
print(df.head(10))
