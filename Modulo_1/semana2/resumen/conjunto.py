s = {1, 2, 3, 4}
print(s[2])
s1 = {}
s2 = {True, 3.14, None, False, "Hola mundo", (1, 2)}

s2.add(32)
s2.remove(32)
while s2:
    print(s2.pop())

   
dd = set([1, 2, 2, 3, 4])
print(dd)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
#unión
print(a | b)
#intersección 
print(a & b)
#diferencia
print(a - b)
print(b - a)