import pandas as pd 

'''
Ahora, usamos el conjunto de datos de diamantes 
para ver ambos tipos de codificación en acción.
'''
df = pd.read_csv('diamonds.csv')
print(df.shape)
print(df.head())
'''
El conjunto de datos contiene 53.940 instancias y 10 variables.
Veamos si faltan valores en el conjunto de datos.
'''
print(df.isnull().sum().sum())

'''
Dado que esto devuelve 0, no faltan valores en el conjunto de datos.
Veamos cuántas variables categóricas hay en el conjunto de datos.
'''
print(df.info())

'''
Las variables categóricas tienen tipo de datos objeto o categoría.
Entonces, hay 3 variables categóricas en el conjunto de datos. Son corte, color y claridad.
Veamos las categorías o etiquetas únicas de la variable de corte.
'''
print(df["cut"].unique())

'''
Hay 5 categorías únicas en la variable de corte. Para codificar esta variable, 
necesitamos crear 5 variables ficticias en codificación one-hot y 
4 variables ficticias en codificación ficticia.
Asimismo, las variables de color y claridad tienen categorías únicas.
'''
print(df["color"].unique() )
print(df["clarity"].unique())


'''
Tanto la codificación one-hot como la dummy se pueden implementar en Pandas usando su función get_dummies.
Ahora, aplicamos la codificación one-hot solo a la variable de color y vemos los resultados.
'''

one_hot = pd.get_dummies(df["color"],
                         prefix="color",
                         drop_first=False)
'''
Esto devuelve un Pandas DataFrame de datos codificados. Veamos las primeras filas de la misma.
'''
print(one_hot)

'''
Vea cómo el texto especificado en el parámetro de prefijo se combina con los nombres de categoría de color.
Ahora, agregamos una codificación one-hot de la variable de color al conjunto de datos.
'''
one_hot_df = pd.get_dummies(df, prefix="color", 
                            columns=["color"], 
                            drop_first=False)
print(one_hot_df.head())

''''
Ahora, aplicamos codificación one-hot a todas las variables categóricas en el conjunto de datos.
'''
one_hot_df = pd.get_dummies(df, prefix={'color':'color',
                                        'cut':'cut',
                                        'clarity':'clarity'},
                            drop_first=False)
print(one_hot_df)
'''
Ahora, vemos la forma del conjunto de datos codificado.
'''
print(one_hot_df.shape)
''''
El conjunto de datos codificado tiene 27 variables. 
Esto se debe a que la codificación one-hot ha agregado 20 variables ficticias adicionales al codificar las variables categóricas.
Por lo tanto, la codificación one-hot expande el espacio de características (dimensionalidad) en su conjunto de datos.
'''