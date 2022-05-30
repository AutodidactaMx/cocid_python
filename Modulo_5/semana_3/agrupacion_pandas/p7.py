'''
Se aprendio a agupar dataframe en una categoria y crear funciones par aaplicarlas
'''
import pandas as pd
import numpy as np
import seaborn as sns
df = sns.load_dataset('diamonds')
print(df)
print(df.groupby('cut').mean())
print(df.groupby('cut').median())
print(df.groupby('cut')['carat'].max())
print(df.groupby('cut')['carat'].min())

for k, v in df.groupby('cut') :
    gb = v['price'].mean()
    print(f'Cut {k}, Price avg {gb}')
    
print(df.groupby(['cut','color'])['price'].min().to_frame())

print(df.groupby(['cut','color'])['price'].aggregate(['mean','median','std']))

def mean_k(x):
    return np.mean(x)/1000

print(df.groupby(['cut','color'])['price'].aggregate(['mean','median','std',mean_k]))

dict_agg = {'carat':[min,max],'price':[np.mean,mean_k]}

print(df.groupby(['cut','color']).aggregate(dict_agg))

def f_filter(x):
    return mean_k(x['price']) > 4

print(df.groupby('cut').filter(f_filter))

print(df.groupby('cut').filter(f_filter).unique())