class Persona():
    curp: str
    nombre: str

    def __init__(self, curp: str, nombre: str):
        self.curp = curp
        self.nombre = nombre

    def mostrar_info(self):
        print("Curp:", self.curp)
        print("Nombre:", self.nombre)
