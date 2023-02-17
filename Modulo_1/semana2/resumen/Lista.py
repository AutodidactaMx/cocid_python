'''La comprensión de listas, del inglés list comprehensions, 
es una funcionalidad que nos permite crear listas avanzadas 
en una misma línea de código. Esto se ve mucho mejor en la 
práctica, así que a lo largo de esta lección vamos a trabajar
 distintos ejemplos.'''
# Método tradicional
l = []
o=[1, 2, 3]
for i in o:
    l.append(i*2)
print(l)
# Con comprensión de listas
lista = [valor*2 for valor in o]
print(lista)
