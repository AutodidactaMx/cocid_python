import numpy as np

a = np.arange(6).reshape(2,3) 
print(a)
print(np.argmin(a))
print(np.argmin(a, axis=0))
print(np.argmin(a, axis=1))
