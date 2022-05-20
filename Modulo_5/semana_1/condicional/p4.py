import numpy as np

a = np.arange(5, 30, 2)
print(a)
newA = a[a%3==0]

print(newA)
