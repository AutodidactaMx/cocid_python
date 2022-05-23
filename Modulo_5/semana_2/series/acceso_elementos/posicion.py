import pandas as pd
import numpy as np
 
# Creando un arreglo simple
data = np.array(['a','b','c','d','f','g', 'h','i','j','k','l','m','n'])
ser = pd.Series(data)

#Recuperando los primeros elemento
print(ser[0])
print()
print(ser[:5])
print()
print(ser[5:])
