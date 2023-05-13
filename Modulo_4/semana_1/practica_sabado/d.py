import numpy as np
a = np.array([0,10, 10, 30, 110, 20], dtype=np.int32)  

print("Explicacion")
print(np.where([True, False, True], [1,2,3], [4, 5, 6]))

print("Where")
print(np.where((a > 5) & (a < 11), a, a+1000))

