import tkinter as tk
import util.generic as utl
from tkinter import filedialog as fd
import pandas as pd


class AppDesigner(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.filename = None
        
    def carga_df(self):
        self.df = pd.read_csv(self.filename)
        self.df = self.df.replace(' ', pd.NA)
        self.df = self.df.dropna(subset=['edad_compra'])
        self.df = self.df.dropna(subset=['anio_venta'])
        self.df['edad_compra'] = pd.to_numeric(self.df['edad_compra'])
        self.df["anio_venta"] = self.df["anio_venta"].astype(str)
        self.df["Mes_venta"] = self.df["Mes_venta"].astype(
            str).str.pad(width=2, side='left', fillchar='0')        

    def initialize_component(self):
        self.config_window()
        self.frameTitulo()
        self.frameCuerpo()        
        self.botonAbrirSeccion1()
        self.botonAbrirSeccion2()
        self.botonAbrirSeccion3()
        self.botonAbrirSeccion4()

    def select_file(self):
        filetypes = ( ('text files', '*.csv'), ('All files', '*.*') )
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        self.label.config(text =  self.filename)
        self.focus() 
        self.carga_df()
    
    def abrir_estadistico_edad(self):
        pass   
    def abrir_estadistico_ubicacion(self):
        pass   
    def abrir_estadistico_precio_area(self):
        pass    
    def abrir_estadistico_agrupamiento(self):
        pass
    
    def config_window(self):        
        w, h = 1350, 400        
        self.config(bg='#f2f3f7')
        self.resizable(width=False, height=False)

        utl.centrar_ventana(self, w, h)   

    def frameCuerpo(self):
        self.frame_cuerpo = tk.Frame(self, bd=0, relief=tk.SOLID)
        self.frame_cuerpo.pack(side="top",fill=tk.BOTH, expand="yes")    
        self.frame_cuerpo.pack_propagate(0)

    def botonAbrirSeccion1(self):
        self.btn_sta_edad = tk.Button(self.frame_cuerpo, width=30, height=100, font=('Times', 15) ,bg='#e43a41', bd=0,fg="#fff",text="Ver Edad" , command=self.abrir_estadistico_edad)
        self.btn_sta_edad.pack(side=tk.LEFT, padx=10,pady=10)  

    def botonAbrirSeccion2(self):
        self.btn_sta_ubicacion = tk.Button(self.frame_cuerpo,width=30, height=100, font=('Times', 15) ,bg='#ef7a29', bd=0,fg="#fff",text="Ver Ubicacion" , command=self.abrir_estadistico_ubicacion)
        self.btn_sta_ubicacion.pack(side=tk.LEFT, padx=10,pady=10)
        
    def botonAbrirSeccion3(self):
        self.btn_sta_edad_precio = tk.Button(self.frame_cuerpo,width=30, height=100,font=('Times', 15) ,bg='#0072ee', bd=0,fg="#fff", text="Ver Precio vs Area" , command=self.abrir_estadistico_precio_area)
        self.btn_sta_edad_precio.pack(side=tk.LEFT, padx=10,pady=10) 
    
    def botonAbrirSeccion4(self):
        self.btn_sta_agrupamiento = tk.Button(self.frame_cuerpo,width=30, height=100,font=('Times', 15) ,bg='#AEB6BF', bd=0,fg="#fff", text="Ver Precio vs Edad de Compra" , command=self.abrir_estadistico_agrupamiento)
        self.btn_sta_agrupamiento.pack(side=tk.LEFT, padx=10,pady=10) 
    
    def frameTitulo(self):
        self.frame_titulo = tk.Frame(self, height=160, bd=0, relief=tk.SOLID, bg='#f2f3f7')
        self.frame_titulo.pack_propagate(0)
        self.frame_titulo.pack(side="top",fill=tk.X, padx=0, pady=15)     

        # Titulo
        self.labelTitulo = tk.Label(self.frame_titulo, text="Estudio de datos")
        self.labelTitulo.config( fg="#666a88", font=("Verdana", 25), bg='#f2f3f7')
        self.labelTitulo.pack(side="top")        

        self.boton_cargar_ruta = tk.Button(self.frame_titulo, text="Elegir archivo fuente",
                                       font=("Calibri", 12, "bold"), fg="white", padx=15,pady=10,
                                       bg="#888a8a", bd=0, command=self.select_file) 
        self.boton_cargar_ruta.pack(side="top",pady=15)   

        self.label = tk.Label(self.frame_titulo, text='', font=( 'calibre', 10, 'bold'), bg='#f2f3f7', padx=15,pady=10)
        self.label.pack(side="top" ,expand=True) 