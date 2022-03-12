from dominio.objetos.persona import Persona


class Empleado(Persona):
    puesto: str = "Obrero"
    sueldo_diario: float
    bono_mensual: float

    def __init__(self) -> None:
        pass

    def asignar(self, curp, nombre, edad, correo, telefono, puesto, sueldo_diario, bono_mensual) -> None:
        super().asignar(curp, nombre, edad, correo, telefono)
        self.puesto = puesto
        self.sueldo_diario = sueldo_diario
        self.bono_mensual = bono_mensual
        return self

    def mostrar_info(self):
        super().mostrar_info()
        print("Puesto : ", self.puesto)
        print("sueldo_diario : ", self.sueldo_diario)
        print("bono_mensual : ", self.bono_mensual)
        print("Pago mensual : ", self.calcular_pago_mensual())

    def calcular_pago_mensual(self):
        return (self.sueldo_diario * 30)+self.bono_mensual

        
    def __str__(self) -> str:
        return ("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(self.curp,self.nombre,self.edad,self.correo,self.telefono,self.puesto,self.sueldo_diario,self.bono_mensual))
