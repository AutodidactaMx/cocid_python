from configuracion import CANCIONES as canciones
from configuracion import RUTA_CANCIONES as ruta_libros


def seleccion(entrada):
    opcion = 0
    try:
        opcion = int(entrada)
        verificar_opcion(opcion)
        print("#"*80)
        print("Has seleccionado", canciones[opcion])
        print("#"*80, end="\n\n")
    except ValueError:
        print("Debe elegir un numero una opcion numerica")
        exit()
    return opcion


def verificar_opcion(opcion):
    if(opcion < 0 or opcion > 5):
        print("Los siento no eligió una opción disponible")
        exit()
    elif(opcion == 5):
        print("Adios")
        exit()


def mostrar_cancion(opcion):
    with open((ruta_libros+canciones[opcion]), "r") as f:
        line = f.readline()
        while line:
            line = f.readline()
            print(line)
