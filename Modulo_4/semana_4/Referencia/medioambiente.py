import pandas as pd

# Crear un DataFrame con datos ficticios de energía y medio ambiente
data = {
    'Año': [2018, 2019, 2020, 2021],
    'Emisiones CO2 (millones de toneladas)': [120, 115, 110, 105],
    'Consumo de energía (terajulios)': [1500, 1450, 1420, 1380],
    'Generación de energía renovable (terajulios)': [200, 220, 240, 250]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print("Datos de Energía y Medio Ambiente:")
print(df)
print()

# Realizar análisis de los datos
# Calcular la media y el máximo de emisiones de CO2
media_emisiones_CO2 = df['Emisiones CO2 (millones de toneladas)'].mean()
max_emisiones_CO2 = df['Emisiones CO2 (millones de toneladas)'].max()

# Calcular el consumo total de energía y la proporción de energía renovable
consumo_energia_total = df['Consumo de energía (terajulios)'].sum()
proporcion_energia_renovable = df['Generación de energía renovable (terajulios)'].sum() / consumo_energia_total

# Mostrar los resultados del análisis
print("Análisis de Datos:")
print(f"Media de Emisiones de CO2: {media_emisiones_CO2} millones de toneladas")
print(f"Máximo de Emisiones de CO2: {max_emisiones_CO2} millones de toneladas")
print(f"Consumo Total de Energía: {consumo_energia_total} terajulios")
print(f"Proporción de Energía Renovable: {proporcion_energia_renovable * 100:.2f}%")
