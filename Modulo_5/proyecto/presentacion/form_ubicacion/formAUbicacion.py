import seaborn as sns
import matplotlib.pyplot as plt
from presentacion.form_ubicacion.formAUbicacion_designer import FormUbicacionDesigner
sns.set()

class FormUbicacion(FormUbicacionDesigner):    
    
    def __init__(self,df):
        super().__init__()
        self.df = df
        self.initialize_component()  
        self.analisis_ubicacion()    
    
    def analisis_ubicacion(self):
        resumen =  self.df.stb.freq(['Estado'])        
        resumen_reset = resumen.reset_index()
        resumen_reset.rename(columns = {'Estado':'Estado','count':'Frecuencia', 'percent':'Frecuencia relativa', 'cumulative_count':'Frecuencia acumulativa',"cumulative_percent":"Acumulativa"}, inplace = True)        
        self.tabla_resumen(resumen_reset)
        self.grafica(resumen_reset)
    
    def tabla_resumen(self,resumen):
        self.tablaDatosUbicacion.model.df  = resumen[["Estado","Frecuencia","Frecuencia relativa","Frecuencia acumulativa","Acumulativa"]]
   
    def grafica(self,resumen):
        axes = self.figure_ubicacion.subplots()
        ax = resumen.plot.bar(x='Estado', y='Frecuencia',  ax=axes,  color=(0.2, 0.4, 0.6, 0.6))
        ax.set_ylabel('Frecuencia')
        ax2 = resumen.plot.line(x='Estado', y='Acumulativa',  marker='o', secondary_y=True, ax=ax, color = 'orange')
        ax2.set_ylim(0, 100)
        ax2.set_ylabel('Acumulativa')
        ax2.set_title("Ubicacion Segmentación por Estado")
        plt.show()