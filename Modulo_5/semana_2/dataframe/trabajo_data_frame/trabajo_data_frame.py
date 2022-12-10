# importing pandas as pd
import pandas as pd
# importing numpy as np
import numpy as np
 
# diccionario de listas
dict = {'Primero Puntaje':[100, 90, np.nan, 95],
        'Segundo Puntaje': [30, 45, 56, np.nan],
        'Tercero Puntaje':[np.nan, 40, 80, 98]}
 
# creando un marco de datos de la lista
df = pd.DataFrame(dict)
 
# usando la función isnull() 
print(df.isnull())
