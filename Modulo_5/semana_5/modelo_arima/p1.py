'''
Verificamos si la serie es estacionaria usando 
la prueba Augmented Dicker Fuller.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima  

df=pd.read_csv('./datos/AirPassengers.csv')
df.set_index('Month',inplace=True)
df.index=pd.to_datetime(df.index)

'''Revisamos el dickey-Fuller para probar la estacionalidad'''
result=adfuller(df['#Passengers'])
result_dict = dict(zip(['Test (ADF Test)', 'pvalue', 'usedlag', 'nobs', 
                        'critical' 'values', 'icbest'],result))


''' Dado que el valor  p-value es mayor que el nivel de significacia , 
tenemos que diferenciar al serie y veremos como se ve el grafico de correlacion.'''
print(result_dict)