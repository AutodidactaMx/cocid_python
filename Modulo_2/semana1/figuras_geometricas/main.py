from circulo import Circulo
from cuadrado import Cuadrado
from triangulo_equilatero import Triangulo_Equilatero
from triangulo_isosceles import Triangulo_Isosceles
print("Trinagulo isosceles")
triangular_isosceles = Triangulo_Isosceles(20, 30, 31.62)
print(triangular_isosceles.area())
print(triangular_isosceles.perimetro())
print("Trinagulo equilatero")
triangular_equilatero = Triangulo_Equilatero(10)
print(triangular_equilatero.perimetro())
print(triangular_equilatero.area())
print("Cuadrado")
cuadrado = Cuadrado(5)
print(cuadrado.area())
print(cuadrado.perimetro())
print("Circulo")
circulo = Circulo(5)
print(circulo.area())
print(circulo.perimetro())
