global texto 
texto = "variable global" #variables globales
def funcion():
    global texto 
    texto= "variable local" #variables locales        
funcion()
print(texto)
