from configuracion import LIBROS as libro
from configuracion import RUTA_LIBROS as ruta_libros


def seleccion(entrada):
    opcion = 0
    try:
        opcion = int(entrada)
        validar_opcion(opcion)
        print("#"*80)
        print("Has seleccionado", libro[opcion])
        print("#"*80, end="\n\n")
    except ValueError:
        print("Debe elegir una opcion numerica")
        exit()
    return opcion


def validar_opcion(opcion):    
    if(opcion < 1 or opcion > 3):
        print("Los siento no eligió un numero disponible")
        exit()
    elif(opcion == 5):
        print("Adios")
        exit()


def mostrar_cancion(opcion):
    with open((ruta_libros+libro[opcion]), "r") as f:
        line = f.readline()
        while line:
            line = f.readline()
            print(line)
    mensaje_mas_opcion()

def mensaje_mas_opcion():        
    print("#"*80)
    print("Selecciona un libro".center(80))
    print("#"*80, end="\n\n")