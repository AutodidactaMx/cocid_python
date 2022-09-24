from persona import Persona


class Empleado(Persona):
    salario: str
    cp: str

    def __init__(self, curp: str, nombre: str, salario: str, cp: str):
        self.salario = salario
        self.cp = cp
        Persona.__init__(self, curp, nombre)

    def mostrar_info(self):
        super().mostrar_info()
        print("Salario:", self.salario)
        print("Codigo postal:", self.cp)
