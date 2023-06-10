import pandas as pd
'''
Supongamos que tienes un conjunto de datos que 
contiene información sobre los gastos mensuales 
de una empresa en diferentes categorías. 
El conjunto de datos tiene las siguientes columnas: "Categoría", "Mes", "Gasto".'''
# Crear un DataFrame con el conjunto de datos
data = {
    'Categoría': ['Sueldos', 'Suministros', 'Publicidad', 'Alquiler', 'Otros'],
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Gasto': [5000, 2000, 3000, 4000, 1500]
}

df = pd.DataFrame(data)

# Imprimir el DataFrame
print(df)
'''
Ahora, supongamos que deseas calcular el gasto total por 
categoría y el gasto promedio por mes. Puedes utilizar las 
funciones de agregación de Pandas para realizar estos cálculos:
'''
# Calcular el gasto total por categoría
gasto_total = df.groupby('Categoría')['Gasto'].sum()

# Calcular el gasto promedio por mes
gasto_promedio = df.groupby('Mes')['Gasto'].mean()

# Imprimir los resultados
print("Gasto total por categoría:")
print(gasto_total)
print("\nGasto promedio por mes:")
print(gasto_promedio)
