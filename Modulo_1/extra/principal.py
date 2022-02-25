from configuracion  import MENU_CANCIONES as lista_menus
import biblioteca as biblio

print("#"*80)
print("Bienvenido, por favor, selecciona una canción de este top \
          de 4 canciones ".center(80))
print("#"*80, end="\n\n")

while True:
    for menu in lista_menus:
        print(menu)    
  
    entrada = input("\nOpcion :")
    opcion = biblio.seleccion(entrada)
    biblio.mostrar_cancion(opcion)

