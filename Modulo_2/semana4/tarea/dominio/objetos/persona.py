class Persona:
    curp: str = None
    nombre: str = None
    edad: str = None
    correo: str = None
    telefono: str = None

    def __init__(self) -> None:
        pass

    def mostrar_info(self) -> None:
        print("curp : ", self.curp)
        print("nombre : ", self.nombre)
        print("edad : ", self.edad)
        print("correo : ", self.correo)
        print("telefono : ", self.telefono)
