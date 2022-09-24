from persona import Persona


class Cliente(Persona):
    direccion: str
    esMiembro: bool

    def __init__(self, curp: str, nombre: str, edad: str, correo: str,
                 telefono: str, direccion: float):
        self.direccion = direccion        
        Persona.__init__(self, curp, nombre, edad, correo, telefono)

    def mostrar_info(self):
        super().mostrar_info()
        print("direccion : ", self.direccion)
        print("es miembro : ",  "SI" if self.esMiembro == True else "No" )

    def asignarEstadoMembresia(self, estado: bool):
        self.esMiembro = estado
