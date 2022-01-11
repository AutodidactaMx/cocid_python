import heapq

H = [21,1,45,78,3,5]
# Crear el heap

heapq.heapify(H)
print(H)

# Remueve elementos del heap
heapq.heappop(H)

print(H)

