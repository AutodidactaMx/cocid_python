from modelo.ventas_model import VentasModel
from modelo.ventas_servicio_model import VentasServicioModel
from datetime import datetime
from persistencia.ventas import VentasPersistencia
from persistencia.ventas_servicio import VentasServicioPersistencia

def CargaVentasDatos(RUTA_DATOS):
    informacion = []
    with open((f"{RUTA_DATOS}"), mode="r", encoding="utf-8") as archivo:
        next(archivo)
        for line in archivo.readlines():
            fila = line.split(',')            
            obj = VentasModel(
                id =fila[0], 
                descuento =fila[1], 
                total=float(fila[2]),
                propina=float(fila[4]),
                modo_pago= fila[5],
                fecha_hora_venta = datetime.strptime(fila[6].replace('"', '').replace('\n', ''), '%Y-%m-%d %H:%M:%S').date()
                )
            informacion.append(obj)
    VentasPersistencia().insertarMany(informacion)

def CargaVentasServiciosDatos(RUTA_DATOS):
    informacion = []
    with open((f"{RUTA_DATOS}"), mode="r", encoding="utf-8") as archivo:
        next(archivo)
        for line in archivo.readlines():
            fila = line.split(',')            
            obj = VentasServicioModel(
                total =float(fila[0]),
                fecha_hora_venta =datetime.strptime(fila[1].replace('"', '').replace('\n', ''), '%Y-%m-%d %H:%M:%S').date(),
                servicio=fila[2].replace('\n', '')
                )
            informacion.append(obj)
    VentasServicioPersistencia().insertarMany(informacion)
