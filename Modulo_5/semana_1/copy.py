import numpy as np

x = np.array([1, 2, 3])
y = x
z = np.copy(x)
x[0] = 10
print(x[0] == y[0])

print(x[0] == z[0])
print("x",x)
print("y",y)
print("z",z)
