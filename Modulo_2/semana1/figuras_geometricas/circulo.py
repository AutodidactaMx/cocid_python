import math
class Circulo:    
    radio: float

    def __init__(self, radio: float):        
        self.radio = radio
        self.p = math.pi

    def area(self):
        return self.p * pow(self.radio, 2)

    def perimetro(self):
        return 2 * self.p * self.radio
