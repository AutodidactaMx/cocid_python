from utileria.consola import texto_colores as color1
from utileria.consola import fondo_colores as fondocolor
from utileria.fechas import timestamp as tm

print(color1.texto_amarillo("Hola de color amarillo"))
print(color1.texto_azul("Hola de color azul"))
print(color1.texto_rojo("Hola de color rojo"))
print(color1.texto_verde("Hola de color verde"))
print(color1.texto_restablecer("Restablecio los colores por defecto"))


print(fondocolor.fondo_amarillo("Hola de color amarillo"))
print(fondocolor.fondo_azul("Hola de color azul"))
print(fondocolor.fondo_rojo("Hola de color rojo"))
print(fondocolor.fondo_verde("Hola de color verde"))
print(fondocolor.fondo_restablecer("Restablecio los colores por defecto"))

tm.convertir() 