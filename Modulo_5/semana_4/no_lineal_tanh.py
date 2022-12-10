import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('cars.csv')
p = 10000
scaled = df['price_usd'].apply(lambda x: np.tanh(x/p))

fig, axs = plt.subplots(2, 1)
axs[0].hist(df.price_usd)
axs[1].hist(scaled)
plt.show()


