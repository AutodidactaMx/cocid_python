variable1 = "variable original"
def variable_global():
    global variable1
    variable1 = "variable global modificada"

print(variable1)
#variable original
variable_global()
print(variable1)
#variable global modificada
