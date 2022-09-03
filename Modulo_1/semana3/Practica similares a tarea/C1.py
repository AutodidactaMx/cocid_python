calificacion = int(input("Introduzca su calificación : "))
notas = {10: "Excelente", 9: "Muy Bien",
         8: "Bien", 7: "Suficiente", 6: "Aprobado"}
resultado = ""
if calificacion > 5 and calificacion <= 10:
    resultado = notas[calificacion]
elif calificacion >= 0 and calificacion < 5:
    resultado = "Reprobado"
else:
    resultado = "Debe introducir un valor entre 0 - 10"

print(resultado)
