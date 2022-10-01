from math import sqrt
from operaciones.df import DF


class Distribucion_Frecuencia:
    """Las distribuciones de frecuencias son tablas en que se dispone 
    las modalidades de la variable por filas. En las columnas se dispone 
    el número de ocurrencias por cada valor, porcentajes, etc. La finalidad de las
    agrupaciones en frecuencias es facilitar la obtención de la información que contienen los datos."""
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
        dfs = []
        for intervalo in range(self.__intervalo):
            fi = self.calculo_fi(rango_ini=x_inicial,
                                 rango_final=(x_inicial+self.__amplitud),
                                 coleccion_numeros=self.__datos_agrupados)
            Fi += fi
            fr = self.calculo_fr(fi=fi, n=self.__n)
            Fr += fr            
            dfs.append(DF(valor_x=self.calculo_x(
                valor=x_inicial, amplitud=self.__amplitud),
                xi=self.calculo_xi(
                valor=x_inicial, amplitud=self.__amplitud),
                fi=fi, Fi=Fi, fr=fr, Fr=Fr))
            x_inicial += self.__amplitud

        return dfs

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
        return f"[{valor} - {valor + amplitud})"

    def calculo_xi(self, valor: float, amplitud: float) -> float:
        '''Marca de clase Xi'''
        return (valor + (valor + amplitud)) / 2

    def calculo_fi(self, rango_ini: float, rango_final: float, coleccion_numeros: list) -> int:
        '''Frecuencia absoluta'''
        maximo = max(coleccion_numeros)
        contador = 0
        for numero in coleccion_numeros:
            if (maximo == numero and (rango_ini <= numero <= rango_final)):
                contador += 1
            elif (rango_ini <= numero < rango_final):
                contador += 1
        return contador

    def calculo_fr(self, fi: float, n: int):
        '''Frecuencia relativa'''
        return fi / n   
