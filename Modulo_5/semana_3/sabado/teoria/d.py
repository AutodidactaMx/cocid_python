import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = {'X': [10, 15, 12, 8, 20]}
df = pd.DataFrame(data)

# Calcular diferentes medidas de dispersión
rango = df['X'].max() - df['X'].min()
desviacion_estandar = df['X'].std()
varianza = df['X'].var()

# Imprimir los resultados
print("Rango:", rango)
print("Desviación estándar:", desviacion_estandar)
print("Varianza:", varianza)