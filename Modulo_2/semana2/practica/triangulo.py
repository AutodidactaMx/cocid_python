from math import sqrt
from figura import FiguraGeometrica


class TrianguloRectangulo(FiguraGeometrica):
    __valor2: float

    def obtenerValor2(self):
        return self.__valor2

    def asignarValor2(self, valor):
        self.__valor2 = valor

    def obtenerArea(self):
        return (self.obtenerValor() * self.obtenerValor2()) / 2

    def obtenerPerimetro(self):
        c = sqrt((pow(self.obtenerValor(), 2) + pow(self.obtenerValor2(), 2)))
        return (self.obtenerValor() + self.obtenerValor2()) + c
