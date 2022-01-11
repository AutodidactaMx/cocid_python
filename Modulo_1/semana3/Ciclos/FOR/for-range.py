# Imprimir rango de 10 números
for i in range(10):
    print(i, end=" ")
print()
 
# Usando un rango por iterar
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end=" ")
print()
 
# Realizar la suma de los primeros 10 números
sum = 0
for i in range(1, 10):
    sum = sum + i
print("Suma los primero 10 números :", sum)