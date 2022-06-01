'''
Calcular los auto mas vendidos por año
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('cars.csv')
df['ones'] = 1

idx_filtro =  ((df['year_produced']==2015) | (df['year_produced']==2016) ) & ( (df['manufacturer_name']=='Volkswagen') | (df['manufacturer_name']=='Audi')) 
df_my = df

df_my = df_my.groupby(['manufacturer_name','year_produced'])[['ones']].sum()
df_y = df_my.groupby(['year_produced'])[['ones']].max()

def f_filter(x):         
    return np.max(x['ones']) == df_y.loc[x.name[0],:].max() 

df_mm= df_my.groupby(['year_produced','manufacturer_name']).filter(f_filter)

df_mm.plot.bar()
plt.show()

