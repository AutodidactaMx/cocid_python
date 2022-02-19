class Cuadrado:
    valor: float

    def __init__(self, valor):
        self.valor = valor

    def area(self):        
        return pow(self.valor, 2)

    def perimetro(self):        
        return self.valor * 4
