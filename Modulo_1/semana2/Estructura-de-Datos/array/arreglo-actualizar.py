import array
 
# Inicializando con los valores de tipo enero
arr = array.array('i', [1, 2, 3, 1, 2, 5])
 
# Imprimiendo el arreglo
print ("Arreglo antes de la actualización  : ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")
 
print ("\r")
 
# Actualizando el elemento arreglado
arr[2] = 6
print("Arreglo despues de la actualización  : ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")
print()
 
# Actualizando el elemento arreglado
arr[4] = 8
print("Arreglo despues de la actualización : ", end ="")
for i in range (0, 6):
    print (arr[i], end =" ")