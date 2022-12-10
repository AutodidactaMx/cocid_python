'''
El primer gráfico representa la distribución de frecuencias de la 
variable Edad.
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sidetable 
from IPython.display import display
import tkinter as tk
from pandastable import Table, TableModel

'''Cargamos la data'''
df = pd.read_csv('bienes_raices.csv')
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
df_edad = df[['edad_compra']]
'''
Hacemos un tratmiento para generar valores en intervalos de 
6 contenedores por edad de compra
'''
df_edad["edad_rango"]= pd.cut(df["edad_compra"],6)

'''
Creamos una columna con la finalidad agrupar todo el 
conjunto de datos por los datos  de parametros estadisticos basicos
como medidas de tendencia centra y de dispersion

El sesgo es un peso desproporcionado a favor o en contra de una cosa,
persona o grupo en comparación con otra, generalmente de una manera 
que se considera injusta. Los sesgos se pueden aprender observando contextos culturales
'''
def mod(x):
    return x.value_counts().index[0]

df_std_full = df
df_std_full["GENERAL"] = "G" 
df_std = df_std_full.groupby(['GENERAL'])[["edad_compra"]].aggregate(
    [np.mean,np.median,np.std,np.var, mod, pd.DataFrame.skew])

'''
Calculamos  informacion para la frecuecia de datos por edad de compra
y ordenamos el valor
'''
resume_compra =  df_edad.stb.freq(['edad_compra'])
resume_compra = resume_compra.sort_values(by='edad_compra', ascending=True)
resume =  df_edad.stb.freq(['edad_rango'])
'''
Graficamos la los intervalos de edad y un histograma para verificar el sesgo, desviasion existente  de los datos
'''
fig, axes = plt.subplots(nrows=1, ncols=2)

df_edad['edad_compra'].plot.hist(bins=6,edgecolor='black', linewidth=1.2,ax=axes[0])
resume_compra.plot.bar(x='edad_compra', y='count', figsize=(10, 5),ax=axes[1])


class DataFrameTable(tk.Frame):
    def __init__(self, parent=None, df=pd.DataFrame()):
        super().__init__()
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)
        self.table = Table(
            self, dataframe=df,
            showtoolbar=False,
            showstatusbar=True,
            editable=False)      
        self.table.show()          


root = tk.Tk()
table = DataFrameTable(root, df_edad)
table = DataFrameTable(root, df_std)
plt.show()
root.mainloop()

