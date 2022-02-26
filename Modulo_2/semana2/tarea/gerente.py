from empleado import Empleado


class Gerente(Empleado):
    bono_especial: float = 1000.00    

    def __init__(self, curp: str, nombre: str, edad: str, correo: str,
                 telefono: str, sueldo_diario: float, bono_mensual: float):
        self.puesto = "Gerente"
        Empleado.__init__(self, curp, nombre, edad, correo,
                          telefono, sueldo_diario, bono_mensual)

    def calcular_pago_mensual(self):
        return super().calcular_pago_mensual() + self.bono_especial
