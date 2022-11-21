# importing pandas as pd
import pandas as pd
# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'Primero Puntaje':[100, 90, np.nan, 95],
        'Segundo Puntaje': [30, 45, 56, np.nan],
        'Tercero Puntaje':[np.nan, 40, 80, 98]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
 
# filling missing value using fillna()  
print(df.fillna(100))
