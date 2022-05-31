'''
Se aprendio unificar dos dataframe por medio de merge 
contectandolos por medio de este parametros, en el caos de base de datos esta relacioanda en
llaves primarias y secundarioas
'''
import pandas as pd

df_left = pd.DataFrame(
                      {'X': ['x0', 'x1', 'x2', 'x3'],
                        'W': ['w0', 'w1', 'w2', 'w3'], 
                        'Y': ['y0', 'y1', 'y2', 'y3'] ,
                        'Mix': ['y2', 'y3', 'a2', 'a3']},
                       index=[0,1,2,3])

df_right = pd.DataFrame(
                       {'Z': ['z2', 'z3', 'z4', 'z5'],
                         'A': ['a2', 'a3', 'a4', 'a5'], 
                         'Y': ['y2', 'y3', 'y4', 'y5']},
                        index=[2,3,4,5])
'''
Visualizacion de DataFrame creados
'''
print(df_left)
print("-"*100)
print(df_right)
print("-"*100)
'''
Union dejandole la carga de indicar la relacion 
de union por columna en comun a la funcion merge
'''
print(pd.merge(df_left, df_right))
'''
Realizando una union de tipo inner join de dos columnas que distintas
'''
print(pd.merge(df_left, df_right, how = 'inner', left_on = 'Mix', right_on = 'Y'))
'''
Realizacndo una union por medio de valores en comun
'''
print(pd.merge(df_left, df_right, how = 'inner', on = 'Y'))
'''
Realizando una union con valores de lado izquierdo de la comparacion
'''
print(pd.merge(df_left, df_right, how = 'left', on = 'Y'))
'''
Realizando una union con valores de lado derecho de la comparacion
'''
print(pd.merge(df_left, df_right, how = 'right', on = 'Y'))
'''
Realizando una union con la union de todos los valores
'''
print(pd.merge(df_left, df_right, how = 'outer', on = 'Y'))