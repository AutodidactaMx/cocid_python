import presentacion.solicitud_campos as solicitud
from persistencia.repositorio_persona import RepositorioPersona
from persistencia.repositorio_empleado import RepositorioEmpleado


def flujo(flujo: int) -> None:

    if(flujo == 1):
        print("Eligio insertar persona")
        insertar_persona()
    elif(flujo == 2):
        print("Eligio insertar empleado")
        insertar_empleado()
    elif(flujo == 3):
        print("Eligio consultar persona")
        consultar_persona()
    elif(flujo == 4):
        print("Eligio consultar empleado")
        consultar_empleados()
    else:
        print("Lo siento esa opcion no esta disponible")


def insertar_persona():
    persona = solicitud.solicitar_campos_persona()
    repo = RepositorioPersona()
    insertados = repo.insertar(persona)
    print(insertados, "Fue registrado satisfactoriamente")


def insertar_empleado():
    empleado = solicitud.solicitar_campos_empleado()
    repo = RepositorioEmpleado()
    insertados = repo.insertar(empleado)
    print(insertados, "Fue registrado satisfactoriamente")


def consultar_persona():
    repo = RepositorioPersona()
    lista: list = repo.consultar()
    print ("{:<15} {:<15} {:<15} {:<15}".format('Curp','Nombre','Edad','Correo','Telefono'))
    for persona in lista:
        print(persona)

def consultar_empleados():
    repo = RepositorioEmpleado()
    lista: list = repo.consultar()
    print ("{:<15} {:<15} {:<15} {:<15}".format('Curp','Nombre','Edad','Correo','Telefono','Puesto','Sueldo diario','Bono mensual'))
    for persona in lista:
        print(persona)


