from salario import Salario


class Empleado():
    pago: float
    bono: float
    salario: Salario

    def __init__(self, pago: float, bono: float):
        self.pago = pago
        self.bono = bono
        self.salario = Salario(self.pago)

    def salario_anual(self):
        return self.salario.pago_anual() + self.bono


obj_emp = Empleado(100, 100)
print(obj_emp.salario_anual())
