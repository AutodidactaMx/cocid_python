import presentacion.solicitud_campos as solicitud
from persistencia.repositorio_persona import RepositorioPersona
from persistencia.repositorio_empleado import RepositorioEmpleado


def flujo(flujo: int) -> None:

    if(flujo == 1):
        insertar_persona()
    elif(flujo == 2):
        insertar_empleado()
    elif(flujo == 3):
        pass
    elif(flujo == 4):
        pass
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
