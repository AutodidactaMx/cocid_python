import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('bienes_raices.csv')
scaled = (df['Precio']-df['Precio'].mean())/df['Precio'].std()


fig, axs = plt.subplots(2, 1)
axs[0].hist(scaled)
axs[1].hist(df.Precio)
plt.show()