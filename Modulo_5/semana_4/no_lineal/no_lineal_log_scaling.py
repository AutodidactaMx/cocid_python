'''
Aplica la función logaritmo a los valores de las variables. 
Es útil cuando los datos tienen una distribución sesgada o tienen una amplia gama de valores.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('.data/cars.csv')
scaled = df['price_usd'].apply(lambda x: np.log(x) if x != 0 else 0)

fig, axs = plt.subplots(2, 1)
axs[0].hist(df.price_usd)
axs[1].hist(scaled)
plt.show()

