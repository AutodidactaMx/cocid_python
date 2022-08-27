# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Escribir un programa que resuelva lo siguiente: Debes guardar en
# una lista las siguientes calificaciones de un grupo :
# 7, 7.5, 6, 2, 8.3, 6.5, 10,9.4.
# Debe mostrar en pantalla :
# Calificación más baja.
# Calificacion mas alta.
# Promedio del grupo.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def promedio(lst):
    return sum(lst) / len(lst)

calificaciones = [7, 7.5, 6, 2, 8.3, 6.5, 10, 9.4]
calificaciones.sort()

print("Calificación más baja : ", calificaciones[0])
print("Calificacion mas alta : ", calificaciones[-1])
print("Promedio del grupo : ",  promedio(calificaciones))
