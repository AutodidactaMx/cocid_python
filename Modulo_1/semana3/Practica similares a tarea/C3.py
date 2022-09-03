materias = ["Matemáticas", "Física", "Química", "Historia"]
print("De la siguiente lista :")
print(materias)
respuesta = input("¿Desea agregar una materia más? si o no : ")

if "si" == respuesta:
    materia = input("¿Que materia quisiera agregar? : ")
    if (materia not in materias):
        materias.append(materia)

print(materias)
