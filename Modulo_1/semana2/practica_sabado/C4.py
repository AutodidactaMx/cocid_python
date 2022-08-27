# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Escribir un programa que resuelva lo siguiente: en un tipo de estructura
# de datos de diccionario debe contener la cantidad de interacción de una
# publicación con los siguientes valores:
# “Comentarios”:”2”
# “Likes”:”2003”
# “Dislike”:”222”
# “Emoji”:”100”
# Al final debe mostrar el número total de las diferentes interacciones en la publicación.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

publicacion = {
    "Comentarios": 2,
    "Likes": 2003,
    "Dislike": 222,
    "Emoji": 100,
}
total_interaccion = 0
for clave in publicacion:
    total_interaccion += publicacion[clave]    
print("Número total de las diferentes interacciones en la publicación",
      total_interaccion)
