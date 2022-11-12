import numpy as np
  
arr1 = np.array([[2, 4], [6, 8]])
arr2 = np.array([[3, 5], [7, 9]])
  
concat = np.concatenate((arr1, arr2), axis = 1)
  
print (concat)
