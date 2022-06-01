import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cars.csv')

idx_filtro =  ((df['year_produced']==2015) | (df['year_produced']==2016) ) & ( (df['manufacturer_name']=='Volkswagen') | (df['manufacturer_name']=='Audi')) 
df_mm = df
print(df_mm)

df_media = df_mm.groupby(['year_produced'])[['price_usd']].median()
df_mean = df_mm.groupby(['year_produced'])[['price_usd']].mean()

df_media.plot.bar(title = 'Mediana')
df_mean.plot.bar(title = 'Media')
plt.show()