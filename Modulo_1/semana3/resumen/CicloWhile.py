########################################
dia = 0    
semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
while dia < 7:
   print("Hoy es " + semana[dia])
   dia += 1
########################################
while True:
   respuesta = input("Quiere salir SI o NO :")
   if respuesta == "SI" : 
    print("Adios")
    break
   else : 
    print("No quiere salir")