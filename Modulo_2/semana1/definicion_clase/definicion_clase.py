class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.__patas = 4
        self._colas = 1
        self.caminando = False

    def caminar(self):
        self.caminando = True


mi_perro = Perro("PATOTAS", 2)


print("Nombre :", mi_perro.nombre)
print("Edad:", str(mi_perro.edad), " años")
mi_perro.caminar()
print("El perro esta caminando ?", mi_perro.caminando)
