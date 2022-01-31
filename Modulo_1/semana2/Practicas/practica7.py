# Una pizzería vende dos categorías de pizzas: vegetarianas y no vegetarianas.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario el tipo de pizza vegetariana o no vegetariana,
# y en función de su respuesta le muestre un menú con los ingredientes disponibles
# para que elija. Solo se puede elegir un ingrediente especial, por defecto todas
# las pizzas llevan mozzarella y el tomate de ingrediente.
# Al final se debe mostrar por pantalla si el tipo de pizza  y sus ingredientes.

def menu_principal():
    print("Tipo de pizza")
    print(" 1 : vegetarianos")
    print(" 2 : no vegetarianos")


def ingredientes_vegetariana():
    ingredientes = {"1": "Pimiento", "2": "tofu"}
    print("Ingredientes vegetarianos:")
    print(" 1 : ", ingredientes.get("1"))
    print(" 2 : ", ingredientes.get("2"))
    return ingredientes.get(str(input("Cual tipo de ingredientes va querer ? : ")), " ")


def ingredientes_no_vegetariana():
    ingredientes = {"1": "Pepperoni", "2": "Jamón", "3": "Salmón"}
    print("Ingredientes no vegetarianos:")
    print(" 1 : ", ingredientes.get("1"))
    print(" 2 : ", ingredientes.get("2"))
    print(" 3 : ", ingredientes.get("3"))
    return ingredientes.get(str(input("Cual tipo de ingredientes va querer ? : ")), " ")


def ingredientes(respuesta):
    ingredientes = "Mozzarella, Tomate "
    if(respuesta == "1"):
        ingrediente = ingredientes_no_vegetariana()
    elif(respuesta == "2"):
        ingrediente = ingredientes_vegetariana()

    print(ingredientes + " y " + ingrediente)


menu_principal()
respuesta = input("Cual tipo de pizza va querer ? : ")
ingredientes(respuesta)
