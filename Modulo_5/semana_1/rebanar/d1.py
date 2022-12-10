import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
b = a1[1:4]

b[1] = 10
print(b)  # [2, 10, 4]
print(a1) # [1, 2, 10, 4, 5]

