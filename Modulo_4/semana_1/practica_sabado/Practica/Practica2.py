'''
En estadística, la desviación típica 
(también conocida como desviación estándar es una medida que se utiliza para cuantificar 
la variación o la dispersión de un conjunto de datos numéricos.1​
Una desviación estándar baja indica que la mayor parte de los datos de una muestra 
tienden a estar agrupados cerca de su media,
mientras que una desviación estándar alta indica que los datos se extienden 
sobre un rango de valores más amplio.

Analisar el peso de  niños 
'''

import matplotlib.pyplot as plt 
import numpy as np 

def graficar(g,n):
    plt.subplot(2,1,n)
    plt.title(f"Grupo {n}")        
    plt.fill_between( [  np.mean(g) -  np.std(g) ,  np.mean(g) +  np.std(g)  ]  , [0,0] , [len(g)]*2 ,color='#006E7F', label='STD', alpha=0.5 , zorder=1)
    plt.plot( np.ones(len(g))*np.mean(g), np.arange(len(g)), '#006E7F' , label='Media', linewidth=5 , alpha=0.7)
    plt.scatter(g, y, label='Peso', color='#B22727')
    plt.ylim(0, 2)
    plt.xlim(10, 30)
    plt.grid(b=True)
    plt.yticks([])

    plt.legend()

g1 = np.array([10,12,23,25,30])
g2 = np.array([18,19,20,21,22])

y = np.full([5],1,dtype = np.int8)

graficar(g1,1)
graficar(g2,2)
plt.show()