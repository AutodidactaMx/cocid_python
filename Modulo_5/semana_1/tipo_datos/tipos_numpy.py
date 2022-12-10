'''
Se establece asignando uno de los tipos de Numpy 
(np.int, np.float, np.str, np.bool, etc.) al argumento dtype.
•	np.int8: (1 byte) - Para enteros entre -128 y 127.
•	np.int16: (2 bytes) - Para enteros entre -32768 y 32767.
•	np.int32: (4 bytes) - Para enteros entre -2147483648 y 2147483647.
•	np.int64: (8 bytes) - Para números enteros entre -9223372036854775808 y 9223372036854775807.
'''
import numpy as np
a = np.array([0, 0, 1, 1, 0], dtype=np.bool8)
print(a)  # [0 0 1 1 0]
print(a.dtype)  # dtype('int64')
