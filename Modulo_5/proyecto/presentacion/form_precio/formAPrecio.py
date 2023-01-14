import numpy as np
import pandas as pd
import sidetable
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from presentacion.form_precio.formAPrecio_designer import FormPrecioDesigner
sns.set()

class FormPrecio(FormPrecioDesigner):
    df = None
    
    def __init__(self,df):
        super().__init__()
        self.df = df
        self.initialize_component()
        self.analisis_correlacion()
        self.analisis_coeficiente()
        self.analisis_predictivo()


    def analisis_correlacion(self):
        axes = self.figure_correlacion.subplots()        
        df_correlacion = self.df[["area_pies","Precio"]]        
        pd.plotting.scatter_matrix(df_correlacion, figsize=(5,5), marker = 'o', hist_kwds = {'bins': 10}, s = 30, alpha = 0.4,ax=axes)        
        axes.set_title("Relación entre Area y precio")        
        plt.show()
        
    def analisis_coeficiente(self):
        axes = self.figure_coeficiente.subplots()        
        df_converage = self.df[["area_pies","Precio"]]                                
        scaler = StandardScaler()
        scaled = scaler.fit_transform(df_converage[["area_pies","Precio"]])
        scaledT = scaled.T 
        covariance_matrix = np.cov(scaledT)                                
        sns.set(font_scale=1.5)
        
        hm = sns.heatmap(covariance_matrix,
                        cbar=True,
                        annot=True,
                        square=True,
                        fmt='.2f',
                        annot_kws={'size': 12},
                        yticklabels=["area_pies","Precio"],
                        xticklabels=["area_pies","Precio"],ax=axes)
   
    def analisis_predictivo(self):                                      
        
        x = self.df['area_pies'].values.reshape(-1, 1)
        y = self.df['Precio'].values.reshape(-1, 1)       
        
        modelo = linear_model.LinearRegression()
        modelo.fit(x, y)                  

        axes = self.figure_regresion.subplots()        
        axes.scatter(x, y, color="blue")        
        y_pred = modelo.predict(x)                   
        axes.plot(x, y_pred, color="red")
        axes.set_title("Regrescion lineal de precios")        
        axes.set_ylabel('Precios')
        axes.set_xlabel('Area')                  
        
        r2 =  r2_score(y, y_pred)
        self.lbl_r2.config(text=f"Bondad del ajuste de un modelo a la variable : {str(r2)}")
        
        
        