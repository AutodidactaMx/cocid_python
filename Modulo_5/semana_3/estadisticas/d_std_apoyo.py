import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cars.csv')

idx_filtro =  ((df['year_produced']==2015)  ) & ( (df['manufacturer_name']=='BMW') )
df_mm = df[idx_filtro]
ord = df_mm.sort_values(by='price_usd', ascending=True)
print(ord['price_usd'])
df_mm['price_usd'].plot.hist(bins=20)
plt.show()