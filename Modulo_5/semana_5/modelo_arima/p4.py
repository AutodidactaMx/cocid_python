'''
¿Como encontrar el número de términos AR?
Cualquier autocorrelación en una serie estacionaria se puede rectificar 
agregando suficientes términos AR. Entonces inicialmente tomamos 
el orden del termino AR como igual a tantos rezagos que cruzan el 
límite de significancia en la gráfica PACF.
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

#Segunda diferenicacion d = 1.
diff = df.diff().diff()
'''
ACF y diagramas PACF son herramientas comúnmente usadas para la identificación del 
modelo en los modelos Box-Jenkins.
'''
'''
Tomaremos el numero el primer rezago que cruza el limite en este caso tomaremos AR p=1.
La función de autocorrelación parcial (PACF)
'''
fig, axes =  plt.subplots(2,2, sharex=False)
axes[0][0].plot(diff.values,color="orange")
axes[0][0].set_title("Diferenciacion")
axes[0][1].set(ylim=(-1,4))
plot_pacf(diff.dropna().values, ax = axes[0][1], color='orange', title="PACF Autocorrelación parcial AR p")


'''
Tomaremos el numero el primer rezago que cruza el limite en este caso tomaremos MA q=1.
La función de autocorrelación (ACF)
'''
axes[1][0].plot(diff.values,color="fuchsia")
axes[1][0].set_title("Diferenciacion")
axes[1][1].set(ylim=(-1,4))
plot_acf(diff.dropna().values, ax = axes[1][1], color='fuchsia',title="ACF Autocorrelacion Simple MA q")
plt.show()
