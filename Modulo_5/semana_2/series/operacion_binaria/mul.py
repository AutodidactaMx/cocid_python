# importing pandas module  
import pandas as pd  
 
# Creando a series
data = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
 
# Creando a series
data1 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'c', 'd'])
 
print(data.mul(data1, fill_value=0))
