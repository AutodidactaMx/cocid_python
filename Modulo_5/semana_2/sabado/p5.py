'''
Unid dataframe par aunificar nuestros paquetes de informacion 
concatenando numpy dataframe
'''
import pandas as pd
import numpy as np

pd.options.display.float_format = '{:,.2f}'.format
np.set_printoptions(precision=2)

x1 = np.random.rand(2,5) * 100
x2 = np.random.rand(2,5) * -1
#print(x1)
#print(x2)
x = np.concatenate([x1,x2])
x = np.concatenate([x1,x2],axis=1)
#print(x)

s1 = pd.Series(x1[0], index=['a','b','c','d','e'])
s2 = pd.Series(x2[0], index=['f','g','h','i','j'])

s = pd.concat([s1,s2])
#print(s)
s = pd.concat([s1,s2],axis=1)
#print(s)
s = pd.concat([s1.reset_index(drop=True),s2.reset_index(drop=True)],axis=1)
#print(s)

#DF
df1 = pd.DataFrame(np.random.rand(3,2)*10, columns=['a','b'])
df2 = pd.DataFrame(np.random.rand(3,2)*-1, columns=['a','b'], index=[2,3,4])

#print(df1)
#print(df2)
dfs = pd.concat([df1,df2])
#print(dfs)
dfs = pd.concat([df1,df2],axis=1)
#print(dfs)
dfs = pd.concat([df1,df2],axis=1, join='inner')
#print(dfs)
dfs = pd.concat([df1.reset_index(drop=True),df2.reset_index(drop=True)],axis=1)
#print(dfs)
dfs = df1.append(df2)
#print(dfs)
dfs = df1.append(df2).append(df2)
#print(dfs)
#print(dfs.T)
print(df1.T.append(df2.T))
