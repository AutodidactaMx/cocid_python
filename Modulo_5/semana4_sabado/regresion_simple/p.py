import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import r2_score

'''
Asignamos la configuracion de el estilo de graficas de seaborn
mejor visualizacion
'''
sns.set()
'''
Cargamos nuestra información de ingreso
'''
df = pd.read_csv('./data/Bolsa_de_Valores.csv')
'''
Convertimos series de pandas en vectores de numpy para colocarlo en el modelo de regresión
'''
x = df['Interest_Rate'].values.reshape(-1, 1) ### Tasa de interés
y = df['Stock_Index_Price'].values.reshape(-1, 1) ### Precio_de_índice_de_acciones

'''
Verificamos la forma de nuestros vestores
'''
print(y.shape)
print(x.shape)

'''
Creo un modelo de regresión lineal
'''
modelo = linear_model.LinearRegression()
'''
Se entrena el modelo con los datos (X,Y)
'''
modelo.fit(x, y)  
'''
Una vez entrenado el modelo podemos traer los valores de coeficientes β1 y β0
'''
print("Interseccion (β0)", modelo.intercept_)
print("Pendiente (β1) Coeficiente", modelo.coef_)
'''
Al tener nuestro modelo preparado ahora procedemos hacer predicción 
de los valores con apoyo de la variable independiente x aplicado al modelo
para obtener valores de la variable dependiente Y
'''
y_pred = modelo.predict(x)

'''
Graficamos los puntos de β1 interceptor posteriormente
agregamos una línea con los valores Y a predecir con 
referencia al eje de X 
'''
plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
'''
Podemos ver el valor a predecir de las variables que necesitemos
en este caso usaremos el siguiente arreglo de salario a predecir
'''
entrada = [[1.0],[2.9],[2.10]]
prediccion_modelo = modelo.predict(entrada)
print("Prediccion de salario : ",prediccion_modelo)
'''
Graficamos con puntos la entrada de salario con respecto al salario
con una gráfica de línea y de puntos
''' 
print(prediccion_modelo)
plt.scatter(entrada, prediccion_modelo, color="red")
plt.plot(entrada, prediccion_modelo, color="black")

plt.show()

'''
Coeficiente de determinación R2
El coeficiente de determinación R2 determina la calidad del modelo para replicar los resultados, 
y la proporción de variación de los resultados que puede explicarse por el modelo
r2 =  ssr(Variabilidad explicada por la regresión) / sst(Variabilidad total conjunto de datos)
r2 = 0  no explica la variabilidad  de los datos
r2 = 1  Explica toda la variabilidad de los datos
'''    
r2 =  r2_score(y, y_pred)
print('Estadístico R2: ' , r2)