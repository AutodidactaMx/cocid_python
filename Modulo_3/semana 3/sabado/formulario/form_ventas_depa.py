import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tratamiento.proceso import *
import utileria.generico as utl

class FormularioVentaDep(tk.Toplevel):
    
    def consulta(self):
        for i in self.tv.get_children():
            self.tv.delete(i)
        ventas: list = ProcesoVentasDepartameto()
        if ventas:
            for ref, v in enumerate(ventas):
                self.tv.insert(parent='', index=ref, iid=ref, text='', values=(
                    v.tienda, v.departamento, v.ventas))    

    def __init__(self):
        super().__init__()        
        self.config_window()
        self.componente()

    def config_window(self):
        self.title('Analisis de ventas')
        w, h = 400, 500
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='white')
        utl.centrar_ventana(self, w, h)
        self.focus()
    
    def componente(self):
         # Titulo
        self.labelTitulo = tk.Label(self, text="Ventas por departamento")
        self.labelTitulo.config(fg="#666a88", font=("Verdana", 15), bg='#fcfcfc')
        self.labelTitulo.pack(side="top")

         # Tabla
        self.tv = ttk.Treeview(self, show='headings')         
        self.tv['columns'] = ('tienda', 'departamento', 'ventas')
        self.tv.column('#0', width=0)
        self.tv.column('tienda',  width=100)
        self.tv.column('departamento',  width=120)
        self.tv.column('ventas',  width=80)

        self.tv.heading('#0', text='')
        self.tv.heading('tienda', text='tienda')
        self.tv.heading('departamento', text='departamento')
        self.tv.heading('ventas', text='ventas')
        self.tv.pack(side="top", padx=10, pady=10)
        self.tv.config(height=400)

        self.consulta()

 