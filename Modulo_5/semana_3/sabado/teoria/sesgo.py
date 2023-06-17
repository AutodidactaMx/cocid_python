import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = {'A': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]}
df = pd.DataFrame(data)

# Calcular el sesgo
sesgo = df['A'].skew()
print("Sesgo:", sesgo)

# Visualizar la distribución
plt.hist(df['A'], bins=5)
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución de datos')
plt.show()
