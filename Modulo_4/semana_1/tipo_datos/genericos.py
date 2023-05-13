import numpy as np

a = np.array([0, 0, 1, 1, 0], dtype=str)  # Entero (int)
print(a)  # [0 0 1 1 0]
print(a.dtype)  # dtype('int32')

a = np.array([0.1, 0.4, 0.9], dtype=float)  # Flotante (float)
print(a)  # [0.1 0.4 0.9]
print(a.dtype)  # dtype('float64')

a = np.array(['0', '0', '1', '1', '0'], dtype=str)  # Unicode (str)
print(a)  # ['0' '0' '1' '1' '0']
print(a.dtype)  # dtype('<U1')

a = np.array([0, 0, 1, 1, 0], dtype=bool)  # Booleano (bool)
print(a)  # [False False  True  True False]
print(a.dtype)  # dtype('bool')
