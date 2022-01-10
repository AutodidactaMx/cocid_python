import array as arr

# Arreglo tipo entero
a = arr.array('i', [1, 2, 3])

print("Arreglo antes de insertar : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# Insertar elemento por posicion
a.insert(0, 4)

print("Arreglo despues de insertar : ", end=" ")
for i in (a):
    print(i, end=" ")
print()

# Arreglo tipo flotante
b = arr.array('d', [2.5, 3.2, 3.3])

print("Arreglo antes de insertar : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()

# Agregando elemento  usando append
b.append(4.4)

print("Arreglo despues de insertar : ", end=" ")
for i in (b):
    print(i, end=" ")
print()
