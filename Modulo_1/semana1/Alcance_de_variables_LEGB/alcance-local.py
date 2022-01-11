def fun1():
    a = 0  # Variables locales
    a += 1
    print("funcion 1 variable a = ", a)

def fun2():
    a = "uno" # Variables locales
    a = a + ", dos"
    print("funcion 2 variable a = ", a)

a = 'Hola Python'  # Variable global
fun1()
fun2()
print("Fuera de la función a =", a)
