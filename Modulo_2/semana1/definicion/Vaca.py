class Vaca:
    cola = True
    da_leche = False
    camina = False

    def __init__(self, nombre, color, cola):
        self._nombre = nombre
        self.color = color
        self.cola = cola

    def info(self):
        print("#"*30)
        print("Nombre :", self._nombre)
        print("Color:", self.color)
        print("Cola:", ("Con cola" if(self.cola) else "Sin cola"))
        print(("Esta caminando" if(self.camina) else "Esta detenida"))
        print("#"*30)

    def caminar(self):
        self.camina = True

    def detenerse(self):
        self.camina = False


muu = Vaca("muu", "amarilla", True)
muu._nombre = "cambio de nombre"
muu.caminar()
muu.info()

clara_bella = Vaca("clara bella", "blanca", False)
muu.caminar()
muu.detenerse()
clara_bella.info()
