'''
Unid dataframe para unificar nuestros paquetes de información 
concatenando numpy dataframe
'''
import pandas as pd
import numpy as np

'''
Se configura el formato visual de tipo numerico
'''
pd.options.display.float_format = '{:,.2f}'.format
np.set_printoptions(precision=2)
'''
Creacion de informacion por medio de numpy
'''
print("-"*100)
x1 = np.random.rand(2,5) * 100
x2 = np.random.rand(2,5) * -1
print(x1)
print(x2)
'''
Concatenacion de arreglos
'''
print("-"*100)
x = np.concatenate([x1,x2])
x = np.concatenate([x1,x2],axis=1)
print(x)
'''
Creacion de series  usnado los arreglos de numpy
'''
print("-"*100)
s1 = pd.Series(x1[0], index=['a','b','c','d','e'])
s2 = pd.Series(x2[0], index=['f','g','h','i','j'])
'''
Concatenacion de series de dataFrame
'''
print("-"*100)
s = pd.concat([s1,s2])
print(s)
s = pd.concat([s1,s2],axis=1)
print(s)
s = pd.concat([s1.reset_index(drop=True),s2.reset_index(drop=True)],axis=1)
print(s)
'''
Creacion de Dataframe por medio de numpy
'''
print("-"*100)
df1 = pd.DataFrame(np.random.rand(3,2)*10, columns=['a','b'])
df2 = pd.DataFrame(np.random.rand(3,2)*-1, columns=['a','b'], index=[2,3,4])
print(df1)
print(df2)
'''
Concatenacion de dataframes por medio de DataFrame
'''
dfs = pd.concat([df1,df2])
print(dfs)
dfs = pd.concat([df1,df2],axis=1)
print(dfs)
dfs = pd.concat([df1,df2],axis=1, join='inner')
print(dfs)
dfs = pd.concat([df1.reset_index(drop=True),df2.reset_index(drop=True)],axis=1)
'''
Concatenacion por medio append  usandolo como agregacion
'''
print(dfs)
dfs = df1.append(df2)
print(dfs)
dfs = df1.append(df2).append(df2)
print(dfs)
'''
Cambio de posicion filas por columnas
'''
print(dfs.T)
print(df1.T.append(df2.T))
