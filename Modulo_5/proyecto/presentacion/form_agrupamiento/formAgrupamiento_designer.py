import tkinter as tk
import util.generic as utl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandastable import Table

class FormAgrupamientoDesigner(tk.Toplevel):        
    
    def __init__(self): 
        super().__init__()
        
    def initialize_component(self): 
        self.config_window()  
        self.framePrincipal()   
        self.framePrincipalPanel1()                    
        self.framePrincipalPanel3()
        self.framePrincipalPanel2()             
        self.graficaAgrupacion()
        self.graficaCodo()
        self.graficaDispersion()
              
    
    def config_window(self):
        self.title('Analisis de variable de edades')        
        w, h = 1800, 500                                                                     
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='#f2f3f7')          
        utl.centrar_ventana(self,w,h)        
    
    def framePrincipal(self):
        self.frame_zona_principal = tk.Frame(self, bd=1, height=500, relief=tk.SOLID, bg='#f2f3f7')
        self.frame_zona_principal.pack(side="top",fill=tk.X )
    
    def frameSecundario(self):
        self.frame_zona_secundario = tk.Frame(self, bd=1, height=500, relief=tk.SOLID, bg='#f2f3f7')
        self.frame_zona_secundario.pack(side="top",fill=tk.X )
        
    def framePrincipalPanel1(self):
        self.frame_zona_principal_panel1 = tk.Frame(self.frame_zona_principal, bd=0,  height=500, relief=tk.SOLID, bg='red')
        self.frame_zona_principal_panel1.pack(side="left",fill=tk.BOTH, expand="yes")
        
    def framePrincipalPanel2(self):
        self.frame_zona_principal_panel2 = tk.Frame(self.frame_zona_principal, bd=0,  height=500,relief=tk.SOLID, bg='black')
        self.frame_zona_principal_panel2.pack(side="left",fill=tk.BOTH, expand="yes")
    
    def framePrincipalPanel3(self):
        self.frame_zona_principal_panel3 = tk.Frame(self.frame_zona_principal, bd=0,  height=500,relief=tk.SOLID, bg='black')
        self.frame_zona_principal_panel3.pack(side="right",fill=tk.BOTH, expand="yes")
    
    def graficaAgrupacion(self):
        self.figure_barra_edades= plt.Figure()
        self.canvas_figure_barra_edades = FigureCanvasTkAgg(self.figure_barra_edades, self.frame_zona_principal_panel2)
        self.canvas_figure_barra_edades.get_tk_widget().pack(side=tk.LEFT,  ipady=10)
    
    def graficaCodo(self):
        self.figure_codo= plt.Figure()
        self.canvas_figure_codo = FigureCanvasTkAgg(self.figure_codo, self.frame_zona_principal_panel3)
        self.canvas_figure_codo.get_tk_widget().pack(side=tk.RIGHT,  ipady=10)
    
    def graficaDispersion(self):
        self.figure_dispersion= plt.Figure()
        self.canvas_figure_dispersion = FigureCanvasTkAgg(self.figure_dispersion, self.frame_zona_principal_panel1)
        self.canvas_figure_dispersion.get_tk_widget().pack(side=tk.LEFT,  ipady=10)
    
                    
 