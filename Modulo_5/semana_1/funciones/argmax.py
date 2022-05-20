import numpy as np

a = np.array([
        [0,1,2],
        [3,4,5]
    ])
print(a)
print(np.argmax(a))
print(np.argmax(a, axis=0))
print(np.argmax(a, axis=1))
