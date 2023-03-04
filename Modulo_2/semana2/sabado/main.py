from cocid.estadistica import EstadisticaBasica
from cocid.operaciones import OperacionesBasicas

lista = []
with open('./data/lista.csv') as f:
    for line in f.readlines() : 
        for s in line.split(',') :
            lista.append(float(s))    

data = OperacionesBasicas(lista)

print("Maximo:",data.maximo(lista))
print("Longitud:",data.longitud())
print("Suma:",data.suma())
print("Moda:",data.moda())
print("Mediana:",data.mediana())
print("Media:",data.media())


x = 10
y = 3

print(x % y)

x = 15
y = 2

print(x // y)

##la división del piso // redondea el resultado al número entero más cercano

