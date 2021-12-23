a = 1  # Variable global
b = "global"

def fun():
    global b 
    a = 2  # Variables locales
    a += 1
    print("En la función a =", a)
    print("variable b =", b)    
    b = " modificado local"    

fun()
print("Fuera de la función a =", a)
print("Fuera de la función b =", b)
