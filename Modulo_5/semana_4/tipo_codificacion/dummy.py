import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Color': ['Rojo', 'Verde', 'Azul']}
df = pd.DataFrame(data)

# Aplicar la codificación dummy con k-1 columnas utilizando el método get_dummies
df_encoded = pd.get_dummies(df['Color'], prefix='Color', drop_first=True)

# Mostrar el DataFrame original y el DataFrame codificado
print("DataFrame original:")
print(df)
print("\nDataFrame codificado:")
print(df_encoded)
