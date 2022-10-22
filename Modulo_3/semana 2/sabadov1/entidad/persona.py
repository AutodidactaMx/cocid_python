
class PersonaEntidad:
    curp: str = None
    nombre: str = None
    edad: str = None
    correo: str = None
    telefono: str = None

    
    def __init__(self, curp, nombre, edad, correo, telefono) -> None:
        self.curp = curp
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.telefono = telefono        