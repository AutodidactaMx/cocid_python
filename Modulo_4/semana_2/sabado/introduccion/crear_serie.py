# Crear una Serie en Pandas:
import pandas as pd
import numpy as np

# Crear una Serie a partir de una lista de valores
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)