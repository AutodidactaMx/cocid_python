# Obtenga la entrada del usuario usando input ("Ingrese su edad:").
# Si el usuario tiene 18 años o más, dé su opinión: tiene edad
# suficiente para conducir.
# Si es menor de 18, dé su opinión para esperar la cantidad de años que faltan.

edad = int(input("Ingrese su edad:"))
if(edad >= 18):
    print("Tiene edad suficiente para conducir.")
if(edad > 0 and edad < 18):
    anios_faltantes = 18 - edad
    print(f"Necesitas {anios_faltantes} años más para conducir.")
else:
    print("Aun no nace")
# Modo de pruena