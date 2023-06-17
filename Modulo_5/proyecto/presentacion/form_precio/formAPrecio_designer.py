import tkinter as tk
import util.generic as utl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FormPrecioDesigner(tk.Toplevel):
    
    def __init__(self): 
        super().__init__()
        
    def initialize_component(self):                
        self.config_window()           
        self.framePrincipal()
        self.framePrincipalPanel1()
        self.framePrincipalPanel2() 
        self.graficaCorrelacion()
        self.graficaCoeficiente()
        self.labelR2()
        self.graficaRegresion() 
    
    def config_window(self):
        self.title('Analisis de precios')        
        w, h = 1200,800                                                                     
        utl.centrar_ventana(self,w,h)        
        self.config(bg='#f2f3f7')
        self.state('zoomed')     

        
    def framePrincipal(self):
        self.frame_zona_principal = tk.Frame(self, bd=0, relief=tk.SOLID, width=300, height=300, bg='#f2f3f7')
        self.frame_zona_principal.pack(side="top" )
        
    def framePrincipalPanel1(self):
        self.frame_zona_principal_panel1 = tk.Frame(self.frame_zona_principal, bd=0, height=300,width=300, relief=tk.SOLID, bg='#f2f3f7')
        self.frame_zona_principal_panel1.pack(side="left",fill=tk.X ,expand="yes")
    
    def framePrincipalPanel2(self):
        self.frame_zona_principal_panel2 = tk.Frame(self.frame_zona_principal, bd=0, height=300, width=300,relief=tk.SOLID, bg='#f2f3f7')
        self.frame_zona_principal_panel2.pack(side="left",fill=tk.X ,expand="yes" )
   
    def graficaCorrelacion(self):
        self.figure_correlacion = plt.Figure()             
        self.canvas_figure_correlacion = FigureCanvasTkAgg(self.figure_correlacion, self.frame_zona_principal_panel1)
        self.canvas_figure_correlacion.get_tk_widget().pack(side=tk.LEFT ) 
    
    def graficaCoeficiente(self):
        self.figure_coeficiente = plt.Figure()             
        self.canvas_figure_coeficiente= FigureCanvasTkAgg(self.figure_coeficiente, self.frame_zona_principal_panel2)
        self.canvas_figure_coeficiente.get_tk_widget().pack(side=tk.LEFT, fill=tk.X) 
        
    def labelR2(self):
        self.lbl_r2 = tk.Label(self, font=('Times', 14) ,  anchor='center')
        self.lbl_r2.pack(fill=tk.X, padx=20,pady=5, expand="yes")

    def graficaRegresion(self):
        self.figure_regresion = plt.Figure(figsize=(100,8), dpi=70)             
        self.canvas_figure_regresion= FigureCanvasTkAgg(self.figure_regresion, self)
        self.canvas_figure_regresion.get_tk_widget().pack(side=tk.TOP, fill=tk.X ,expand="yes") 
    
             