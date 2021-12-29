
# Imprimiendo todas las letras excepto la 'p' and 's'
i = 0
a = 'datospordatos'
 
while i < len(a):
    if a[i] == 'p' or a[i] == 's':
        i += 1
        continue
         
    print('letra actual :', a[i])
    i += 1