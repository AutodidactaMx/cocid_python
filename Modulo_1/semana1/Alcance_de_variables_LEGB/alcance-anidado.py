# Función de externa:
def fun(i):
    a = ["uno","dos","tres"]
    #Función anidada:
    def subfun():
        a.append(i)
        return a
    return subfun

test = fun("cuatro")
print(test())
