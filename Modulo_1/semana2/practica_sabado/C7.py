# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Escribir un programa que resuelva el siguiente problema : 
# Una zapatería vende con regularidad dos modelos de zapatos: 
# SNEAKER URBANO y BOTA OUTDOOR . 
# El equipo de logística debe calcular el costo de envío por pedidos, 
# el valor de  SNEAKER URBANO es de $1200.00; BOTA OUTDOOR es de $1340.00. 
# Se debe calcular el número de pares vendidos y calcular el valor total del envío. 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from constantes import SNEAKER_URBANO
from constantes import BOTA_OUTDOOR


def calculo_valor(cantidad, valor):
    return cantidad * valor


num_ven_sneaker = int(input("Número de pares de zapatos vendidos de SNEAKER URBANO:"))
num_ven_bota = int(input("Número de pares de zapatos vendidos de BOTA OUTDOOR:"))

valor_sneaker = calculo_valor(num_ven_sneaker, SNEAKER_URBANO)
valor_funko_felpa = calculo_valor(num_ven_bota, BOTA_OUTDOOR)
total = valor_sneaker+valor_funko_felpa

print("Calcular el valor total del envío : ", str(total))