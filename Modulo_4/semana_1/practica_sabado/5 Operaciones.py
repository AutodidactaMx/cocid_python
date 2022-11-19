import numpy as np
a = np.array([0,10, 10, 30, 110, 20], dtype=np.int32)  
print("Suma")
print(a * 2)
print("division")
print(a / 2)  

print("Condicionales")  
print(a[(a > 5) & (a < 100)])

print("Acumulamiento")
print(a.cumsum())

a = np.array([[1,10, 10, 30, 110, 20],[1,10, 10, 30, 110, 20]], dtype=np.int32)  

print("Explicacion")
print(np.where([True, False, True], [1,2,3], [4, 5, 6]))

print("Where")
print(np.where((a > 5) & (a < 11), a, a+1000))


(unique, counts) = np.unique(a, return_counts=True)
print(f'Únicos:     {unique}')
print(f'Frecuencia: {counts}')