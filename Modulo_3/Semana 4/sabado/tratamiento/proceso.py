from utileria.generico import obtenerDatos
from persistencia.ventas import VentasPersistencia


def CargaDatos(RUTA_DATOS):
    datos = obtenerDatos(RUTA_DATOS)
    VentasPersistencia().insertarMany(datos)

def ProcesoVentasDepartameto(opcion =None) -> list:
    ventasP = VentasPersistencia()
    ventas_departamento = ventasP.ventasPorDepartamento(opcion)
    return ventas_departamento

def ObtenerDepartementos() -> list:
    ventasP = VentasPersistencia()
    return ventasP.ObtenerDepartamentos()
    
