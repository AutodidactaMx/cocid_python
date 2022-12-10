import pandas as pd
  
# Datos iniciales
data = [{'col_a': 2, 'col_b':3}, {'col_a': 10, 'col_b': 20, 'col_c': 30}]
  
# Lista de diccionario y lista de indices
df = pd.DataFrame(data, index =['primero', 'segundo'])
  
print(df)
