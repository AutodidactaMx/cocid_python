# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Escribir un programa que resuelva lo siguiente:  De acuerdo a la 
# siguiente lista de colores : 
# [“rojo”,”lila”,”verde”,”morado”,”naranja”,”morado”,”verde”,”verde”,”lila”] 
# debes generar e imprimir una lista que contenga como elementos a tuplas de dos elementos, 
# cada una compuesta por color de la lista original y la cantidad de veces que aparece en ella.
# Resultado : [('rojo', 1), ('verde', 3), ('morado', 2), ('lila', 2), ('naranja', 1)]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

lista_original = ["rojo","lila","verde","morado","naranja","morado","verde","verde","lila"]
lista_valor_unico  =  set(lista_original)
lista_tuplas = []
print("Lista original : ", lista_original)
print("Lista valores unicos : ",lista_valor_unico)
for valor in lista_valor_unico:    
    tupla = (valor,lista_original.count(valor))     
    lista_tuplas.append(tupla)
print("Lista tuplas : ", lista_tuplas)