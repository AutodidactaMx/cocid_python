import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios
x = np.random.randn(100)
y = np.random.randn(100)

# Crear el gráfico de dispersión
plt.scatter(x, y)

# Agregar etiquetas a los ejes
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Agregar título al gráfico
plt.title('Gráfico de dispersión de ejemplo')

# Mostrar el gráfico
plt.show()
