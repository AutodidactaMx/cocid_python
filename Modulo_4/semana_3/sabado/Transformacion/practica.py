import os
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

RUTA_ORIGEN = "./Transformacion/data/origen"
RUTA_DESTINO = "./Transformacion/data/destino"

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

    fechaIniFiltro = datetime(2022, 10, 29, 10, 00, 0, 0)
    fechaFinFiltro = datetime(2022, 10, 29, 12, 00, 0, 0)

    concatenado = pd.concat([dfKWHS, dfKWHE])

    filtro = concatenado[(concatenado["Fecha"] >= fechaIniFiltro) & (concatenado["Fecha"] <= fechaFinFiltro)]
    total = filtro['Fecha'].count()
    if total > 0:                        
        df = pd.concat([df, filtro])        

df = pd.pivot_table(df, values='Valor', index=['Fecha'],
                    columns=['Clave_de_medicion'], fill_value=0)         

destino = f"{RUTA_DESTINO}/procesado.csv"           


df.to_csv(destino)

#axes = df.plot.line(rot=0, marker='*', subplots=False)
#plt.show()
