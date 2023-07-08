from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
sns.set()
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from statsmodels.tsa.arima.model import ARIMA
import tkinter as tk
import pandas as pd
import utileria.generico as utl
from utileria.generico import *
import procesamiento.proceso_arranque_principal as proceso

class FormularioSecundario(tk.Toplevel):
    
    def __init__(self):
        super().__init__()
        self.config_window()        
        self.panel()
        self.dataframeVentas, self.dataframeServicios = proceso.cargaInicialDatos()
        self.agregar_graficaF1()
        self.agregar_graficaF2()
        self.agregar_graficaF3()        
        self.mainloop()

        
    def config_window(self):
        self.title('Analisis de ventas')
        w, h = 900, 500
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='white')
        self.state('zoomed')
        utl.centrar_ventana(self, w, h)

    
    def panel(self):          
        self.framearriba = tk.Frame(self, bg="black")
        self.framearriba.pack(side=tk.TOP, padx=10, pady=10,fill='both', expand=True)

        self.frameabajo = tk.Frame(self, bg="white")
        self.frameabajo.pack(side=tk.BOTTOM,padx=10, pady=10,fill='both', expand=True)


        self.frame1 = tk.Frame(self.framearriba, bg="red")
        self.frame1.pack(side=tk.LEFT, padx=10, pady=10,fill='both', expand=True)
        self.frame2 = tk.Frame(self.framearriba, bg="green")
        self.frame2.pack(side=tk.RIGHT, padx=10, pady=10,fill='both', expand=True)
        self.frame3 = tk.Frame(self.frameabajo, bg="blue")
        self.frame3.pack( padx=10, pady=10,fill='both', expand=True)

    def agregar_graficaF1(self):        
        scaler = StandardScaler()

        df = self.dataframeServicios        
        data = df.groupby('servicio').agg({
            'total': 'sum'
        })
        data_scaled = scaler.fit_transform(data)        
        kmeans = KMeans(n_clusters=3)  # Especifica el número de clusters deseado
        kmeans.fit(data_scaled)        
        data['cluster'] = kmeans.labels_

        # Visualizar los resultados del clustering
        figura = plt.Figure()
        lienzo_figura = FigureCanvasTkAgg(figura, self.frame3 )
        lienzo_figura.get_tk_widget().pack(fill='both', expand=True)
        
        ax1 = figura.add_subplot()
        ax1.scatter(data.index, data['total'], c=data['cluster'], cmap='viridis')            
        


    def agregar_graficaF2(self):        
        df = self.dataframeVentas
        x = df['total'].values.reshape(-1, 1) ### El promedio de trabajo de las personas 
        y = df['propina'].values.reshape(-1, 1) ### Salario de las persona


        modelo = linear_model.LinearRegression()
        modelo.fit(x, y)          

        y_pred = modelo.predict(x)
        # Visualizar los resultados del clustering
        figura = plt.Figure()
        lienzo_figura = FigureCanvasTkAgg(figura, self.frame2 )
        lienzo_figura.get_tk_widget().pack(fill='x', expand=True)
        barra_herramientas = NavigationToolbar2Tk(lienzo_figura, self.frame2)
        barra_herramientas.update()
        
        ax1 = figura.add_subplot()
        ax1.plot(x, y_pred, color='red')
        ax1.scatter(x, y)
        entrada = [[3000],[4000],[5000]]
        prediccion_modelo = modelo.predict(entrada)                
        ax1.scatter(entrada, prediccion_modelo, color="red")
        ax1.plot(entrada, prediccion_modelo, color="black")
        
        


    def agregar_graficaF3(self):        

        df = self.dataframeVentas

        df['fecha_hora_venta_dt'] = pd.to_datetime(df['fecha_hora_venta'])
        df['fecha'] = df['fecha_hora_venta_dt'].dt.date
        df_v = df[["fecha","total"]]


        df_ventas = df_v.groupby('fecha').agg({
            'total': 'sum'
        })

        df_ventas = df_ventas.sort_values('fecha',ascending=False)

        X = (df_ventas.values)        
        train, test = X, X
        history = [x for x in train]


        predictions = list()
        for t in range(30):    
            model_train = ARIMA(history, order=(1,1,3))
            modelo_train_fit = model_train.fit()
            output = modelo_train_fit.forecast()    
            yhat = output[0]
            predictions.append(yhat) 
            obs = test[t]
            history.append(obs)    
            

        # Realizar predicciones
        dias_predecir = pd.date_range(start=df_ventas.index[1], periods=31, freq='D')[1:]

        predicciones = pd.DataFrame(predictions, columns=['total_pro'])

        # Visualizar los resultados del clustering
        figura = plt.Figure()
        lienzo_figura = FigureCanvasTkAgg(figura, self.frame1 )
        lienzo_figura.get_tk_widget().pack(fill='both', expand=True)
        
        ax1 = figura.add_subplot()
        
        # Graficar los datos originales y las predicciones
        
        ax1.plot(df_ventas.index, df_ventas['total'], label='Datos originales')
        ax1.plot(dias_predecir, predicciones['total_pro'], label='Predicciones')
        ax1.title('Modelo ARIMA - Predicciones')
        ax1.legend()        



