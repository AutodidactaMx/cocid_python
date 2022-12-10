import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cars.csv')
idx_filtro =  ((df['year_produced']==2015)  ) 
df_mm = df[idx_filtro]
df_mm = df_mm[['manufacturer_name','price_usd']]
df_mm = df_mm.groupby(['manufacturer_name']).aggregate([np.mean,np.std])
qual = df_mm['price_usd']
qual.plot(kind = "barh", y = "mean", legend = False, xerr = "std", title = "Precios", color='green')
plt.show()
print(df_mm)