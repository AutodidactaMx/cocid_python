# importing pandas as pd
import pandas as pd
  
# diccionario de listas
dict = {'nombre':["luis", "marcos", "marta", "pedro"],
        'grado': ["LIC", "MTA", "DOC", "LIC"],
        'puntaje':[90, 40, 80, 98]}
 
# creando un marco de datos a partir de un diccionario
df = pd.DataFrame(dict)
 
# iterando sobre filas usando la función iterrows()
for i, j in df.iterrows():
    print("Indice:",i, "Fila:" , j)
    print()
