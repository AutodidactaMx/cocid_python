from dominio.objetos.persona import Persona
from dominio.objetos.empleado import Empleado


def solicitar_campos_persona() -> Persona:
    p = Persona()
    p.curp = input("Ingrese su curp : ")
    p.nombre = input("Ingrese su nombre : ")
    p.edad = input("Ingrese su edad : ")
    p.correo = input("Ingrese su correo : ")
    p.telefono = input("Ingrese su telefono : ")    
    return p


def solicitar_campos_empleado() -> Empleado:
    e = Empleado()
    e.curp = input("Ingrese su curp : ")
    e.nombre = input("Ingrese su nombre : ")
    e.edad = input("Ingrese su edad : ")
    e.correo = input("Ingrese su correo : ")
    e.telefono = input("Ingrese su telefono : ")
    e.sueldo_diario = int(input("Ingrese sueldo diario :"))
    e.bono_mensual = int(input("Ingrese bono mensual :"))
    return e
