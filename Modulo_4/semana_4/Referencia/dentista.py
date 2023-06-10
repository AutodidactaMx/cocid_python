'''
Supongamos que tienes un conjunto de datos 
que contiene información sobre tus clientes de dentista. 
El conjunto de datos tiene las siguientes columnas: "Nombre", 
"Edad", "Género", "Última visita", "Procedimiento", "Costo".
'''
import pandas as pd

# Crear un DataFrame con el conjunto de datos
data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Laura', 'Ana'],
    'Edad': [35, 42, 28, 50, 37],
    'Género': ['Hombre', 'Mujer', 'Hombre', 'Mujer', 'Mujer'],
    'Última visita': ['2022-10-15', '2023-01-02', '2023-03-20', '2023-05-10', '2023-06-05'],
    'Procedimiento': ['Limpieza', 'Extracción', 'Blanqueamiento', 'Limpieza', 'Empaste'],
    'Costo': [100, 200, 300, 80, 150]
}

df = pd.DataFrame(data)

# Imprimir el DataFrame
print(df)
'''
Ahora, supongamos que deseas obtener algunas 
estadísticas y realizar análisis sobre tus clientes.
Para empezar, puedes calcular la edad promedio de 
tus clientes y el costo promedio de los procedimientos realizados:
'''

# Calcular la edad promedio de los clientes
edad_promedio = df['Edad'].mean()

# Calcular el costo promedio de los procedimientos
costo_promedio = df['Costo'].mean()

# Imprimir los resultados
print("Edad promedio de los clientes:", edad_promedio)
print("Costo promedio de los procedimientos:", costo_promedio)

'''
Además, puedes realizar agrupaciones y 
contar cuántos clientes tienes por género y 
cuántos procedimientos has realizado en total:
'''
# Contar el número de clientes por género
clientes_por_genero = df['Género'].value_counts()

# Calcular el número total de procedimientos realizados
total_procedimientos = df['Procedimiento'].nunique()

# Imprimir los resultados
print("Número de clientes por género:")
print(clientes_por_genero)
print("\nNúmero total de procedimientos realizados:", total_procedimientos)
