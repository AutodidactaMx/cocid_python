'''
Nota: Los precios se indican para todas las propiedades. Sin embargo, las edades están disponibles sólo para individuos y no para empresas.
Las filas que incluyen empresas (no tienen un valor de edad) son automáticamente ignoradas en todas las medidas de 
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sidetable 
from IPython.display import display
import tkinter as tk
from pandastable import Table, TableModel

'''Cargamos la data'''
df = pd.read_csv('./semana_3/sabado/bienes_raices.csv')
'''
Limpiamos datos con espacio vacios y elimnamos todo
valor en nulo
'''
df = df.replace(' ',pd.NA)
df = df.dropna(subset=['edad_compra'])
'''
Cambiamos el tipo de dato object a numerico
'''
df['edad_compra'] =  pd.to_numeric(df['edad_compra'])
'''
Nos llevamos la columna con la que vamos a trabajar
en este caso es edad
'''
df_edad = df[['edad_compra','Precio']]
display(df_edad.cov())
ax1 = df_edad.plot.scatter(x='Precio',y='edad_compra', c='DarkBlue', figsize=(10, 5))
ax1.set_xlim(0, 600000)
plt.show()