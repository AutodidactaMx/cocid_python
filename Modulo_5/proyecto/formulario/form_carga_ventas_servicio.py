import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog as fd
from procesamiento.proceso_carga import *
import utileria.generico as utl

class FormularioCargaVentasServicio(tk.Toplevel):
    
    def select_file(self):
        filetypes = ( ('text files', '*.csv'), ('All files', '*.*') )
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        self.label.config(text =  self.filename)
        self.focus()

    def CargaDatosCsv(self):
        CargaVentasServiciosDatos(self.filename)     
        messagebox.showinfo(message="Termino la carga",title="Mensaje")              
        self.destroy()

    def __init__(self):
        super().__init__()        
        self.config_window()
        self.componente()

    def config_window(self):
        self.title('Carga de datos')
        w, h = 900, 200
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='white')
        utl.centrar_ventana(self, w, h)
        self.focus()
    
    def componente(self):
         # Titulo
        self.labelTitulo = tk.Label(self, text="Cargar un archivo servicios")
        self.labelTitulo.config(fg="#666a88", font=("Verdana", 15), bg='#fcfcfc')
        self.labelTitulo.pack(side="top")

        self.boton_cargar_ruta = tk.Button(self, text="Elegir archivo de carga",
                                       font=("Calibri", 12, "bold"), fg="white", padx=2,
                                       bg="#5DADE2", bd=0, command=self.select_file)        
        self.boton_cargar_ruta.pack(expand=True)   

        self.label = tk.Label(self, text='---------------------', fg="#666a88", font=(
            'calibre', 10, 'bold'), bg='#fcfcfc')
        self.label.pack(expand=True) 

        self.boton_procesar = tk.Button(self, text="Inicial proceso carga",
                                       font=("Calibri", 12, "bold"), fg="white", padx=5,
                                       bg="#3a7ff6", bd=0, command=self.CargaDatosCsv)        
        self.boton_procesar.pack(expand=True) 

 