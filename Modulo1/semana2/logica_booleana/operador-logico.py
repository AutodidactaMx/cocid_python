animal_a="perro"
animal_b="gato"
animal_c="perico"

animal="perro"
# Es falso por que no cumple ambas condiciones
print(animal == animal_a and animal == animal_b) 
# Es verdadero por que entra a una condición
print(animal == animal_a or animal == animal_b) 
# Es verdadero por que cumple ambas condiciones
print(animal != animal_b and animal != animal_c) 
 # Es falso por que no cumple ninguna condición
print(animal == animal_b or animal == animal_c)
# Es verdadero al comparar que es falso
print(not(animal == animal_b)) 

