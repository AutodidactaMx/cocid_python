from tratamiento.util import obtenerDatos
from persistencia.ventas import VentasPersistencia

def CargaDatos():
    datas = obtenerDatos()
    ventasP = VentasPersistencia()
    ventasP.insertarMany(datas)

def ProcesoVentasDepartameto():
    ventasP = VentasPersistencia()
    ventas_departamento = ventasP.ventasPorDepartamento()
    print(ventas_departamento)

def ProcesoVentasTienda():
    ventasP = VentasPersistencia()
    ventas_departamento = ventasP.ventasPorTienda()
    print(ventas_departamento)

def ProcesoVentasAnio():
    ventasP = VentasPersistencia()
    ventas_departamento = ventasP.ventasPorAnio()
    print(ventas_departamento)