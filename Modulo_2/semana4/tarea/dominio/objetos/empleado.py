from dominio.objetos.persona import Persona

class Empleado(Persona):
    puesto: str = "Obrero"
    sueldo_diario: float
    bono_mensual: float
    
    def __init__(self) -> None:
        pass

    def mostrar_info(self):
        super().mostrar_info()
        print("Puesto : ", self.puesto)
        print("sueldo_diario : ", self.sueldo_diario)
        print("bono_mensual : ", self.bono_mensual)
        print("Pago mensual : ", self.calcular_pago_mensual())

    def calcular_pago_mensual(self):
        return (self.sueldo_diario * 30)+self.bono_mensual
