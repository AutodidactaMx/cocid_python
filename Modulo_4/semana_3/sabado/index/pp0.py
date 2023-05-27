import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame de ejemplo
data = {'nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis'],
        'género': ['Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino']}
df = pd.DataFrame(data)
df['género'] = pd.Categorical(df['género'].apply(str))
print(df.info())
# Contar el número de ocurrencias de cada categoría
count = df['género'].value_counts()

# Crear gráfico de barras
plt.bar(count.index, count.values)

# Personalizar el gráfico
plt.title('Distribución de Género')
plt.xlabel('Género')
plt.ylabel('Cantidad')

# Mostrar el gráfico
plt.show()