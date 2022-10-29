
class Persona:
    curp: str = None
    nombre: str = None
    edad: str = None
    correo: str = None
    telefono: str = None

    
    def __init__(self) -> None:
        pass

    
    def asignar(self, curp, nombre, edad, correo, telefono) -> None:
        self.curp = curp
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.telefono = telefono
        return self

    def mostrar_info(self) -> None:
        print("curp : ", self.curp)
        print("nombre : ", self.nombre)
        print("edad : ", self.edad)
        print("correo : ", self.correo)
        print("telefono : ", self.telefono)
        
    def __str__(self) -> str:
        return ("{:<15} {:<15} {:<15} {:<15}".format(self.curp,self.nombre,self.edad,self.correo,self.telefono))
