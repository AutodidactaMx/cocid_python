# Packaging
# Como sugiere su nombre, envuelve todos los argumentos en una sola variable, 
# y esta llamada de función entra en una tupla llamada args.
#  Podemos usar cualquier otro nombre en lugar de args.
# Example: def func( *args )
def fun(a, b, c, d):
    print(a, b, c, d)
 
lista = [1, 2, 3, 4]
fun(*lista)
######################################## 
def fun2(*args):
    return sum(args)
print(fun2(10, 20))
########################################
def fun3(*args): 
    args = list(args) 
    print(args) 
fun3('Hello', 'beautiful', 'world!')
########################################
def fun4(a, b, c):
    print(a, b, c)
d = {'a':2, 'b':4, 'c':10}
fun4(**d)
########################################
def fun5(**kwargs):
    print(type(kwargs))     
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))
fun5(name="geeks", ID="101", language="Python")