from salario import Salario


class Empleado():
    salario: Salario
    bono: float

    def __init__(self, salario: Salario, bono: float):
        self.bono = bono
        self.salario = salario

    def salario_anual(self):
        return self.salario.pago_anual() + self.bono


salario = Salario(100)
obj_emp = Empleado(salario, 100)
print(obj_emp.salario_anual())
