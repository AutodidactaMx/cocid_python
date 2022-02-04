# -----------------------------------------------------------
# Funciones para la creación de una figura de arbol
# -----------------------------------------------------------

def __figura_rectangular(longitud):
    for i in range(1, longitud, 2):
        print(('*'*longitud))

def __figura_pino(longitud):
    for i in range(1, longitud, 2):
        print(('*'*i).center(longitud))

def __tronco_arbol(longitud):    
    for leg in range(2):
        print(('|||').center(longitud))
        
def __base_arbol(longitud):    
    print(('\___/').center(longitud))

def arbol_comun(longitud):    
    __figura_rectangular(longitud)
    __tronco_arbol(longitud)
    __base_arbol(longitud)

def pino(longitud):
    __figura_pino(longitud)
    __tronco_arbol(longitud)
    __base_arbol(longitud)
    
