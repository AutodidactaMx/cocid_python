import heapq

H = [21,1,45,78,3,5]
# Convertir en Pila
heapq.heapify(H)
print(H)

#  Agregar elemento
heapq.heappush(H,8)
print(H)