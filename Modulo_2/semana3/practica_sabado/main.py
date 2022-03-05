from operaciones.distribucion_frecuencia import Distribucion_Frecuencia
conjunto_datos = [
    38, 15, 10, 12, 62, 46, 25, 56, 27, 24, 23, 21, 20, 25, 38, 27, 48, 35, 50, 65, 59, 58, 47, 42, 37, 35, 32, 40, 28, 14, 12, 24, 66, 73, 72, 70, 68, 65, 54, 48, 34, 33, 21, 19, 61, 59, 47, 46, 30, 30
]

try:
    edades_df = Distribucion_Frecuencia(datos_agrupados=conjunto_datos)
    tablas_df = edades_df.calculo()
    edades_df.mostrar_tablas(tablas_df=tablas_df)
except Exception as e:
    print("Surgio un error en el calculo de Distribucion de frecuencia error :"+str(e))
