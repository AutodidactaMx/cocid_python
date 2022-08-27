# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Escribir un programa que resuelva el siguiente descuento:
# Una paleteria vende dos categorías de paletas: sabor naturales y artificiales.
# Los ingredientes para cada tipo de paleta aparecen a continuación :
# ·         Sabor natural : Limon, Naranja, Fresa, Mango.
# ·         Sabor artificial : Chicle, Cafe, Oreon.
# Elabora un programa que pregunte al usuario si quiere una paleta de sabor
# natural o artificial, en función a la respuesta se debe mostrar el menú
# de sabores disponibles. Solo puede elegir un sabor, por defecto todas las
# paletas incluyen servilleta. Al final de la elección se debe mostrar
# la paleta del sabor seleccionado y lo que incluye por defecto
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def menu_principal():
    print("Tipo de paletas")
    print(" 1 : Sabor natural")
    print(" 2 : Sabor artificial")


def sabor_natural():
    sabor = {"1": "Limon", "2": "Naranja", "3": "Fresa", "4": "Mango"}
    print("Sabor natural:")
    print(" 1 : ", sabor.get("1"))
    print(" 2 : ", sabor.get("2"))
    print(" 3 : ", sabor.get("3"))
    print(" 4 : ", sabor.get("4"))
    return sabor.get(str(input("Cual tipo de sabor va querer ? : ")), " ")


def sabor_artificial():
    sabor = {"1": "Chicle", "2": "Cafe", "3": "Oreon"}
    print("Sabor artificial:")
    print(" 1 : ", sabor.get("1"))
    print(" 2 : ", sabor.get("2"))
    print(" 3 : ", sabor.get("3"))
    return sabor.get(str(input("Cual tipo de sabor va querer ? : ")), " ")


def seleccion(respuesta):
    incluye = "servilleta "
    if (respuesta == "1"):
        sabor = sabor_natural()
    elif (respuesta == "2"):
        sabor = sabor_artificial()

    print(incluye + " y " + sabor)


while (True):
    menu_principal()
    respuesta = input("Cual tipo de paleta va querer ? : ")
    seleccion(respuesta)
    vasSalir = input("Quieres nuevo pedido ? opcion(si,no): ")
    if (vasSalir == "no"):
        break
