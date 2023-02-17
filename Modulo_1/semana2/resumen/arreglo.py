'''https://docs.python.org/es/3/library/array.html
Este modulo define un tipo de objeto que representa un arreglo de valores básicos: 
caracteres, números enteros y de punto flotante. Los arreglos son tipos de secuencias 
que se comportan de forma similar a las listas, a excepción que el tipo de objeto 
guardado es definido.
'''
import array as arr
# creando un arreglo con tipo flotante
a = arr.array('d', [10.2, 23.22, 44.43])
# Imprimiendo
print ("Arreglo float: ", end =" ")
for i in range (0, 3):
    print (a[i], end =" ")

'''
Code	C Type	Python Type	Min bytes
'b'	signed char	int	1
'B'	unsigned char	int	1
'u'	Py_UNICODE	Unicode	2
'h'	signed short	int	2
'H'	unsigned short	int	2
'i'	signed int	int	2
'I'	unsigned int	int	2
'l'	signed long	int	4
'L'	unsigned long	int	4
'f'	float	float	4
'd'	double	float	8
'''
a = arr.array('u', ['d','a'])
for i in range (0, 2):
    print (a[i], end =" ")