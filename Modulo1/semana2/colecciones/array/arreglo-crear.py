import array as arr
 
# Creando el arreglo con tipo entero
a = arr.array('i', [1, 2, 3])
 
# imprimiendo
print ("Arreglo entero : ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")
print()
 
# creando un arreglo con tipo flotante
b = arr.array('d', [10.2, 23.22, 44.43])
 
# imprimiendo
print ("Arreglo float: ", end =" ")
for i in range (0, 3):
    print (b[i], end =" ")