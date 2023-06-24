import math
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np

sns.set()

# Cargar los datos desde un archivo CSV
df = pd.read_csv('./data/Bolsa_de_Valores.csv')

# Extraer las variables independiente (x) y dependiente (y)
x = df['tasa_de_interes'].values.reshape(-1, 1)
y = df['precio_de_índice_de_acciones'].values.reshape(-1, 1)

# Calcular el coeficiente de correlación
corr_matrix = np.corrcoef(x.flatten(), y.flatten())
corr_coefficient = corr_matrix[0, 1]

# Crear una instancia del modelo de regresión lineal
modelo = LinearRegression()

# Ajustar el modelo a los datos de entrenamiento
modelo.fit(x, y)

# Imprimir los coeficientes de la línea de regresión
print("Intersección u ordenante (β0):", modelo.intercept_)
print("Pendiente (β1) Coeficiente:", modelo.coef_)

# Predecir los valores de y utilizando el modelo
y_pred = modelo.predict(x)

# Graficar los puntos de datos y la línea de regresión
plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.xlabel('Tasa de Interés')
plt.ylabel('Precio del Índice de Acciones')
plt.title('Regresión Lineal')

# Datos de entrada para la predicción
entrada = [[1.5], [2.9], [2.10]]

# Realizar la predicción utilizando el modelo entrenado
prediccion_modelo = modelo.predict(entrada)

# Calcular el coeficiente de determinación (R^2)
r2 = r2_score(y, y_pred)
print('Coeficiente de Determinacion Estadístico R2:', r2)
print('Coeficiente de correlación:', corr_coefficient )
print("Predicción de precio del índice de acciones:", prediccion_modelo)

# Graficar los puntos de entrada y las predicciones
plt.scatter(entrada, prediccion_modelo, color="red")
plt.plot(entrada, prediccion_modelo, color="black")

# Mostrar la gráfica
plt.show()