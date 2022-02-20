
class Salario():
    pago: float

    def __init__(self, pago: float):
        self.pago = pago

    def pago_anual(self):
        return self.pago * 12
