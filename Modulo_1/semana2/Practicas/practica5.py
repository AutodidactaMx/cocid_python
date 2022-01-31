# Una panadería vende barras de pan a $8.90 cada una. El pan que no es
# el día tiene un descuento del 20%. Escribe un programa que comience
# leyendo el número de barras vendidas que no son del día. Como
# resultado debe imprimir en pantalla el precio habitual de una barra
# de pan, el descuento que se le hace por no ser fresca y el coste final total.
from constantes import PRECIO_BARRA_PAN as PRECIO
from constantes import DESCUENTO_PAN_VIEJO as DESCUENTO


def calculo_subtotal(numero_ventas):
    return numero_ventas * PRECIO


def calculo_descuentos(subtotal):
    return subtotal * DESCUENTO


def calculo_total(subtotal, descuentos):
    return subtotal - DESCUENTO


numero_barras_vendidas = float(
    input("Introduce el número de barras vendidas que no son del día : "))

subtotal = calculo_subtotal(numero_barras_vendidas)
descuentos = calculo_descuentos(subtotal)
total = calculo_total(subtotal, descuentos)

print("###############################################")
print("Subtotal del pan             : ", str(subtotal))
print("Descuentos no ser fresco     : ", str(descuentos))
print("Total a pagar                : ", str(total))
print("###############################################")
