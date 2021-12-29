def Switch(argument):
    switcher = {
        0: " Este es el caso cero",
        1: " Este es el caso uno",
        2: " Este es el caso dos",
    }
    return switcher.get(argument, "Ninguno")

argument = 1
print (Switch(argument))