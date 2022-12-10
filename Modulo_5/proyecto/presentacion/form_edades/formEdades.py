import numpy as np
import pandas as pd
import seaborn as sns
import sidetable 
from util.generic import mod
import matplotlib.pyplot as plt
from presentacion.form_edades.formEdades_designer import FormEdadesDesigner
sns.set()
class FormEdades(FormEdadesDesigner):
      df = None          
      
      def __init__(self, df):  
        super().__init__() 
        self.df = df
        self.initialize_component()           
        self.analisis_edades()
        
      def tabla_estadisticos(self):        
        df_st = self.df
        df_st["GENERAL"] = "Data" 
        df_std = df_st.groupby(['GENERAL'])[["edad_compra"]].aggregate([np.mean,np.median,np.std,np.var, mod, pd.DataFrame.skew])        
        df_std.rename(columns = {'mean':'Media', 'median':'Mediana', 'mod':'Moda',"skew":"Sesgo","std":"Desv. Est.","var":"Varianza"}, inplace = True)        
        df_std_reset = df_std.T.reset_index()
        df_std_reset.rename(columns = {'level_0':'Nivel', 'level_1':'Estadisticos', 'Data':'Resultado'}, inplace = True)        
        self.tablaDatosDfEstadistico.model.df = df_std_reset[['Estadisticos','Resultado']]
      
      def analisis_edades(self):                  
        resumen_compra =  self.df.stb.freq(['edad_compra'])        
        resumen_compra = resumen_compra.sort_values(by='edad_compra', ascending=True)        
        self.barra_edades(resumen_compra)
        self.histograma_edades() 
        self.tabla_estadisticos()             
        
      def histograma_edades(self):
        axes = self.figure_histograma_edades.subplots()
        axes.set_title("Intervalos de la tabla de edades", fontsize=20)
        self.df['edad_compra'].plot.hist(bins=6,edgecolor='black', linewidth=1.2,ax=axes)                        
        plt.show()
        
      def barra_edades(self,resumen_compra):
        axes = self.figure_barra_edades.subplots()        
        axes.set_title("Distribución de frecuencias de la variable Edad", fontsize=20)
        resumen_compra.plot.bar(x='edad_compra', y='count',ax=axes)
        plt.show()
        