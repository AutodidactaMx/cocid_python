import csv
from operaciones.distribucion_frecuencia import Distribucion_Frecuencia
from operaciones.persistencia import guardar, leer
conjunto_datos = []

try:
    conjunto_datos = leer("lista.csv")
    edades_df = Distribucion_Frecuencia(datos_agrupados=conjunto_datos)
    tablas_df = edades_df.calculo()     
    guardar("Distribucion de frecuencia.csv",tablas_df)
except Exception as e:
    print("Surgio un error en el calculo de Distribucion de frecuencia error :"+str(e))
