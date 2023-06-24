#Convierte cada valor de una columna en un número entre 0 y 1. 
#El nuevo valor se calcula como el valor actual dividido por el valor máximo de la columna. 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/bienes_raices.csv')
scaled = df['Precio']/df['Precio'].max()

fig, axs = plt.subplots(2, 1)
axs[0].hist(df.Precio)
axs[1].hist(scaled)
plt.show()