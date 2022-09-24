from figura import FiguraGeometrica


class Cuadrado(FiguraGeometrica):

    def obtenerArea(self):
        return pow(self.obtenerValor(), 2)

    def obtenerPerimetro(self):
        return self.obtenerValor() * 4
