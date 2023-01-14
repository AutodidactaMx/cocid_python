import tkinter as tk
import util.generic as utl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandastable import Table

class FormEdadesDesigner(tk.Toplevel):        
    
    def __init__(self): 
        super().__init__()
        
    def initialize_component(self): 
        self.config_window()  
        self.framePrincipal()        
        self.framePrincipalPanel1()
        self.framePrincipalPanel2()
        self.framePrincipalSecundario()
        self.tablaEstadisticos()
        self.graficaHistogramaEdades()
        self.graficaBarraEdades()
              
    
    def config_window(self):
        self.title('Analisis de variable de edades')        
        w, h = 1024, 900                                                                     
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='#f2f3f7')          
        utl.centrar_ventana(self,w,h)        
    
    def framePrincipal(self):
        self.frame_zona_principal = tk.Frame(self, bd=1, height=200, relief=tk.SOLID, bg='#f2f3f7')
        self.frame_zona_principal.pack(side="top",fill=tk.X )
        
    def framePrincipalPanel1(self):
        self.frame_zona_principal_panel1 = tk.Frame(self.frame_zona_principal, bd=0,  height=300, width=200, relief=tk.SOLID)
        self.frame_zona_principal_panel1.pack(side="left",fill=tk.X)
        
    def framePrincipalPanel2(self):
        self.frame_zona_principal_panel2 = tk.Frame(self.frame_zona_principal, bd=0,  height=300,relief=tk.SOLID, bg='#f2f3f7')
        self.frame_zona_principal_panel2.pack(side="left",fill=tk.X, expand="yes")
    
    def framePrincipalSecundario(self):
        self.frame_zona_principal_secundario = tk.Frame(self, bd=1,  height=300, relief=tk.SOLID, bg='#f2f3f7')
        self.frame_zona_principal_secundario.pack(side="top",fill=tk.BOTH, expand="yes")
     
    def tablaEstadisticos(self):
        self.tablaDatosDfEstadistico = Table(self.frame_zona_principal_panel1, showtoolbar=False, showstatusbar=False, width=200,height=200,rows=8)
        self.tablaDatosDfEstadistico.show()   
    
    def graficaHistogramaEdades(self):
        self.figure_histograma_edades = plt.Figure(figsize=(80,5), dpi=80)
        self.canvas_figure_historgrama_edades = FigureCanvasTkAgg(self.figure_histograma_edades, self.frame_zona_principal_panel2)
        self.canvas_figure_historgrama_edades.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    
    def graficaBarraEdades(self):
        self.figure_barra_edades= plt.Figure(figsize=(100,20), dpi=80)
        self.canvas_figure_barra_edades = FigureCanvasTkAgg(self.figure_barra_edades, self.frame_zona_principal_secundario)
        self.canvas_figure_barra_edades.get_tk_widget().pack(side=tk.LEFT,  ipady=10)

    
                    
 