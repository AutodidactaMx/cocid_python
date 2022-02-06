# Escriba un bucle que haga siete llamadas a print(),
# de modo que obtengamos en la salida un triángulo.

for i in range(5):
    for j in range(i):
        print("*", end="")
    print("")

for i in range(1,5,1):    
        print("*"*i)    
