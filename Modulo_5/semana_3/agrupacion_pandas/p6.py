'''
Se aprendio unificar dos dataframe por medio de merge 
contectandolos por medio de este parametros, en el caos de base de datos esta relacioanda en
llaves primarias y secundarioas
'''
import pandas as pd
import numpy as np

df_left = pd.DataFrame(
                      {'X': ['x0', 'x1', 'x2', 'x3'],
                        'W': ['w0', 'w1', 'w2', 'w3'], 
                        'Y': ['y0', 'y1', 'y2', 'y3'] ,
                        'Mix': ['y2', 'y3', 'a2', 'a3']},
                       index=[0,1,2,3])
print(df_left)
df_right = pd.DataFrame(
                       {'Z': ['z2', 'z3', 'z4', 'z5'],
                         'A': ['a2', 'a3', 'a4', 'a5'], 
                         'Y': ['y2', 'y3', 'y4', 'y5']},
                        index=[2,3,4,5])
print(df_right)
#print(pd.merge(df_left, df_right))

#print(pd.merge(df_left, df_right, how = 'inner', on = 'Y'))

#print(pd.merge(df_left, df_right, how = 'inner', left_on = 'Mix', right_on = 'Y'))

#print(pd.merge(df_left, df_right, how = 'inner', left_on = 'Mix', right_on = 'A'))

#https://www.datasciencemadesimple.com/wp-content/uploads/2017/09/join-or-merge-in-python-pandas-1.png

#print(pd.merge(df_left, df_right, how = 'inner', on = 'Y'))

#print(pd.merge(df_left, df_right, how = 'left', on = 'Y'))

#print(pd.merge(df_left, df_right, how = 'right', on = 'Y'))

#print(pd.merge(df_left, df_right, how = 'outer', on = 'Y'))

df_left = pd.DataFrame(
                      {'X': ['x0', 'x1', 'x2', 'x3'],
                        'W': ['w0', 'w1', 'w2', 'w3'], 
                        'Y': ['y0', 'y1', 'y2', 'y3'],
                        'A': ['a0', 'a1', 'a2', 'a3'],})

print(pd.merge(df_left, df_right, how ='outer', on = [ 'A', 'Y'], suffixes=['_left','_right']) )
#print(pd.merge(df_left, df_right, how ='outer', on = 'A', suffixes=['_left','_right']) )