import array
  
# Inicializando el arreglo de valores de entero
arr = array.array('i', [1, 2, 3, 1, 5])
 
# Imprimiendo el arreglo
print ("Creando el arreglo es : ", end ="")
for i in range (0, 5):
    print (arr[i], end =" ")
 
print ("\r")
 
# Usando el pop para retirar el elemento
print ("El popped elemento es : ", end ="")
print (arr.pop(2))
 
# Imprimiendo el arreglo despues del pop
print ("El arreglo despues de popping es : ", end ="")
for i in range (0, 4):
    print (arr[i], end =" ")
 
print("\r")
 
# Usando remove() para eliminar el primer elemento
arr.remove(1)
 
# Imprimiendo despues de remover
print ("El arreglo despues de removing es : ", end ="")
for i in range (0, 3):
    print (arr[i], end =" ")