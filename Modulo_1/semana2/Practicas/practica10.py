# Generar e imprimir una lista que contenga como elementos 
# a tuplas de dos elementos, cada una compuesta por un número de la lista original
# y la cantidad de veces que aparece en ella. Por ejemplo, 
# si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: 
# [(5,3), (16,1), (2,2), (57,1)]
lista_original = [5,16,2,5,57,5,2]
lista_valor_unico  =  set(lista_original)
lista_tuplas = []
print("Lista original : ", lista_original)
print("Lista valores unicos : ",lista_valor_unico)
for valor in lista_valor_unico:    
    tupla = (valor,lista_original.count(valor))     
    lista_tuplas.append(tupla)
print("Lista tuplas : ", lista_tuplas)
