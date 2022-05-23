import pandas as pd
 
# hacer un dataframe desde un archivo csv
data = pd.read_csv("ventas.csv", index_col ="Id Factura")
 
# recuperando filas por el método iloc
row2 = data.iloc[3] 
 
print(row2)
