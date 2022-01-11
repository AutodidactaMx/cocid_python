import array as arr
 
# Creando lista
l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
 
a = arr.array('i', l)
print("Inicializar arreglo: ")
for i in (a):
    print(i, end =" ")
 
# Imprime el elemento del rango
# Usando la operacion de rebanada
Sliced_array = a[3:8]
print("\nRebana de elemento en rango 3-8: ")
print(Sliced_array)
 
# Imprimiendo el elemendo iniciado de una posicionhasta el final
Sliced_array = a[5:]
print("\nElmento rebanada de 5th elemento hasta el final: ")
print(Sliced_array)
 
# Imprimiendo los elementos del comienzo al final
Sliced_array = a[:]
print("\nImprimiendo todos los elementos usando la rebanadas: ")
print(Sliced_array)