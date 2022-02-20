from circulo import Circulo
from cuadrado import Cuadrado
from figura import Figura


circulo = Circulo(1)
cuadrado = Cuadrado(1)

figura = Figura(circulo)
print(figura.area())
print(figura.perimetro())
