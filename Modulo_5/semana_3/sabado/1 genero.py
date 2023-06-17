'''
Nota: Las empresas no tienen género. Sin embargo, 
necesitamos añadirlas a este gráfico circular, ya que de lo contrario, 
obtendremos una interpretación errónea de los datos.
'''
'''
Vemos datos segadas debido que las personas que solo muestra a las personas 
que firman el contrato el cual representa a una familia, pero vemos un dato 
interesante las que hay un porcentaje representado por las empresas
'''

import pandas as pd
import matplotlib.pyplot as plt
from pandastable import Table
import tkinter as tk
'''
Carga de archivo csv
'''
df = pd.read_csv('bienes_raices.csv')
'''Remplazar valores NA asignar valor B para representar el negocio'''
df['genero']= df['genero'].fillna('B')
'''
Calculamos la frecuencia valor de genero
'''
df_genero = df.groupby(['genero'])['genero'].count().to_frame("Frecuencia")
'''
Calculamos la frecuencia relativa
'''
df_genero["Frecuencia_relativa"] = (df_genero["Frecuencia"] / df_genero["Frecuencia"].sum()) * 100
'''
Graficamos las variables
'''
df_genero.plot.pie(y='Frecuencia_relativa', figsize=(5, 5), autopct='%1.1f%%',shadow=True)


'''
Imprimimos el resumen de tabla de frecuencias
'''
class DataFrameTable(tk.Frame):
    def __init__(self, df=pd.DataFrame()):
        super().__init__()        
        self.pack(fill=tk.BOTH, expand=True)
        self.table = Table(
            self, dataframe=df,
            showtoolbar=False,
            showstatusbar=True,
            editable=False)
        self.table.show()
        plt.show()

table = DataFrameTable(df_genero)
table.display_table()