import numpy as np 
from matplotlib import pyplot as plt 

dias = np.arange(0, 132,dtype = np.int32)
temp = np.random.uniform(18, 32, dias.size)


media = np.zeros((dias.size), dtype=float) 
median = np.copy(media)  
minimo = np.copy(media)  
maximo = np.copy(media)  
media[:] = np.mean(temp) #  se utiliza para distribuciones normales de números, con una cantidad baja de valores atípicos.
median[:] = np.median(temp) #  se utiliza generalmente para devolver la tendencia central en el caso de distribuciones numéricas sesgadas
minimo[:] = np.min(temp)
maximo[:] = np.max(temp)

plt.title("Temperatura 2021") 
plt.xlabel("Dias") 
plt.ylabel("Temperatura") 
plt.plot(dias,temp,  "#F4BFBF",label="temperatura") 
plt.plot(dias,media, "#1A3C40", label="media") 
plt.plot(dias,median, "#9254C8", label="mediana") 
plt.plot(dias,minimo, "#8CC0DE", label="minimo") 
plt.plot(dias,maximo, "#FF5D5D", label="maximo") 
plt.tight_layout()
plt.legend()
plt.grid(b=True)
plt.show()
