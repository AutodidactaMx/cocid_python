# -----------------------------------------------------------
# Programa para construir un arbol por medio de decisiones
# de entrada :
# Tipo de arbol
# Tamaño del arbol
# -----------------------------------------------------------
import constructor_arboles as ca


def solicitar_datos():
    print("-"*30)
    print("Tienda de arboles".center(30))
    print("-"*30)
    print("Tipos : ")
    print("1) Tipo pino ")
    print("2) Arbol común")
    tipo_arbol_string = input("Que tipo de arbol va necesitar? : ")
    if(tipo_arbol_string):
        tipo_arbol = int(tipo_arbol_string)
    else:
        print("Lo siento debio de elegir una opcion")
        exit()
    print("Tamaños : ")
    print("1) Grande ")
    print("2) Mediano")
    print("Si no elige por defecto es pequeño")
    tamanio_arbol_string = input("Tamaño de arbol : ")
    tamanio_arbol = int(
        tamanio_arbol_string) if tamanio_arbol_string != "" else 0
    return {"tamanio": tamanio_arbol, "tipo": tipo_arbol}


def construir_arbol(caracteristicas):
    tamanio = obtener_tamanio(caracteristicas["tamanio"])

    if(caracteristicas["tipo"] == 1):
        ca.pino(tamanio)
    elif(caracteristicas["tipo"] == 2):
        ca.arbol_comun(tamanio)
    else:
        print("Eligio una opcion fuera del menu")


def obtener_tamanio(opcion):
    if(opcion == 1):
        tamanio = 20
    elif(opcion == 2):
        tamanio = 10
    else:
        tamanio = 5
    return tamanio


caracteristicas = solicitar_datos()
construir_arbol(caracteristicas)
