#Unpacking
#Desempaquetar es el término que se refiere a una lista de operaciones o tupla asignada a una sola variable.
# Example - (a, b, c) = List/tuple
a, b, c = '123'
print(f"{a} {b} {c}")
a, b, c = '123'
print(f"{a} {b} {c}")
a, b, c = [1, 2, 3]
print(f"{a} {b} {c}")
mi_dict = {'uno': 1, 'dos':2, 'tres': 3}
a, b, c = mi_dict
print(f"{a} {b} {c}")
a, b, c = mi_dict.values()
print(f"{a} {b} {c}")

########################################
def fun2():
    return (1,2,3) 
a , b, c = fun2()
print(f"{a} {b} {c}")