import math
from figura import FiguraGeometrica


class Circulo(FiguraGeometrica):

    def obtenerArea(self):
        return math.pi * pow(self.obtenerValor(), 2)

    def obtenerPerimetro(self):
        return 2 * math.pi*self.obtenerValor()
