#Cargar datos desde un archivo CSV en Pandas:
import pandas as pd

# Cargar datos desde un archivo CSV en un DataFrame
df = pd.read_csv('london_merged.csv')
print(df)