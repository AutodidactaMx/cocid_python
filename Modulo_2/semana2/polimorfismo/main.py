from circulo import Circulo
from cuadrado import Cuadrado
from figura import Figura

def imprimir_area(figura):
    print(figura.area())

circulo = Circulo(1)
cuadrado = Cuadrado(1)
imprimir_area(circulo)
imprimir_area(cuadrado)
