import tkinter as tk
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from presentacion.app_designer import AppDesigner
import pandas as pd
from sklearn import linear_model
import sidetable 
import seaborn as sns
from pandastable import Table, TableModel
from sklearn.metrics import r2_score

sns.set()
class App(AppDesigner):           
    
    def __init__(self):  
        super().__init__()  
        self.df = None 
        self.modelo = None    
        self.initialize_component()   
        self.carga_data()
        self.entrenar_modelo()     
        self.coeficientes()      
        self.load_graphic()   
        
    def carga_data(self):
        self.df = pd.read_csv('./data/Bolsa_de_Valores.csv')                   
        
    def entrenar_modelo(self):
        '''
        Aquí tenemos 2 variables de entrada para la regresión múltiple. 
        Si solo desea usar una variable para la regresión lineal simple,
        use X = df['Interest_Rate'] por ejemplo. Alternativamente, puede 
        agregar variables adicionales entre corchetes
        '''
        x = self.df[['Interest_Rate','Unemployment_Rate']].astype(float) 
        '''
        Variable de salida (lo que estamos tratando de predecir)
        '''
        y = self.df['Stock_Index_Price'].astype(float) 
        
        '''
        Se entrena el modelo con los datos (X,Y)
        '''
        self.modelo = linear_model.LinearRegression()
        self.modelo.fit(x, y)
        y_pred = self.modelo.predict(x)
        self.lbl_r2.config(text=f"Estadístico R2: : {str(r2_score(y, y_pred))}")
    
    def coeficientes(self):
        '''
        Una vez entrenado el modelo podemos traer los valores de coeficientes β1 y β0
        '''
        self.lbl_coeficiente.config(text=f"Coeficientes Pendiente (β1) {str(self.modelo.coef_)}")        
        self.lbl_interceptor.config(text=f"Interseccion (β0) {str(self.modelo.intercept_)}")
        
        
    def load_graphic(self):                                 
        ax3 = self.figure_left.add_subplot()
        ax3.scatter(self.df['Interest_Rate'].astype(float),self.df['Stock_Index_Price'].astype(float), color = 'r')
        ax3.legend(['Stock_Index_Price']) 
        ax3.set_xlabel('Tasa de interés')
        ax3.set_ylabel(' Precio del índice bursátil')
        ax3.set_title('Tasa de interés vs. Precio del índice bursátil')
                
        ax4 = self.figure_right.add_subplot()
        ax4.scatter(self.df['Unemployment_Rate'].astype(float),self.df['Stock_Index_Price'].astype(float), color = 'g')        
        ax4.legend(['Stock_Index_Price']) 
        ax4.set_xlabel('Tasa de desempleo')
        ax3.set_ylabel(' Precio del índice bursátil')
        ax4.set_title('Tasa_desempleo vs. Precio del índice bursátil')
                
    def prediccion(self):     
        '''
        Al tener nuestro modelo preparado ahora procedemos hacer predicción 
        de los valores con apoyo de la variable independiente x aplicado al modelo
        para obtener valores de la variable dependiente Y
        '''    
        tasa_interes = float(self.txt_tasa_interes.get())             
        tasa_desempleo = float(self.txt_tasa_desempleo.get()) 
        prediccion = self.modelo.predict([[tasa_interes ,tasa_desempleo]])        
        self.lbl_prediccion.config(text=f"Precio del índice bursátil previsto: : {str(prediccion)}")
