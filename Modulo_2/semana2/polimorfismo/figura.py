class Figura():
    def __init__(self, figura):
        self.__figura = figura

    def area(self):
        return self.__figura.area()

    def perimetro(self):
        return self.__figura.perimetro()
