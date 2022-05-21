import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

print("Union")
print(np.union1d(arr1, arr2))

print("Intercepcion")
print(np.intersect1d(arr1, arr2,assume_unique=True))

print("Diferencia izquierda")
print( np.setdiff1d(arr1,arr2 , assume_unique=True))

print("Diferencia derecha")
print( np.setdiff1d(arr2,arr1 , assume_unique=True))

print("Diferencia Simetricas")
print(np.setxor1d(arr1, arr2,  assume_unique=True))