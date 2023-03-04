class Persona:
    curp: str
    nombre: str
    edad: str
    correo: str
    telefono: str

    def __init__(self, curp: str, nombre: str, edad: str,
                 correo: str, telefono: str):
        self.curp = curp
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.telefono = telefono

    def mostrar_info(self):
        print("curp : ", self.curp)
        print("nombre : ", self.nombre)
        print("edad : ", self.edad)
        print("correo : ", self.correo)
        print("telefono : ", self.telefono)
