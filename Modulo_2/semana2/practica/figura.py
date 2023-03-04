import abc


class FiguraGeometrica:
    __valor: float

    @abc.abstractmethod
    def obtenerArea(self):
        pass

    @abc.abstractmethod
    def obtenerPerimetro(self):
        pass

    def obtenerValor(self):
        return self.__valor

    def asignarValor(self, valor):
        self.__valor = valor
