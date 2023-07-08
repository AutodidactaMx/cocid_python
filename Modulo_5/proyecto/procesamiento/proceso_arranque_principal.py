from persistencia.ventas import VentasPersistencia
from persistencia.ventas_servicio import VentasServicioPersistencia
import pandas as pd

def cargaInicialDatos():
    listaVenta = VentasPersistencia().consultarTodo()
    listaVentaServicio = VentasServicioPersistencia().consultarTodo()

    ventas_modelo = [modelo.__dict__ for modelo in listaVenta]
    ventas_servicio_modelo = [modelo.__dict__ for modelo in listaVentaServicio]

    dataframeVentas = pd.DataFrame(ventas_modelo)
    dataframeServicios = pd.DataFrame(ventas_servicio_modelo)    
    
    return dataframeVentas, dataframeServicios
