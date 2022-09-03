'''
Funciones de Heapq
Heapify: es la función principal que se utiliza para 
convertir una lista regular en un montón. Esto significa 
que el número más pequeño de la lista se desplaza hacia el primer lugar, 
es decir, la posición del índice [0]. Al mismo tiempo, esta función no ordena 
todos los demás elementos de una lista.
Heappop: esta es la función pop() de la pila que se usa
para sacar el elemento de la lista. Y en la situación de heappop, 
se devuelve el artículo más pequeño.
Heappush: al igual que la función push(), esta función agrega el nuevo 
elemento en un montón y no provoca ningún cambio en la secuencia.
Heapreplace: el elemento más pequeño de la lista se reemplaza por el 
nuevo elemento proporcionado por esta función.
'''

# Importando "heapq" para implementar heap queue
import heapq
 
# Inicializando lista
li = [5, 7, 9, 1, 3]
 
# Usando heapify para convertir una lista en heap
heapq.heapify(li)
 
# Imprimiendo un heap
print("Creado el heap : ", end="")
print(list(li))
 
# Usando heappush() para colocar un elemento dentro de un heap
# colcar 4
heapq.heappush(li, 4)
 
# Usando el heappop() para extraer el elemanto mas pequeño
print("El elemento es : ", end="")
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))