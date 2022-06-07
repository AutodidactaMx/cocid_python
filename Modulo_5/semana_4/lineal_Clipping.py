import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cars.csv')
vmax = 10000
vmin = 10
scaled = df['price_usd'].apply(lambda x: vmax if x > vmax else vmin if x < vmin else x)

fig, axs = plt.subplots(2, 1)
axs[0].hist(df.price_usd)
axs[1].hist(scaled)

plt.show()


