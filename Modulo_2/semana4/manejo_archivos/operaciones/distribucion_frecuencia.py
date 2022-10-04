from math import sqrt


class Distribucion_Frecuencia:
    """Las distribuciones de frecuencias son tablas en que se dispone
    las modalidades de la variable por filas. En las columnas se dispone
    el número de ocurrencias por cada valor, porcentajes, etc.
    La finalidad de las agrupaciones en frecuencias es facilitar
    la obtención de la información que contienen los datos."""
    __datos_agrupados: list = []
    __minimo: float = 0
    __maximo: float = 0
    __rango: float = 0
    __n: float = 0
    __intervalo: float = 0
    __amplitud: float = 0

    def __init__(self, datos_agrupados: list):
        self.__datos_agrupados = datos_agrupados
        self.valores_calculo()

    def calculo(self) -> dict:
        """Tablas en que se dispone las modalidades de la variable retorna tabla :
        Valor , Marca de clase, Frecuencia absoluta,
        Frecuencia absoluta acumulada, Frecuencia relativa,
        Frecuencia reltavita acumulada
        Return : {
            "valor_x": lista_x,
            "xi": lista_xi,
            "fi":  lista_fi,
            "Fi": Lista_Fi,
            "fr": lista_fr,
            "Fr": lista_Fr
        }
        """
        x_inicial = self.__minimo
        Fi = 0
        Fr = 0
        lista_x = []
        lista_xi = []
        lista_fi = []
        Lista_Fi = []
        lista_fr = []
        lista_Fr = []
        for intervalo in range(self.__intervalo):
            lista_x.append(self.calculo_x(
                valor=x_inicial, amplitud=self.__amplitud))
            lista_xi.append(self.calculo_xi(
                valor=x_inicial, amplitud=self.__amplitud))
            fi = self.calculo_fi(rango_ini=x_inicial,
                                 rango_final=(x_inicial+self.__amplitud),
                                 coleccion_numeros=self.__datos_agrupados)
            lista_fi.append(fi)
            Fi += fi
            Lista_Fi.append(round(Fi, 2))
            fr = self.calculo_fr(fi=fi, n=self.__n)
            lista_fr.append(fr)
            Fr += fr
            lista_Fr.append(round(Fr, 2))
            x_inicial += self.__amplitud

        return {
            "valor_x": lista_x,
            "xi": lista_xi,
            "fi":  lista_fi,
            "Fi": Lista_Fi,
            "fr": lista_fr,
            "Fr": lista_Fr
        }

    def valores_calculo(self) -> None:
        '''Calculos iniciales
            Minimo, Maximo, Rango, Total, Inetrvalo, Amplitud
        '''
        self.__minimo = min(self.__datos_agrupados)
        self.__maximo = max(self.__datos_agrupados)
        self.__rango = self.__maximo-self.__minimo
        self.__n = len(self.__datos_agrupados)
        self.__intervalo = round(sqrt(self.__n))
        self.__amplitud = self.__rango / self.__intervalo

    def calculo_x(self, valor: float, amplitud: float) -> str:
        '''Valor de variable X'''
        return f"[{round(valor,2)} - {round(valor + amplitud,2)})"

    def calculo_xi(self, valor: float, amplitud: float) -> float:
        '''Marca de clase Xi'''
        return round(((valor + (valor + amplitud)) / 2), 2)

    def calculo_fi(self, rango_ini: float, rango_final: float,
                   coleccion_numeros: list) -> int:
        '''Frecuencia absoluta'''
        maximo = max(coleccion_numeros)
        contador = 0
        for numero in coleccion_numeros:
            if (maximo == numero and (rango_ini <= numero <= rango_final)):
                contador += 1
            elif(rango_ini <= numero < rango_final):
                contador += 1
        return contador

    def calculo_fr(self, fi: float, n: int):
        '''Frecuencia relativa'''
        return round(fi / n, 2)

    def mostrar_atributos(self) -> None:
        valor = f"Datos Agrupados : {self.__datos_agrupados} \n\r \
        Minimo : {self.__minimo} \n\r \
        Maximo : {self.__maximo} \n\r \
        Rango : {self.__rango}  \n\r \
        N : {self.__n} \n\r \
        Intervalo : {self.__intervalo} \n\r \
        Amplitud : {self.__amplitud} \n\r \
        "
        print(valor)

    def mostrar_tablas(self, tablas_df: dict) -> None:
        """Imprime en pantalla la tabla de distribuciones de frecuencias"""
        print("x".rjust(15, ' '),
              "xi".rjust(15, ' '),
              "fi".rjust(15, ' '),
              "Fi".rjust(15, ' '),
              "fr".rjust(15, ' '),
              "Fr".rjust(15, ' '))
        for vector in range(self.__intervalo):
            print(str(tablas_df['valor_x'][vector]).rjust(15, ' '),
                  str(tablas_df['xi'][vector]).rjust(15, ' '),
                  str(tablas_df['fi'][vector]).rjust(15, ' '),
                  str(tablas_df['Fi'][vector]).rjust(15, ' '),
                  str(tablas_df['fr'][vector]).rjust(15, ' '),
                  str(tablas_df['Fr'][vector]).rjust(15, ' '))
