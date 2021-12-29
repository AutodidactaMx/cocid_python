import heapq

H = [21,3,45,78,3,5]
# Crea el heap

heapq.heapify(H)
print(H)

# Remplaza elemento
heapq.heapreplace(H,6)
print(H)
