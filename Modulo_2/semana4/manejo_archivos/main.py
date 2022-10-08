import os
from operaciones.distribucion_frecuencia import Distribucion_Frecuencia
from operaciones.manipulador_archivo import ManipuladorArchivo

try:
    ma = ManipuladorArchivo("./base_datos/edades.txt")
    ma.crear_archivo_datos_aleatorios(5)
    ma.agregar_archivo_datos_aleatorios(5)
    
    conjunto_datos = ma.extraer_datos_archivo()
    edades_df = Distribucion_Frecuencia(datos_agrupados=conjunto_datos)
    tablas_df = edades_df.calculo()
    edades_df.mostrar_atributos()
    edades_df.mostrar_tablas(tablas_df=tablas_df)
except Exception as e:
    print("Surgio un error en el calculo de Distribucion \
          de frecuencia error :"+str(e))
