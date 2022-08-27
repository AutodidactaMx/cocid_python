# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Escribir un programa que resuelva el siguiente problema : 
# Una tienda de Todo a un precio vende sus productos a $20.00. Los productos 
# con defectos se les da un 10% de descuento. Debe escribir un programa que 
# reciba cantidad de productos con defecto e imprima en pantalla el cálculo de la venta, 
# el precio habitual de producto, el descuento que se le hace por 
# ser defectuoso y el coste final total.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from constantes import PRODUCTO 
from constantes import DESCUENTO 


def calculo_subtotal(numero_ventas):
    return numero_ventas * PRODUCTO


def calculo_descuentos(subtotal):
    return subtotal * DESCUENTO


def calculo_total(subtotal, descuentos):
    return subtotal - descuentos


num_productos_defectos = float(
    input("Introduce el número de productos vendidas con defectos : "))

subtotal = calculo_subtotal(num_productos_defectos)
descuentos = calculo_descuentos(subtotal)
total = calculo_total(subtotal, descuentos)

print("###############################################")
print("Subtotal del producto        : ", str(subtotal))
print("Descuentos por defecto       : ", str(descuentos))
print("Total a pagar                : ", str(total))
print("###############################################")