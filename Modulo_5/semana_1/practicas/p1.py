import numpy as np
   
# 1D array
arr = [25,28,30,30,35,35,36,37,37,38,40,40,40,40,40,40,41,43,48,50]
res = np.percentile(arr, 50)
print(res)
