import pandas as pd
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

sns.set()
df = pd.read_csv('./regresion_simple/data/Bolsa_de_Valores.csv')
x = df['tasa_de_interes'].values.reshape(-1, 1)
y = df['precio_de_índice_de_acciones'].values.reshape(-1, 1)

modelo = linear_model.LinearRegression()
modelo.fit(x, y)  
print("Interseccion (β0)", modelo.intercept_)
print("Pendiente (β1) Coeficiente", modelo.coef_)

y_pred = modelo.predict(x)

plt.scatter(x, y)
plt.plot(x, y_pred, color='red')

entrada = [[1.5],[2.9],[2.10]]
prediccion_modelo = modelo.predict(entrada)

r2 =  r2_score(y, y_pred)
print('Estadístico R2: ' , r2)
print("Prediccion de salario : ",prediccion_modelo)
plt.scatter(entrada, prediccion_modelo, color="red")
plt.plot(entrada, prediccion_modelo, color="black")

plt.show()

