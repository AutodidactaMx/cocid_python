'''Creacion de arreglos'''
import numpy as np

arreglo = np.array([])
print("\n Arreglo vacio")
print(arreglo)

arreglo_agregado = np.append(arreglo, [7, 8, 9], axis=0)
print("\n Agregacion de datos")
print(arreglo_agregado)

arreglo_agregado = np.append(arreglo, [7, 8, 9], axis=0)
print("\n Agregacion de datos")
print(arreglo_agregado)


vacio = np.empty((3, 4), dtype=int)
print("\n Arreglo vacio")
print(vacio)

vacio = np.zeros((3, 4), dtype=int)
print("\n Arreglo valores ceros")
print(vacio)

vacio = np.ones((3, 4), dtype=int)
print("\n Arreglo valores unos")
print(vacio)


valor_unico = np.full([3, 3], 100, dtype=int)
print("Arreglo un valor unico")
print(valor_unico)


