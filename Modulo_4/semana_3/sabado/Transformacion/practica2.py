''' https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html'''
import os
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

pd.options.display.float_format = '{:.3f}'.format

RUTA_ORIGEN = "./Transformacion/data/origen"
RUTA_DESTINO = "./Transformacion/data/destino"

def minimo(x):
    return np.min(x)

lista_archivos = os.listdir(RUTA_ORIGEN)
lista_archivos_filtro = list( filter(lambda x: (x.split('.')[1] == 'xlsx'),lista_archivos))


df = pd.DataFrame()
for archivo in lista_archivos_filtro:
    nombre_archivo = archivo.split('.')[0]   
    clave = nombre_archivo.split('_')[1] 
    ruta = f"{RUTA_ORIGEN}/{archivo}" 
    sheetKWHEntregada = f'{clave}kwhEntrada'
    sheetKWHRSalida = f'{clave}kwhSalida'

    dfKWHE = pd.read_excel(ruta, sheet_name=sheetKWHEntregada)    
    dfKWHS = pd.read_excel(ruta, sheet_name=sheetKWHRSalida)    

    dfKWHE['Fecha'] = pd.to_datetime(dfKWHE['Fecha'])
    dfKWHE['Clave'] = clave
    dfKWHE['Clave_de_medicion'] = sheetKWHEntregada

    dfKWHS['Fecha'] = pd.to_datetime(dfKWHS['Fecha'])
    dfKWHS['Clave'] = clave
    dfKWHS['Clave_de_medicion'] = sheetKWHRSalida
             
    df = pd.concat([df, dfKWHS, dfKWHE])        

dfg = df.groupby(['Clave','Clave_de_medicion'])[['Valor']].aggregate([minimo,np.mean,np.std,np.max])
axes = dfg.plot.bar(rot=0, subplots=False)
plt.show()
print(df)


