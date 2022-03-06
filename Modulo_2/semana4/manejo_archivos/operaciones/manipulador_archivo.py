import random


class ManipuladorArchivo():
    ruta_archivo: str = None

    def __init__(self, ruta_archivo: str) -> None:
        self.ruta_archivo = ruta_archivo
        pass

    def crear_archivo_datos_aleatorios(self, cantidad: int) -> None:
        """Crear archivo con datos aleatorios. En caso de que exista el archivo se sobre escribira."""
        random_numbers = [random.randint(1, 100) for edad in range(cantidad)]
        archivo = open(self.ruta_archivo, "w+")
        for index, numero in enumerate(random_numbers, start=1):
            separador = "," if index < len(random_numbers) else ""
            escribir = f"{numero}{separador}"
            archivo.write(escribir)
        archivo.close()

    def agregar_archivo_datos_aleatorios(self, cantidad: int) -> None:
        """Agrega al archivo datos aleatorios. En caso de que no exista el archivo se crea."""
        random_numbers = [random.randint(1, 100) for edad in range(cantidad)]
        archivo = open(self.ruta_archivo, "a+")
        if(self.tiene_dato()):
            archivo.write(",")

        for index, numero in enumerate(random_numbers, start=1):
            separador = "," if index < len(random_numbers) else ""
            escribir = f"{numero}{separador}"
            archivo.write(escribir)
        archivo.close()

    def extraer_datos_archivo(self) -> list:
        archivo = open(self.ruta_archivo, "r")
        return list(map(int, archivo.read().split(",")))

    def tiene_dato(self):
        archivo = open(self.ruta_archivo, "r")
        dato = archivo.read()
        archivo.close()
        return True if dato else False
