import csv
from operaciones.distribucion_frecuencia import Distribucion_Frecuencia
from operaciones.persistencia import guardar, leer,leerExcel
conjunto_datos = []

try:
    conjunto_datos = leerExcel("E.xlsx",'A2','A50')
    edades_df = Distribucion_Frecuencia(datos_agrupados=conjunto_datos)
    tablas_df = edades_df.calculo()     
    guardar("Distribucion de frecuencia.csv",tablas_df)
except Exception as e:
    print("Surgio un error en el calculo de Distribucion de frecuencia error :"+str(e))
