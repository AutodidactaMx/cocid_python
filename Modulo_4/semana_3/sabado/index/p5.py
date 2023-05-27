import pandas as pd
import numpy as np
pd.options.display.float_format = '{:,.1f}'.format
df = pd.read_csv('./index/poblacion.csv')
print("-"*100)
print(df.head(5))
print("-"*100)
df = df.set_index(['año','pais']).sort_index(ascending=False)
print("-"*100)
print(df.head(5))
print("-"*100)
print(df.index.get_level_values(0))
print("-"*100)
print(df.index.get_level_values(1))
print("-"*100)
print(df.head(10))
