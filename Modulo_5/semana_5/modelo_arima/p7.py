'''Pronostico del modelo validación de avance'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

df=pd.read_csv('./datos/AirPassengers.csv')
df.set_index('Month',inplace=True)
df.index=pd.to_datetime(df.index)

X = (df.values)
size = int(len(X) * 0.75)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]


predictions = list()
for t in range(len(test)):
    model_train = ARIMA(history, order=(1,2,1))
    modelo_train_fit = model_train.fit()
    output = modelo_train_fit.forecast(steps=1)    
    yhat = output[0]
    predictions.append(yhat) 
    obs = test[t]
    history.append(obs)           

fc = np.array(predictions).reshape(-1,1)
test_full =np.concatenate([train, test])
predictions_full =np.concatenate([train, fc])
plt.show()
plt.plot(test_full, color='green')
plt.plot(predictions_full, color='red')
plt.show()
