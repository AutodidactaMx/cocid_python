# Escribe un programa donde tengas dos grupos de alumnos:
# Grupo A : Luisa, Ana, Luis, Pedro, Juan, Jessica, Magdalena
# Grupo B : Jesus, Claudia, Ana, Mauricio, Blanca, Jessica, Magdalena
# Me debe imprimir la lista de todos los estudiantes de ambos grupos, la intersección entre ellos y la diferencia.

grupo_a = set(["Luisa", "Ana", "Luis", "Pedro",
              "Juan", "Jessica", "Magdalena"])
grupo_b = set(["Jesus", "Claudia", "Ana", "Mauricio",
              "Blanca", "Jessica", "Magdalena"])

intersecion_alumnos = grupo_a & grupo_b
todos_alumnos = grupo_a | grupo_b
todos_diferencia = grupo_a - grupo_b

print("#####################################################################################################################################################################")
print("Todos los alumnos : ")
while todos_alumnos:
    print(todos_alumnos.pop(), end=",")
print()
print("#####################################################################################################################################################################")


print("Los alumnos en en ambos grupos : ")
while intersecion_alumnos:
    print(intersecion_alumnos.pop(), end=",")
print()


print("#####################################################################################################################################################################")
print("Alumnos que solo estan en sus propios grupos : ")
while todos_diferencia:
    print(todos_diferencia.pop(), end=",")
print()
print("#####################################################################################################################################################################")
