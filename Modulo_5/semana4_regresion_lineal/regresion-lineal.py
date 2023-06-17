import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import r2_score
sns.set()

df = pd.read_csv('ingreso.csv')

x = df['horas'].values.reshape(-1, 1) ### El promedio de trabajo de las personas 
y = df['ingreso'].values.reshape(-1, 1) ### Salario de las persona


modelo = linear_model.LinearRegression()
modelo.fit(x, y)  
print("Interseccion (β0)", modelo.intercept_)
print("Pendiente (β1)", modelo.coef_)

y_pred = modelo.predict(x)
plt.plot(x, y_pred, color='red')
plt.scatter(x, y)


entrada = [[40],[43],[44]]
prediccion_modelo = modelo.predict(entrada)

r2 =  r2_score(y, y_pred)
print('Estadístico R2: ' , r2)


plt.scatter(entrada, prediccion_modelo, color="red")
plt.plot(entrada, prediccion_modelo, color="black")
plt.show()

