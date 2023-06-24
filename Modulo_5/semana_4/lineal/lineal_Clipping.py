'''
El recorte implica la limitación de todos los valores por debajo o por encima de un cierto valor. 
El recorte es útil cuando una columna contiene algunos valores atípicos. Podemos establecer un valor 
máximo de vmax y un valor mínimo de vmin y establecer todos los valores atípicos superiores al valor 
máximo en vmax y todos los valores atípicos inferiores al valor mínimo en vmin. 
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/cars.csv')


limite_superior = 10000
limite_inferior = 10
scaled = df['price_usd'].clip(lower=limite_inferior, upper=limite_superior)

fig, axs = plt.subplots(2, 1)
axs[0].hist(df.price_usd)
axs[1].hist(scaled)

plt.show()


