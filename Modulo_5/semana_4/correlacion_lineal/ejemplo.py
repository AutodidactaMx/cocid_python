import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo con dos variables
data = {'Variable1': [1, 2, 3, 4, 5],
        'Variable2': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# Calcular la correlación utilizando el método corr() de Pandas
correlation = df['Variable1'].corr(df['Variable2'])

# Calcular la covarianza utilizando el método cov() de Pandas
covariance = df['Variable1'].cov(df['Variable2'])

# Mostrar los resultados de correlación y covarianza
print("Correlación:", correlation)
print("Covarianza:", covariance)

# Graficar los datos
plt.plot(df['Variable1'], df['Variable2'], 'o-')
plt.xlabel('Variable1')
plt.ylabel('Variable2')
plt.title('Relación entre Variable1 y Variable2')
plt.grid(True)
plt.show()