# Escribir un programa que lea un entero positivo, n, introducido por el
# usuario y después muestre en pantalla la suma de todos los enteros desde
# 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada
# de la siguiente forma:  n * (n + 1) / 2.

def calculo(n):
    return n * (n + 1) / 2


numero_entrada = int(input("Introduce un numero entero:"))
print(calculo(numero_entrada))
