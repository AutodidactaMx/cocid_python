import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Datos de ejemplo
X = np.array([[1, 2], [1, 3], [2, 2], [2, 4], [1, 5], [6, 4], [9, 1], [9, 2], [8, 5], [6, 4]])

# Crear el objeto KMeans con 2 clusters
kmeans = KMeans(n_clusters=2)

# Ajustar el modelo a los datos
kmeans.fit(X)

# Obtener las etiquetas de los clusters asignados a cada punto
labels = kmeans.labels_

# Obtener las coordenadas de los centroides
centroids = kmeans.cluster_centers_

# Visualización de los clusters y los centroides
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=100)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('K-Means Clustering')
plt.show()
