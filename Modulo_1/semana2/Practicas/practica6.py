# Los impuestos para la declaración de la renta en un determinado país son los siguientes:
# Renta	Impuesto
# Menor que $1,000.00	5%
# Mayor igual que $1,000.00 y menor que $2,000.00	10%
# Mayor igual que $2,000.00 y menor $8,000.00	35%
# mayor igual que $8,000.00	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar.

def calcular_impuesto(renta):
    if(renta < 1000.00):
        return renta * 0.05
    elif(renta >= 1000.00 and renta < 2000.00):
        return renta * 0.10
    elif(renta >= 2000.00 and renta < 8000.00):
        return renta * 0.35
    elif(renta >= 8000.00):
        return renta * 0.45


renta_anual = float(input("Cual es su renta anual? : "))
print("El impuesto que debe de pagar es : ",
      str(calcular_impuesto(renta_anual)))
