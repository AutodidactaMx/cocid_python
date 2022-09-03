tamanio = int(input("Introduce la altura del triángulo equilátero: "))

for i in range(1, tamanio + 1):
    for j in range(tamanio - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()