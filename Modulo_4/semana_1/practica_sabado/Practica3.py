from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

'''
Tiempo estimado en realizacion de examen 
min : 1.2, max : 3.87
alumnos aplicando el examen : 30
'''
dato = np.random.uniform(1.2, 3.87, 30)
d = np.sort(dato)
# Valores de rango en Percentile
p = np.array([0.0, 10.0, 20.0, 30.0,40.0,50.0,60.0,70.0,80.0,90.0, 100.0])

perc = np.percentile(d, p)
plt.title(f"Percentil de tiempo en aplicacion de examen")        
plt.plot(d)
# Coloque puntos rojos en los percentiles
plt.plot((len(d)-1) * p/100., perc, 'ro', label = "Percentil")
# Establecer ubicaciones y etiquetas de marca
plt.xticks((len(d)-1) * p/100., map(str, p))
plt.grid(b=True)
plt.legend()
plt.show()