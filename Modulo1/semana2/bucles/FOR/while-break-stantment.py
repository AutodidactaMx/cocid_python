
# Rompe el ciclo en cuanto detecta la 'p' or 's'
i = 0
a = 'datospordatos'
 
while i < len(a):
    if a[i] == 'p' or a[i] == 's':
        i += 1
        break
         
    print('Letra actual :', a[i])
    i += 1