diccionario = {'nombre' : 'ivan', 'edad' : 35, 'cursos': 
['Python','Django']}
diccionario[0] = 'pepe' 
for d in diccionario :    
    print(diccionario[d])

for clave in diccionario.keys():
  print(f"{clave}")  
for valor in diccionario.values():
  print(f"{valor}")    

for clave, valor in diccionario.items():  
    print(f"{clave} {valor}")  