class Cuadrado:    
    lado: float

    def __init__(self, lado: float):        
        self.lado = lado

    def area(self):
        return (self.lado * self.lado) 

    def perimetro(self):
        return self.lado + self.lado + self.lado + self.lado
