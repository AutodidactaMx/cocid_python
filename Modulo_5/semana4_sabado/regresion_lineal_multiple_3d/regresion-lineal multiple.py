import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import r2_score
from pandastable import Table, TableModel
import sidetable 
import tkinter as tk

sns.set()

df = pd.read_csv('./regresion_lineal_multiple_3d/softdrink.csv')

x = df[['x1','x2']].values
y = df[['y']].values

modelo = linear_model.LinearRegression()
modelo.fit(x, y)  
y_pred = modelo.predict(x)

x1w= int(np.max(x[:,0]))
x2w= int(np.max(x[:,1]))
fig = plt.figure(figsize=(15,10))
p3 = fig.add_subplot(projection='3d')
x1, x2 = np.meshgrid(range(x1w), range(x2w))
z_modelo = modelo.coef_[0][0]*x1 + modelo.coef_[0][1]*x2
p3.plot_surface(x1, x2, z_modelo, alpha=0.3, color='green')
p3.scatter(x[:,0], x[:,1], y)
p3.set_title(u'Regresión lineal usando dos variables \(X1,X2) para predecir Y')
p3.set_xlabel('Eje X1')
p3.set_ylabel('Eje X2')
p3.set_zlabel('Eje Y')
p3.view_init(10, )
plt.show()


r2 =  r2_score(y, y_pred)
print('Estadístico R2: ' , r2)