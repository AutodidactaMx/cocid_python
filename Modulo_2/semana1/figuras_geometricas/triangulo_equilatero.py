from math import sqrt


class Triangulo_Equilatero:
    base: float

    def __init__(self, base: float):
        self.base = base

    def area(self):
        return (sqrt(3) / 4) * pow(self.base, 2)

    def perimetro(self):
        return 3*self.base
