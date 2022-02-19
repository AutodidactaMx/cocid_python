class Triangulo_Isosceles:
    base: float
    altura: float
    lado: float

    def __init__(self, base: float, altura: float, lado: float):
        self.base = base
        self.altura = altura
        self.lado = lado

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return 2*self.lado + self.base
