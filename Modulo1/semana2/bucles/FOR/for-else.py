 
for i in range(1, 4):
    print(i)
else:  # Se ejecuta por que no se rompio el for
    print("No Break\n")
 
for i in range(1, 4):
    print(i)
    break
else:  # No ejecuta por que no se rompio el for
    print("No Break")