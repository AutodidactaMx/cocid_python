from persistencia.persona import RepositorioPersona

def crear_tabla():    
    return RepositorioPersona().contruir_tabla() 

def eliminar_tabla():    
    return RepositorioPersona().eliminar_tabla()
    
def eliminar_persona(curp):    
    return RepositorioPersona().eliminar(curp) 

def insertar_persona(persona):    
    return RepositorioPersona().insertar(persona)    

def consultar_persona():    
    return RepositorioPersona().consultar()     

def verificar_tabla():    
    return RepositorioPersona().verificar_tabla()     