# Obtenga la entrada del usuario usando input ("Escribe elnombre de una fruta:").
# Si una fruta no existe en la lista, agregue la fruta
# a la lista e imprima la lista modificada. Si la fruta existe print('Esa fruta ya existe en la lista')
# La siguiente lista contiene algunas frutas:
# fruits = ['platano', 'naranja', 'mango', 'limon']
frutas = ['platano', 'naranja', 'mango', 'limon']
fruta = input("Escribe el nombre de una fruta: ")
if(not(fruta.lower() in frutas)):
    frutas.append(fruta)
    print("Agregaste una nueva fruta a la lista :")
    print(frutas)
else:
    print("Esa fruta ya existe en la lista")
