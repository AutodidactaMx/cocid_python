"""
En este caso haremos dos diferencias para  revisar  como nos da autocorrelacion 
y luego  volver a realizar la prueba
"""
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

'''
Solo se necesita si la series estacionaria. De lo contrario, no se necesita diferenciación, es decir, d = 0.
'''
#Serie Original
fig, axes =  plt.subplots(3,2, sharex=False)

axes[0,0].plot(df.values,color="red")
axes[0,0].set_title("Serie Original")
plot_acf(df.values, ax = axes[0,1], color='red')

#Primera diferenicacion d = 1.
diff1 = df.diff()
axes[1,0].plot(diff1.values,color="green")
axes[1,0].set_title("Diferenciacion de primer orden")
plot_acf(diff1.dropna().values, ax = axes[1,1], color='green')

#Segunda diferenicacion d = 2.
diff2 = df.diff().diff()
axes[2,0].plot(diff2.values,color="blue")
axes[2,0].set_title("Diferenciacion de segundo orden")
plot_acf(diff2.dropna().values, ax = axes[2,1], color='blue')
plt.show()