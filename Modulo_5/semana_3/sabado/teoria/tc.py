import pandas as pd

# Crear un DataFrame de ejemplo
data = {'A': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Calcular la media
media = df['A'].mean()
print("Media:", media)
# Calcular la mediana
mediana = df['A'].median()
print("Mediana:", mediana)
# Calcular la moda
moda = df['A'].mode()
print("Moda:", moda)