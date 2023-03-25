from const.conf import RUTA_DATOS
from datetime import datetime
from modelos.modelo_venta import VentasSemanales


def obtenerDatos():
    informacion = []
    with open((f"{RUTA_DATOS}"), mode="r", encoding="utf-8") as archivo:
        next(archivo)
        for line in archivo.readlines():
            fila = line.split(',')            
            obj = VentasSemanales(
                tienda=int(fila[0]),
                departamento=fila[1],
                fecha=datetime.strptime(fila[2], '%d/%m/%Y').date(),
                ventasSemanales=float(fila[3]),
                esVacaciones=bool(fila[4]))
            informacion.append(obj)
    return informacion
