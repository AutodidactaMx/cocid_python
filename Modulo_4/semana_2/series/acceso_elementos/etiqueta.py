# import pandas and numpy 
import pandas as pd
import numpy as np
 
# Creando simple arreglo
data = np.array(['a','b','c','d','e','f', 'g','h','i','j','k','l','m'])
ser = pd.Series(data,index=["A","11","12","13","14","15","16","17","18","19","20","21","22"])
  
print(ser["15":])

