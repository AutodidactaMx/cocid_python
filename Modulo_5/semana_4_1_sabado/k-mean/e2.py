import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('./clientes.csv')
df.head()
X1 = df[['edad' , 'puntuacion_de_gastos_(1-100)']].iloc[: , :].values

inertia = []
for n in range(1 , 15):
    algorithm = (KMeans(n_clusters = n) )
    algorithm.fit(X1)
    inertia.append(algorithm.inertia_)

plt.figure(1 , figsize = (15 ,6))
plt.plot(np.arange(1 , 15) , inertia , 'o')
plt.plot(np.arange(1 , 15) , inertia , '-' , alpha = 0.5)
plt.xlabel('Numero de Clusters') , plt.ylabel('Inercia')
plt.show()

algorithm = (KMeans(n_clusters = 4 ))
algorithm.fit(X1)
labels1 = algorithm.labels_
centroids1 = algorithm.cluster_centers_

plt.figure(1 , figsize = (15 , 7) )
plt.scatter( x = 'edad', y = 'puntuacion_de_gastos_(1-100)', data = df, c = labels1, s = 100)
plt.scatter(x = centroids1[: , 0] , y =  centroids1[: , 1] , s = 300 , c = 'red' , alpha = 0.5)
plt.ylabel('puntuacion_de_gastos_(1-100)') , plt.xlabel('edad')

plt.show()