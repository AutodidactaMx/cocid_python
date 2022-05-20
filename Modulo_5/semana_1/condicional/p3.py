import numpy as np

a = np.arange(5, 30, 2)
print(a)
newA = a[(a > 5) & (a < 10)]
print(newA)
