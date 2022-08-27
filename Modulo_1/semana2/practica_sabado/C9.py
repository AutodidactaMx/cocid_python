# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Escribir un programa que resuelva el siguiente descuento:
# El pago del predial realizado al estado tiene un descuento
# por edad de contribuyente de la siguiente manera :
# Mayor de 40 años           -  10%
# Entre 50 años y 60 años    -  25%
# Mayor de 60 años           -  50%
# Escribir un programa que pregunte al usuario su pago de predial
# y muestre por pantalla lo que tiene que pagar considerando el descuento si aplica.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def calcular_descuento(edad, valor):
    if (edad > 40 and edad < 50):
        return valor - (valor * 0.10)
    elif (edad >= 50 and edad < 60):
        return valor - (valor * 0.25)
    elif (edad >= 60):
        return valor - (valor * 0.50)
    else :
        return valor

predial = float(input("Indica la cantidad de predial : "))
edad = float(input("Cual es su edad? : "))
print("El pago considerando el descuento es: ",
      str(calcular_descuento(edad, predial)))
