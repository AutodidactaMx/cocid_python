import tkinter as tk
import util.generic as utl
from pandastable import Table


class AppDesigner(tk.Tk):

    def __init__(self):
        super().__init__()
        
    def abrir_estadistico_edad(self):
        pass   
    def abrir_estadistico_ubicacion(self):
        pass   
    def abrir_estadistico_precio_area(self):
        pass

    def initialize_component(self):
        self.config_window()
        self.frameGeneral() 
        self.botonAbrirSeccion1()
        self.botonAbrirSeccion2()
        self.botonAbrirSeccion3()
        self.frameAbrirDatos()
        self.tablaDatos()

    def config_window(self):
        self.title('Analisis de bienes raices')
        w, h = 900, 500
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='white')
        utl.centrar_ventana(self, w, h)
        
    def frameGeneral(self):
        self.frame_general = tk.Frame(self, bd=0, relief=tk.SOLID, bg='white')
        self.frame_general.pack(side="top",fill=tk.BOTH, expand="yes")
    
    def botonAbrirSeccion1(self):
        self.btn_sta_edad = tk.Button(self.frame_general, font=('Times', 14) ,bg='#3a7ff6', bd=0,fg="#fff",text="Ver estadisticos Edad" , command=self.abrir_estadistico_edad)
        self.btn_sta_edad.pack(side=tk.TOP,fill=tk.X,padx=10,pady=10)   
        
    def botonAbrirSeccion2(self):
        self.btn_sta_ubicacion = tk.Button(self.frame_general, font=('Times', 14) ,bg='#3a7ff6', bd=0,fg="#fff",text="Ver estadisticos Ubicacion" , command=self.abrir_estadistico_ubicacion)
        self.btn_sta_ubicacion.pack(side=tk.TOP,fill=tk.X,padx=10,pady=10)   
        
    def botonAbrirSeccion3(self):
        self.btn_sta_edad_precio = tk.Button(self.frame_general,font=('Times', 14) ,bg='#3a7ff6', bd=0,fg="#fff", text="Ver estadisticos Precio vs Area" , command=self.abrir_estadistico_precio_area)
        self.btn_sta_edad_precio.pack(side=tk.TOP,fill=tk.X,padx=10,pady=10) 
    
    def frameAbrirDatos(self):
        self.frame_data = tk.Frame(self, bd=0, relief=tk.SOLID, bg='red')
        self.frame_data.pack(side="top",fill=tk.BOTH, expand="yes")    
    
    def tablaDatos(self):
        self.tablaDatosDf = Table(self.frame_data, showtoolbar=True, showstatusbar=True, rows=5)
        self.tablaDatosDf.show()    