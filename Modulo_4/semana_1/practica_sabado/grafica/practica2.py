import matplotlib.pyplot as plt

# Datos de ejemplo
x = ['A', 'B', 'C', 'D', 'E']
y = [10, 24, 36, 40, 15]

# Crear un gráfico de barras
plt.bar(x, y)

# Agregar etiquetas a los ejes
plt.xlabel('Categorías')
plt.ylabel('Cantidad')

# Agregar título al gráfico
plt.title('Gráfico de barras de ejemplo')

# Mostrar el gráfico
plt.show()
