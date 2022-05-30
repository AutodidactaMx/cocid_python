import pandas as pd
import numpy as np
import seaborn as sns
pd.options.display.float_format = '{:,.2f}'.format
df = sns.load_dataset('tips')
df['ones'] = 1
print("-"*100)
print(df)
print("-"*100)
df_g = df.groupby(['sex','smoker'])[['ones']].sum()
print(df_g)
print("-"*100)
print(df_g.groupby('sex').apply(lambda x : x / x.sum() * 100 ))
print("-"*100)
pd.cut(df['total_bill'],bins = 3)
print("-"*100)
print(pd.cut(df['total_bill'],bins = 3).value_counts())
print("-"*100)
df['total_bill_bin'] = pd.cut(df['total_bill'],bins = [3,18,35,60])
print(df)
print("-"*100)
print(df.groupby(['time','total_bill_bin'])[['ones']].count())
print("-"*100)
print(df.groupby(['time','total_bill_bin'])[['ones']].count().groupby('time').apply(lambda x : x / x.sum() * 100 ))