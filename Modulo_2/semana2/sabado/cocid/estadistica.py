from cocid.operaciones import OperacionesBasicas

class EstadisticaBasica(OperacionesBasicas):

    def __init__(self, datos: list) -> None:        
        OperacionesBasicas.__init__(self, datos) #Inicializamos clase padre        

    def moda(self):
        '''Es el número que más se repite.'''
        frequency = {}
        modas = []
        for valor in self.datos:
            frequency[valor] = frequency.get(valor, 0) + 1
        frecuencia = self.maximo(frequency.values())
        for key, value in frequency.items():
            if value == frecuencia:
                modas.append(key)
        return modas

    def mediana(self):
        '''Calcular la mediana es justo el valor central, 
        es decir, el que se encuentra en la mitad de la lista. '''
        data = sorted(self.datos)
        # Cociente cuando a se divide por b, redondeado al
        # siguiente número entero más pequeño
        index = self.longitud() // 2

        # Si el conjunto de datos es impar
        if self.longitud() % 2 != 0:
            return data[index]

        # Si el conjunto de datos es par
        return (data[index - 1] + data[index]) / 2

    def media(self):
        '''Es el valor promedio del grupo datos, 
        la cifra que se obtiene al sumar todos los datos y dividir el 
        resultado entre la cantidad de los mismos. '''
        return self.suma() / self.longitud()
