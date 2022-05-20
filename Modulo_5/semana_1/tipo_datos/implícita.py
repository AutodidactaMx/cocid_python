import numpy as np

a = np.array([0, 0, 1, 1, 0])  
print(a)  # [0 0 1 1 0]
print(a.dtype)  # dtype('int32')

a = np.array([0.1, 0.4, 1.0, 1.5, 0.9])  
print(a)  # [0.1 0.4 1.  1.5 0.9]
print(a.dtype)  # dtype('float64')

a = np.array(['0', '0', '1', '1', '0'])  
print(a)  # ['0' '0' '1' '1' '0']
print(a.dtype)  # dtype('<U1')

a = np.array([False, False, True, True, False]) 
print(a)  # [False False  True  True False]
print(a.dtype)  # dtype('bool')
