'''
Supongamos que tienes dos series de datos financieros: 
el rendimiento diario de dos acciones, "AAPL" (Apple Inc.) y "MSFT" (Microsoft Corporation), 
durante un período de tiempo determinado. Queremos evaluar la correlación entre los 
rendimientos de estas dos acciones.
Primero, necesitamos obtener los datos de los rendimientos diarios de las acciones. 
Aquí hay un ejemplo de cómo podrías hacerlo utilizando la biblioteca yfinance para obtener los datos históricos de las acciones desde Yahoo Finance
'''
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# Obtener los datos históricos de las acciones
symbol1 = 'AAPL'
symbol2 = 'MSFT'
start_date = '2020-01-01'
end_date = '2021-12-31'

data = yf.download([symbol1, symbol2], start=start_date, end=end_date)['Adj Close']
data = data.pct_change().dropna()  # Calcular los rendimientos diarios y eliminar los valores faltantes

# Calcular la correlación
correlation = data[symbol1].corr(data[symbol2])

print("Correlación entre", symbol1, "y", symbol2, ":", correlation)

# Crear un gráfico de dispersión con línea de regresión
sns.set(style="darkgrid")
# La función regplot() de Seaborn se utiliza para trazar el gráfico de dispersión con la línea de regresión. 
# Los rendimientos diarios de "AAPL" se utilizan como la variable independiente (eje x) y 
# los rendimientos diarios de "MSFT" como la variable dependiente (eje y).
sns.regplot(x=data[symbol1], y=data[symbol2])
plt.xlabel(symbol1 + ' Devoluciones diarias')
plt.ylabel(symbol2 + ' Devoluciones diarias')
plt.title('Correlación lineal entre ' + symbol1 + ' y ' + symbol2)
plt.show()

''''
Este ejemplo te muestra cómo puedes utilizar la correlación lineal para 
evaluar la relación entre los rendimientos de dos acciones. Sin embargo, 
recuerda que la correlación no implica causalidad, y es importante tener en 
cuenta otros factores y análisis para tomar decisiones financieras informadas.
'''