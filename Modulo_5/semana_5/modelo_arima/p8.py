'''
Hay un paquete que proporciona en un enfoque paso a paso para buscar múltiples
combinaciones de parámetros p, d, q y elige el mejor modelo que tiene el menor AIC.
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

X = (df.values)
size = int(len(X) * 0.75)
train, test = X[0:size], X[size:len(X)]

df=pd.read_csv('./datos/AirPassengers.csv')
df.set_index('Month',inplace=True)
df.index=pd.to_datetime(df.index)

arima_model = auto_arima(train, error_action='ignore', trace=True,
                      suppress_warnings=True, maxiter=5,
                      seasonal=True, m=12)   
arima_model.plot_diagnostics(figsize=(15,2))
plt.show()
