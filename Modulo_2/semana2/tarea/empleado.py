from persona import Persona


class Empleado(Persona):
    puesto: str = "Obrero"
    sueldo_diario: float
    bono_mensual: float

    def __init__(self, curp: str, nombre: str, edad: str, correo: str,
                 telefono: str, sueldo_diario: float, bono_mensual: float):        
        self.sueldo_diario = sueldo_diario
        self.bono_mensual = bono_mensual
        Persona.__init__(self, curp, nombre, edad, correo, telefono)

    def mostrar_info(self):
        super().mostrar_info()
        print("Puesto : ", self.puesto)
        print("sueldo_diario : ", self.sueldo_diario)
        print("bono_mensual : ", self.bono_mensual)
        print("Pago mensual : ", self.calcular_pago_mensual())

    def calcular_pago_mensual(self):
        return (self.sueldo_diario * 30)+self.bono_mensual
