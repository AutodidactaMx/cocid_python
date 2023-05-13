import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios
x = np.linspace(0, 5, 100)
print(x)

# Crear varias funciones para graficar
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)

# Crear el gráfico de línea con múltiples líneas
plt.plot(x, y1, label='Sin(x)')
plt.plot(x, y2, label='Cos(x)')
plt.plot(x, y3, label='Sin(x) + Cos(x)')

# Agregar etiquetas a los ejes
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Agregar título al gráfico
plt.title('Gráfico de línea de ejemplo')

# Agregar leyenda al gráfico
plt.legend()

# Mostrar el gráfico
plt.show()
