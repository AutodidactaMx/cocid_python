import numpy as np

print("Generador de datos por rango en salto")
print(np.arange(1,20,2))

print("Generador de datos en un rango acomodado en N elementos")
print(np.linspace(1, 10, 20,dtype = float))

print("Generador de datos aleatorios por niveles")
print(np.random.rand(10,2))

print("Generador de datos aleatorios en un rango de valores enteros con n cantidad de elementos")
print(np.random.randint(15, 20, 10))

print("Generador de datos aleatorios en un rango de valores flotantes con n cantidad de elementos")
print(np.random.uniform(15, 20, 10))

