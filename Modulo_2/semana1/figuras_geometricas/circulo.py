import math


class Circulo:
    valor: float

    def __init__(self, valor):
        self.valor = valor

    def area(self):
        return math.pi * pow(self.valor, 2)

    def perimetro(self):
        return 2 * math.pi*self.valor
