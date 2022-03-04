from error_salario import SalarioFueraRangoError
salario = float(input("Salario : "))

try:
    if(salario < 500):
        raise SalarioFueraRangoError
except ZeroDivisionError as e:
    print("Error de salario!")
except SalarioFueraRangoError as e:
    print("Error de salario!")
else:
    print("resultado es ", salario)
finally:
    print("Ejecuto al final de la clausula")
