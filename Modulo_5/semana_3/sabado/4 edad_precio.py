'''
Nota: Los precios se indican para todas las propiedades. Sin embargo, las edades están disponibles 
sólo para individuos y no para empresas.
Las filas que incluyen empresas (no tienen un valor de edad) son automáticamente 
ignoradas en todas las medidas
'''
from re import sub
from decimal import Decimal
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sidetable 
from IPython.display import display
import tkinter as tk
from pandastable import Table, TableModel

def limpiarFormatDecimal(x):
    return Decimal(sub(r'[^\d.]', '', x))

'''Cargamos la data'''
df = pd.read_csv('./bienes_raices.csv')
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
df['Precio'] = df['Precio'].apply(limpiarFormatDecimal)

'''
Nos llevamos la columna con la que vamos a trabajar
en este caso es edad
'''
df_edad = df[['edad_compra','Precio']]
df_edad['edad_compra_median'] = np.median(df_edad[['edad_compra']])
df_edad['Precio_median'] = np.median(df_edad[['Precio']])
display(df_edad[['edad_compra','Precio']].cov())

'''
Cuando entre las dos variables hay un relacion directa, la conrianza da un valor positivo
'''
plt.scatter(df_edad['edad_compra'], df_edad['Precio'], c ="blue",
            linewidths = 2)
 
plt.scatter(df_edad['edad_compra_median'], df_edad['Precio_median'], c ="red",
            linewidths = 2)
plt.ylim(0, 600000)
plt.xlabel("Edad compra")
plt.ylabel("Media")
plt.show()
