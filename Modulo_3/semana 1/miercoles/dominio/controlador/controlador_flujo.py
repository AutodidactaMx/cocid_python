from persistencia.repositorio_persona import RepositorioPersona
from persistencia.repositorio_empleado import RepositorioEmpleado



def insertar_persona(persona):    
    return RepositorioPersona().insertar(persona)    