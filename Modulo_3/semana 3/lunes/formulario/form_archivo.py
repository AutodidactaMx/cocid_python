import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tratamiento.proceso import *
import utileria.utileria.generico as utl

class FormularioArchivo:
    
    def select_file(self):
        filetypes = ( ('text files', '*.csv'), ('All files', '*.*') )
        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        self.label.config(text =  self.filename)
    
    def CargaDatosCsv(self):
        CargaDatos(self.filename)
        self.consulta()

    def consulta(self):
        for i in self.tv.get_children():
            self.tv.delete(i)
        ventas: list = ProcesoVentasDepartameto()
        if ventas:
           for idx, venta in enumerate(ventas):
                self.tv.insert(parent='', index=idx, iid=idx, text='', values=(
                    venta.tienda, venta.departamento, venta.ventas)) 
    def __init__(self):
        self.filename = None
        ventana = tk.Tk()
        ventana.title("Formulario")
        ventana.config(bg='#fcfcfc')
        utl.centrar_ventana(ventana, 650, 500)

         # Titulo
        self.labelTitulo = tk.Label(ventana, text="Cargar Un archivo")
        self.labelTitulo.config(fg="#666a88", font=("Verdana", 15), bg='#fcfcfc')
        self.labelTitulo.pack(side="top")

        self.boton_cargar_ruta = tk.Button(ventana, text="Abrir archivo",
                                       font=("Calibri", 12, "bold"), fg="white", padx=5,
                                       bg="#3a7ff6", bd=0, command=self.select_file)        
        self.boton_cargar_ruta.pack(expand=True)      

        self.label = tk.Label(ventana, text='', fg="#666a88", font=(
            'calibre', 10, 'bold'), bg='#fcfcfc')
        self.label.pack(expand=True)  

        
        self.boton_procesar = tk.Button(ventana, text="Carga archivo",
                                       font=("Calibri", 12, "bold"), fg="white", padx=5,
                                       bg="#3a7ff6", bd=0, command=self.CargaDatosCsv)        
        self.boton_procesar.pack(expand=True)  

        # Tabla
        self.tv = ttk.Treeview(ventana, show='headings')         
        self.tv['columns'] = ('tienda', 'departamento', 'ventas')
        self.tv.column('#0', width=0)
        self.tv.column('tienda',  width=100)
        self.tv.column('departamento',  width=120)
        self.tv.column('ventas',  width=80)

        self.tv.heading('#0', text='')
        self.tv.heading('tienda', text='tienda')
        self.tv.heading('departamento', text='departamento')
        self.tv.heading('ventas', text='ventas')
        self.tv.pack(expand=True)

        self.consulta()
        
        ventana.mainloop()




