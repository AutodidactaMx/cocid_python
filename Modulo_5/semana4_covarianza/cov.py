import numpy as np 
import matplotlib.pyplot as plt
'''
Seaborn es una librería de visualización de datos para Python desarrollada sobre matplotlib. 
Ofrece una interfaz de alto nivel para la creación de atractivas gráficas.
'''
import seaborn as sns
'''
Scikit-learn es una biblioteca de Python de código abierto para el aprendizaje automático. 
La biblioteca soporta algoritmos de última generación como KNN, XGBoost, bosque aleatorio, SVM entre otros. 
'''
'''
Estandarización: StandardScaler estandariza una característica restando la media 
y luego escalando a la varianza de la unidad. 
La varianza unitaria significa dividir todos los valores por la desviación estándar. 
La estandarización puede ser útil en los casos en que los datos siguen una distribución
gaussiana (o distribución normal). Sin embargo, esto no tiene por qué ser necesariamente cierto.
Además, a diferencia de la normalización, la estandarización no tiene un rango límite. Por lo tanto,
incluso si tiene valores atípicos en sus datos, no se verán afectados por la estandarización.
'''
from sklearn.preprocessing import StandardScaler

plt.show()
'''
Se carga un conjuntos de datos proporcionados por seaborn de una planta iris
'''
iris = sns.load_dataset('iris')
'''
Usamos el metodo pairplot para  visualizar dos variables y la relacion 
que tienen
'''
sns.pairplot(iris)

'''
Graficacion clasificada por especie
'''
sns.pairplot(iris, hue = 'species')

'''
Normalizar la data por medio de StandardScaler el cual aplica escalamiento z-score
Seleccionamos las variables dee tipo numerico sepal_length, sepal_width, petal_length, petal_width
'''
scaler = StandardScaler()
scaled = scaler.fit_transform(
    iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
)
'''
Transponer los datos escalado
'''
scaledT = scaled.T 
print(scaledT)
'''
Calculamos la covarianza  de las variables calculadas en el Data frame
'''
covariance_matrix = np.cov(scaledT)
print(covariance_matrix)
'''
Graficacion visual de la matriz de correlación
'''

plt.figure(figsize=(10,10))
sns.set(font_scale=1.5)
hm = sns.heatmap(covariance_matrix,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size': 12},
                 yticklabels=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
                 xticklabels=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
plt.show()
 