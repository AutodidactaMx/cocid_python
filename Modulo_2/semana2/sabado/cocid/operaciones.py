class OperacionesBasicas:

    def __init__(self, datos: list):
        self.datos = datos

    def suma(self) -> float:
        '''Obtiene la suma total de la estructura 
        inicial de datos'''
        suma = 0
        for dato in self.datos:
            suma += dato
        return suma

    def longitud(self) -> float:
        '''Obtiene la longitud de la estructura 
        inicial de datos'''
        cont = 0
        for i in self.datos:
            cont += 1
        return cont

    def maximo(self, dato) -> float:
        '''Obtiene el valor maximo de una estructura 
        proporcionada por argumento'''
        max = 0
        for valor in dato:
            if (valor > max):
                max = valor
        return max
