'''
Para implementar la codificación ficticia en los datos, puede seguir los mismos pasos
realizados en la codificación one-hot. La única diferencia es que debe establecer 
el parámetro drop_first en True en lugar de False.
'''
import pandas as pd 

df = pd.read_csv('diamonds.csv')
'''
Ahora, vemos la forma del conjunto de datos codificado.
'''
one_hot = pd.get_dummies(df["color"],
                         prefix="color",
                         drop_first=False)
print(one_hot.shape)

dummy = pd.get_dummies(df["color"],
                         prefix="color",
                         drop_first=True)
print(dummy.shape)

'''
El conjunto de datos codificado tiene 24 variables. 
Esto se debe a que la codificación ficticia ha agregado 17 variables 
ficticias adicionales al codificar las variables categóricas. Entonces, 
la codificación ficticia también expande el espacio de características (dimensionalidad) en su conjunto de datos
'''

