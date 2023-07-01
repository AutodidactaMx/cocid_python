'''
Ahora que determinamos los valores de p, d y q tiene todo lo 
necesario para ajustarse al modelo ARIMA. Usemos la implementacion 
en package ARIMA de statsmodels.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima  

df=pd.read_csv('./AirPassengers.csv')
df.set_index('Month',inplace=True)
df.index=pd.to_datetime(df.index)

model = ARIMA(df.values, order=(1,1,0))
modelofit = model.fit()
'''El resumen del modelo revela mucha información'''
print(modelofit.summary())

