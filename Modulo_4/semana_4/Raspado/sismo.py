'''pip install lxml'''
import numpy as np
from matplotlib import cm
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime

cmap = LinearSegmentedColormap.from_list(name="sismo", 
                                             colors =['green','green','green','yellow', 'orange','red','brown','pink','purple','purple'],
                                             N=10)
nuevo_color = cm.get_cmap(cmap, 7)
tabs = pd.read_html('http://www.ssn.unam.mx/sismicidad/ultimos/')
df = tabs[0] 
df.rename(columns = { 
        'MagnitudMag.':'magnitud', 
        'Fecha y hora':'fecha',
        'Epicentro localización: latitud, longitud loc.: lat., long.' : 'localizacion',
        'ProfundidadProf.' : 'profundidad'}, inplace = True)
df['profundidad'] = df['profundidad'].apply(lambda x: x.replace("km", ""))
df['profundidad'] = df['profundidad'].astype(float)
df['fecha'] = df['fecha'].apply(lambda x: x.replace("&nbsp", "").replace("  ", " "))
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d %H:%M:%S')
df[['localizacion','latitud','altitud']] = df['localizacion'].str.split(',',expand=True)

fig, axes = plt.subplots(nrows=2, ncols=2)
ax = df.plot.scatter(grid=True,ax=axes[0,0], x='fecha',y='localizacion', c = 'magnitud',colormap=nuevo_color, vmin=0, vmax=10)
ax.set_ylim(0, 10)
ax1 = df.plot.scatter(grid=True,ax=axes[0,1], x='fecha',y='magnitud', c = 'magnitud',colormap=nuevo_color, vmin=0, vmax=10)
ax2 = df.plot.scatter(grid=True,ax=axes[1,0], x='fecha',y='profundidad', c = 'magnitud',colormap=nuevo_color, vmin=0, vmax=10)
plt.show()