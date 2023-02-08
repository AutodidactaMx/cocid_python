a = 10 
b = 100 
print("a == b:", a == b)
print("a > b:", a > b)
print("a >= b:", a >= b)

cadena1 = "Hola"
cadena2 = "hola"
print(cadena1 == cadena2)

animal_a="platano"
animal_b="manzana"
animal="platano"
# Es falso por que no cumple ambas condiciones
print(animal == animal_a and animal == animal_b)
# Es verdadero por que entra a una condición
print(animal == animal_a or animal == animal_b)
# Es verdadero al comparar que es falso
print(not(animal == animal_b))