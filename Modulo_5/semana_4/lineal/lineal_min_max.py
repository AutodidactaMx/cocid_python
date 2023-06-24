"""
De manera similar a Single Feature Scaling, 
Min Max convierte cada valor de una columna en un número entre 0 y 1. 
El nuevo valor se calcula como la diferencia entre el valor actual y el valor mínimo, 
dividido por el rango de los valores de la columna. 
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./data/bienes_raices.csv')
scaled = (df['Precio'] - df['Precio'].min())/(df['Precio'].max() - df['Precio'].min())

fig, axs = plt.subplots(2, 1)
axs[0].hist(scaled)
axs[1].hist(df.Precio)

plt.show()
