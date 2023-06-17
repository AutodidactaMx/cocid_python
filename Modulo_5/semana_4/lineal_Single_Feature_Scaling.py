import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bienes_raices.csv')
scaled = df['Precio']/df['Precio'].max()

fig, axs = plt.subplots(2, 1)
axs[0].hist(df.Precio)
axs[1].hist(scaled)
plt.show()