# Una tienda tiene mucho éxito en dos de sus productos:
# Hot Wheels Remolque Tiburón y Funko Felpa. Suele hacer venta
# por correo y la empresa de logística les cobra por peso de
# cada paquete así que deben calcular el peso de los Hot Wheels Remolque
# Tiburón y Funko Felpa que saldrán en cada paquete a demanda.
# Cada Hot Wheels Remolque pesa 300 g y cada Funko Felpa 390 g. Escribir un
# programa que lea el número de Hot Wheels Remolque Tiburón y Funko Felpa
# vendidos en el último pedido y calcule el peso total del paquete que será enviado.
# Tomando en cuenta que los valores del peso de los juguetes son constantes.
from constantes import PESO_HOT_WHEELS_REMOLQUE_TIBURON
from constantes import PESO_FUNKO_FELPA


def calculo_peso(cantidad, peso):
    return cantidad * peso


numero_ventas_hot_wheel = int(input("Número de productos vendidos de Wheels Remolque Tiburón:"))
numero_ventas_funko_felpa = int(input("Número de productos vendidos de Funko Felpa:"))

peso_hot_wheel = calculo_peso(
    numero_ventas_hot_wheel, PESO_HOT_WHEELS_REMOLQUE_TIBURON)
peso_funko_felpa = calculo_peso(numero_ventas_funko_felpa, PESO_FUNKO_FELPA)
total_peso = peso_hot_wheel+peso_funko_felpa

print("El peso total del paqute que será enviado : ", str(total_peso))
