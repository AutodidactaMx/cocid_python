import tkinter as tk
import util.generic as utl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class AppDesigner(tk.Tk):    
    frame_zone_bottom = None
    frame_zone_top = None
    frame_zone_bottom_left = None
    frame_zone_bottom_rigth = None
    
    def __init__(self): 
        super().__init__()    
            
    def prediccion(self) : 
        pass           
        
    def config_window(self):
        self.title('Master panel')        
        w, h = 1110,800                                                                     
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='white')            
        utl.centrar_ventana(self,w,h) 
    
    def frameZoneTop(self):
        self.frame_zone_top = tk.Frame(self, bd=1, height=200, relief=tk.SOLID, bg='white')
        self.frame_zone_top.pack(side="top",fill=tk.X)
        
    def frameZonebottom(self):
        self.frame_zone_bottom = tk.Frame(self, bd=1, height=900, relief=tk.SOLID, bg='white')
        self.frame_zone_bottom.pack(side="top",fill=tk.BOTH, expand="yes")
        
  
    def label_tasa_desempleo(self):
        self.lbl_tasa_desempleo = tk.Label(self.frame_zone_top, text='Tipo Tasa de desempleo: ', bg='white')
        self.lbl_tasa_desempleo.pack(fill=tk.X, padx=10,pady=2)        

    def label_tasa_interes(self):
        self.lbl_tasa_interes = tk.Label(self.frame_zone_top, text='Tipo Tasa de Interés: ', bg='white')
        self.lbl_tasa_interes.pack(fill=tk.X, padx=10,pady=2)
        
    def text_tasa_desempleo(self):
        self.txt_tasa_desempleo = tk.Entry(self.frame_zone_top,font=('Times', 14))
        self.txt_tasa_desempleo.pack(fill=tk.X, padx=10,pady=2)        

    def text_tasa_interes(self):
        self.txt_tasa_interes = tk.Entry(self.frame_zone_top, font=('Times', 14))
        self.txt_tasa_interes.pack(fill=tk.X, padx=10,pady=2)

    def buttom_prediccion(self):
        self.btn_prediccion = tk.Button (self.frame_zone_top, text='Predecir el precio del índice bursátil',command=self.prediccion, bg='orange')
        self.btn_prediccion.pack(fill=tk.X, padx=295,pady=2)   
    
    def label_interceptor(self):
        self.lbl_interceptor = tk.Label(self.frame_zone_top, bg='white', font=('Times', 14))
        self.lbl_interceptor.pack(fill=tk.Y,  padx=10,pady=2)        

    def label_coeficiente(self):
        self.lbl_coeficiente = tk.Label(self.frame_zone_top, bg='white', font=('Times', 14))
        self.lbl_coeficiente.pack(fill=tk.X,  padx=10,pady=2)  
    
    def label_r2(self):
        self.lbl_r2 = tk.Label(self.frame_zone_top, bg="white", font=('Times', 14))
        self.lbl_r2.pack(fill=tk.X,  padx=295 ,pady=2, expand="yes")        
    
    def label_prediccion(self):
        self.lbl_prediccion = tk.Label(self.frame_zone_top, bg='green', fg="white", font=('Times', 14))
        self.lbl_prediccion.pack(fill=tk.X,  padx=295 ,pady=2, expand="yes")        

    def grafica_left(self):        
        self.figure_left = plt.Figure()
        self.figure_left.set_figheight(utl.cm_to_pixel(300))        
        self.figure_left.set_figwidth(utl.cm_to_pixel(500)) 
        self.canvas_figure_left = FigureCanvasTkAgg(self.figure_left, self.frame_zone_bottom)
        self.canvas_figure_left.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,pady=20)
    def grafica_right(self):        
        self.figure_right = plt.Figure()
        self.figure_right.set_figheight(utl.cm_to_pixel(300))        
        self.figure_right.set_figwidth(utl.cm_to_pixel(500)) 
        self.canvas_figure_right = FigureCanvasTkAgg(self.figure_right, self.frame_zone_bottom)
        self.canvas_figure_right.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH,pady=20)    
        
    
    def initialize_component(self):                
        self.config_window()
        self.frameZoneTop()
        self.frameZonebottom()
        self.label_tasa_desempleo()
        self.text_tasa_desempleo()
        self.label_tasa_interes()
        self.text_tasa_interes()
        self.buttom_prediccion()
        self.label_interceptor()
        self.label_coeficiente()
        self.label_r2()
        self.label_prediccion()        
        self.grafica_left()
        self.grafica_right()
        