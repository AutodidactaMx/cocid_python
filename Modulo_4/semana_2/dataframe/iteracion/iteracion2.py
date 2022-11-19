# importing pandas as pd
import pandas as pd
   
# Listas
dict = {'nombre':["luis", "marcos", "marta", "pedro"],
        'grado': ["LIC", "MTA", "DOC", "LIC"],
        'puntaje':[90, 40, 80, 98]}
  
# Creando un marco de datos a partir de un diccionario
df = pd.DataFrame(dict)
 
# creando una lista de columnas de marcos de datos
columns = list(df)
 
for i in columns:
    # imprimiendo el tercer elemento de la columna
    print (df[i][2])
