from cocid.estadistica import EstadisticaBasica

lista = []
with open('./data/lista.csv') as f:
    for line in f.readlines() : 
        for s in line.split(',') :
            lista.append(float(s))    

data = EstadisticaBasica(lista)

print("Maximo:",data.maximo(lista))
print("Longitud:",data.longitud())
print("Suma:",data.suma())
print("Moda:",data.moda())
print("Mediana:",data.mediana())
print("Media:",data.media())

