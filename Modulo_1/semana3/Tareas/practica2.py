# Obtenga dos números del usuario mediante el indicador de entrada. 
# Si a es mayor que b, devuelve a es mayor que b, si a es menor, 
# b devuelve a es menor que b, de lo contrario, a es igual a b.
a = float(input("Escribe un números a : "))
b = float(input("Escribe un números b : "))

if(a > b):
    print("a es mayor que b")
elif(a < b):
    print("a es menor que b")
elif(a == b):
    print("a es igual a b")    