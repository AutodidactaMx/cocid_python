import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('./clientes.csv')
df.head()
'''
Es una función de la biblioteca Seaborn en Python que se utiliza para trazar 
un histograma y una estimación de densidad de kernel (KDE) de una distribución 
univariable de datos. Combina la visualización del histograma y la función de 
densidad de probabilidad estimada para proporcionar una representación gráfica 
completa de la distribución de los datos.
'''
'''
plt.figure(1 , figsize = (15 , 6))
n = 0 
for x in ['edad' , 'ingresos_anuales_(k$)' , 'puntuacion_de_gastos_(1-100)']:
    n += 1
    plt.subplot(1 , 3 , n)
    plt.subplots_adjust(hspace = 0.5 , wspace = 0.5)
    sns.distplot(df[x] , bins = 15)
    plt.title('Distplot of {}'.format(x))
'''
'''
Es una función de la biblioteca Seaborn en Python que se 
utiliza para trazar un conjunto de gráficos de dispersión 
entre múltiples variables en un solo gráfico. 
Proporciona una forma rápida y conveniente de explorar las relaciones 
entre pares de variables en un conjunto de datos.

sns.pairplot(df, vars = ['puntuacion_de_gastos_(1-100)', 'ingresos_anuales_(k$)', 'edad'], hue = "genero")

plt.figure(1 , figsize = (15 , 7))
plt.title('Scatter plot de edad puntuacion_de_gastos', fontsize = 20)
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.scatter( x = 'edad', y = 'puntuacion_de_gastos_(1-100)', data = df, s = 100)
plt.show()
'''

X1 = df[['Age' , 'Spending Score (1-100)']].iloc[: , :].values
inertia = []
for n in range(1 , 15):
    algorithm = (KMeans(n_clusters = n ,init='k-means++', n_init = 10 ,max_iter=300, 
                        tol=0.0001,  random_state= 111  , algorithm='elkan') )
    algorithm.fit(X1)
    inertia.append(algorithm.inertia_)

plt.figure(1 , figsize = (15 ,6))
plt.plot(np.arange(1 , 15) , inertia , 'o')
plt.plot(np.arange(1 , 15) , inertia , '-' , alpha = 0.5)
plt.xlabel('Number of Clusters') , plt.ylabel('Inertia')
plt.show()





'''
X1 = df[['edad' , 'puntuacion_de_gastos_(1-100)']].iloc[: , :].values

algorithm = (KMeans(n_clusters = 4 ))
algorithm.fit(X1)
labels1 = algorithm.labels_
centroids1 = algorithm.cluster_centers_


plt.figure(1 , figsize = (15 , 7) )
plt.scatter( x = 'edad', y = 'puntuacion_de_gastos_(1-100)', data = df, c = labels1, s = 100)
plt.scatter(x = centroids1[: , 0] , y =  centroids1[: , 1] , s = 300 , c = 'red' , alpha = 0.5)
plt.ylabel('puntuacion_de_gastos_(1-100)') , plt.xlabel('edad')


plt.show()
'''