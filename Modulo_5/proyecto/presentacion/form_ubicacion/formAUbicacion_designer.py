import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandastable import Table
import util.generic as utl

class FormUbicacionDesigner(tk.Toplevel):   
    
    def __init__(self): 
        super().__init__() 
    
    def initialize_component(self): 
        self.config_window()   
        self.framePrincipal()      
        self.framePrincipalPanel1()
        self.framePrincipalPanel2()  
        self.tablaEstadisticosUbicacion()
        self.graficaUbicacion()    
    
    def config_window(self):
        self.title('Analisis de variable de ubicación')        
        w, h = 1400,500                                                                     
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='#f2f3f7')  
        utl.centrar_ventana(self,w,h)
        
    def framePrincipal(self):
        self.frame_zona_principal = tk.Frame(self, bd=0, relief=tk.SOLID, bg='#f2f3f7')
        self.frame_zona_principal.pack(side="top",fill=tk.BOTH )   
        
    def framePrincipalPanel1(self):
        self.frame_zona_principal_panel1 = tk.Frame(self.frame_zona_principal, bd=0, relief=tk.SOLID, bg='#f2f3f7', width=100, height=100)
        self.frame_zona_principal_panel1.pack(side="left",fill=tk.BOTH, expand="yes")
        
    def framePrincipalPanel2(self):
        self.frame_zona_principal_panel2 = tk.Frame(self.frame_zona_principal, bd=0,  relief=tk.SOLID, bg='#f2f3f7', width=100, height=100)
        self.frame_zona_principal_panel2.pack(side="left",fill=tk.BOTH, expand="yes")
        
    def tablaEstadisticosUbicacion(self):
        self.tablaDatosUbicacion = Table(self.frame_zona_principal_panel1, showtoolbar=False, showstatusbar=False, rows=8,width=500)
        self.tablaDatosUbicacion.show()  
        
    def graficaUbicacion(self):
        self.figure_ubicacion = plt.Figure(figsize=(50,10))      
        self.canvas_figure_ubicacion = FigureCanvasTkAgg(self.figure_ubicacion, self.frame_zona_principal_panel2)
        self.canvas_figure_ubicacion.get_tk_widget().pack(side=tk.LEFT, fill=tk.X, pady=20)    
    
   