# Imprime la siguiente tabla de multiplicar con ciclos:
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

for i in range(3, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
