"""
Los errores residuales parecen estar bien con una media
cercana a cero y una varianza uniforme.
Grafiquemos los valores reales contra los valores ajustados 
usando .plot_predict()
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

model = ARIMA(df.values, order=(1,2,1))
modelofit = model.fit()

'''
Revisar los errores residuales con una media 
'''
residuals = pd.DataFrame(modelofit.resid)
fig, axes =  plt.subplots(1,2)
residuals.plot(title="Residuales", ax = axes[0], color="crimson", lw=2)
residuals.plot(kind="kde", title="Densidad", ax = axes[1], color="crimson", lw=2)
plt.show()
