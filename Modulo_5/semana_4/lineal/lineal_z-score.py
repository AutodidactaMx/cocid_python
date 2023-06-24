'''
Da una idea de qué tan lejos está del valor promedio de un punto de datos.
Ocupa la medida y desviaciones estándar por debajo o por encima de la 
población dada significan una puntuación bruta. 
Se tratar de ajustar en un rango de -3 y 3 (Lineal) se esta fuera es no lineal
El escalamiento Z-score, donde la media es 0 y la desviación estándar es 1. 
Los valores positivos y negativos representan la distancia con respecto a la media en términos de desviaciones estándar.
'''
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('bienes_raices.csv')
scaled = (df['Precio']-df['Precio'].mean())/df['Precio'].std()


fig, axs = plt.subplots(2, 1)
axs[0].hist(scaled)
axs[1].hist(df.Precio)
plt.show()