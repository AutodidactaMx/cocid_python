def posicionNumero(num, max, min):
    if num == max:
        posicion = "Máximo"
    elif num == min:
        posicion = "Mínimo"
    else:
        posicion = "En medio"
    return posicion


print("Introduce tres números conforme se lo solicite")
num_a = int(input("Introduce el primero número a :"))
num_b = int(input("Introduce el primero número b :"))
num_c = int(input("Introduce el primero número c :"))

numeros = [num_a, num_b, num_c]
mayor = max(numeros)
menor = min(numeros)

print("número a : ", posicionNumero(num_a, mayor, menor))
print("número b : ", posicionNumero(num_b, mayor, menor))
print("número c : ", posicionNumero(num_c, mayor, menor))
