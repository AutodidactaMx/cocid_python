# Eleccion de canciones por rocola
import configuracion as config


def menu_canciones():
    print("1. Get Back")
    print("2. Hey Jude")
    print("3. Let It Be")
    print("4. She LovesYou")
    print("5. Salir", end="\n\n")


def cadena_entrada():
    entrada = input("Opcion :")
    opcion = 0
    try:
        opcion = int(entrada)
        verificar_opcion(opcion)
        print("#"*80)
        print("Has seleccionado",
              config.CANCIONES[opcion], ". Te mostramos la letra a continuación:")
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
    with open((config.RUTA_CANCIONES+config.CANCIONES[opcion]), "r") as f:
        line = f.readline()
        while line:
            line = f.readline()
            print(line)


def presentacion():
    print("#"*80)
    print("Bienvenido, por favor, selecciona una canción de este top de 4 canciones ".center(80))
    print("#"*80, end="\n\n")


presentacion()
while True:
    menu_canciones()
    opcion = cadena_entrada()
    mostrar_cancion(opcion)
