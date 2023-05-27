# Análisis de datos en Pandas:
import pandas as pd
import matplotlib.pyplot as plt


data = {'Nombre': ['Juan', 'María', 'Carlos', 'Luis'],
        'Edad': [25, 31, 18, 42],
        'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']}
df = pd.DataFrame(data)

# Crear un gráfico de barras a partir de los datos
df.plot(x='Nombre', y='Edad', kind='bar')
plt.show()
