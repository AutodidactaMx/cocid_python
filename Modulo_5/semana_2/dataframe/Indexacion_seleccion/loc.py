# importing pandas package
import pandas as pd
 
# Hacer un marco de datos desde un archivo csv
data = pd.read_csv("ventas.csv", index_col ="Tipo cliente")
 
# Recuperación de fila por método loc
primero = data.loc["Normal"]
segundo = data.loc["Member"]
 
 
print(primero, "\n\n\n", segundo)
