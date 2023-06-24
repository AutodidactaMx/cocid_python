import pandas as pd

# Creamos un DataFrame de ejemplo
data = {'Color': ['Rojo', 'Verde', 'Azul']}
df = pd.DataFrame(data)

# Aplicamos el one-hot encoding utilizando la función get_dummies de Pandas
one_hot_encoded = pd.get_dummies(df['Color'])

# Concatenamos las columnas codificadas con el DataFrame original
df_encoded = pd.concat([df, one_hot_encoded], axis=1)

# Mostramos el DataFrame original y el DataFrame codificado
print("DataFrame original:")
print(df)
print("\nDataFrame codificado (one-hot encoding):")
print(df_encoded)
