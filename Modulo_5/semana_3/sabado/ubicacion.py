'''
Este es un diagrama de Pareto. Las barras muestran la frecuencia 
absoluta de cada categoría. En este caso esto se traduce en cuántos
clientes hay en cada estado. Por ejemplo, hay 4 clientes de Virginia.
'''
'''
El eje secundario (la línea naranja), muestra la frecuencia acumulativa. 
Por ejemplo, California, Nevada y Oregon juntos, representan el 81% de todas las compras.
'''
'''Tabla de distribución de frecuencias'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tkinter as tk
from pandastable import Table, TableModel

'''
sidetable comenzó como una combinación sobrealimentada
de pandas value_counts más tabulación cruzada que crea tablas de 
resumen simples pero útiles de su pandas DataFrame. Desde entonces, 
se ha expandido para brindar soporte para tareas comunes y útiles de pandas, 
como agregar subtotales a su DataFrame o aplanar columnas jerárquicas.
El uso es sencillo. Instalar e importar sidetable. Luego acceda a él a través
del nuevo acceso .stb en su DataFrame.
'''
import sidetable 

'''
Carga de el archivo de datos
'''
df = pd.read_csv('./semana_3/sabado/bienes_raices.csv')
'''
Apoyamos del paquete sidetable para usar el metodo
stb para poder tener la tabla de ddistribucion de frecuencia
'''
resume =  df.stb.freq(['Estado'])
'''
Se grafica una grafica de barra por total de Estado 
'''
ax = resume.plot.bar(x='Estado', y='count', figsize=(10, 5))
ax.set_ylabel('Frecuencia')
'''
Graficamos en la liena secundaria el acumulado en porcentaje
del estado
'''
ax2 = resume.plot.line(x='Estado', y='cumulative_percent',  marker='o', secondary_y=True, ax=ax, color = 'orange')
ax2.set_ylim(0, 100)
ax2.set_ylabel('Acumulativa')
ax2.set_title("Segmentación de los clientes de EE.UU. por Estado")

'''
Imprimimos el resumen de tabla de frecuencias
'''
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
        plt.show()


root = tk.Tk()
table = DataFrameTable(root, resume)
root.mainloop()