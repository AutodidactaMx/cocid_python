from configuracion import MENU_LIBROS as lista_menus
import biblioteca as biblio

biblio.mensaje_mas_opcion()

while True:
    for menu in lista_menus:
        print(menu)

    entrada = input("\nOpcion :")
    opcion = biblio.seleccion(entrada)
    biblio.mostrar_cancion(opcion)
