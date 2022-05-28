'''
Ejercicios de group by
'''
import pandas as pd
import numpy as np
import seaborn as sns

pd.options.display.float_format = '{:,.2f}'.format
df = sns.load_dataset('tips')
print(df,end=f'\n')
print("-"*100)
print(df.describe(include='all'))
print("-"*100)
print(df['day'].value_counts())
print("-"*100)
print(df['day'].value_counts() / df['day'].value_counts().sum() * 100)
print("-"*100)
print(df.groupby('sex').mean())
print("-"*100)
df['tip_%'] = df['tip']/df['total_bill']
print(df)
print("-"*100)
print(df.groupby('sex').mean())
print("-"*100)
print(df.groupby('sex').median())
print("-"*100)
print(df.groupby('sex')[['total_bill','tip_%']].describe())
print("-"*100)
def mean_eurtousd(x):
    return np.mean(x)*1.12
print(df.groupby(['sex','time'])[['total_bill','tip_%']].apply(mean_eurtousd))
print("-"*100)
print(df.groupby(['sex','time'])[['total_bill','tip_%']].apply(np.std))
print("-"*100)
print(df.groupby(['sex','time'])[['total_bill','tip_%']].apply(lambda x : np.mean(x) * 1.2))
print("-"*100)
print(df.groupby(['sex','time'])[['total_bill','tip_%']].aggregate([np.mean,np.std,np.max]))
print("-"*100)
dict_agg = {'tip':[min,max],'total_bill':[np.mean,mean_eurtousd]}
print(df.groupby(['sex','time'])[['total_bill','tip']].aggregate(dict_agg))
print("-"*100)
def f_filter(x):
    return mean_eurtousd(x['total_bill'].mean()) > 20
print(df.groupby(['sex','time'])[['total_bill','tip']].filter(f_filter))
print("-"*100)
print(df.groupby(['sex','time'])[['total_bill','tip']].count())
