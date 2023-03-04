from circulo import Circulo
from cuadrado import Cuadrado
from triangulo import TrianguloRectangulo


def calculo(figura):
    print(figura.obtenerArea())
    print(figura.obtenerPerimetro())


circulo = Circulo()
circulo.asignarValor(1)
calculo(circulo)

cuadrado = Cuadrado()
cuadrado.asignarValor(1)
calculo(cuadrado)


triangulo = TrianguloRectangulo()
triangulo.asignarValor(50)
triangulo.asignarValor2(50)
calculo(triangulo)
