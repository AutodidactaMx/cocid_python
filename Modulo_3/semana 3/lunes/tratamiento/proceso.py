from utileria.utileria.generico import obtenerDatos
from persistencia.ventas import VentasPersistencia

def CargaDatos(RUTA_DATOS):
    datos = obtenerDatos(RUTA_DATOS)
    VentasPersistencia().insertarMany(datos)

def ProcesoVentasDepartameto() -> list:
    ventasP = VentasPersistencia()
    ventas_departamento = ventasP.ventasPorDepartamento()
    return ventas_departamento
