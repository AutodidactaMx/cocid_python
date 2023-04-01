import tkinter as tk
from tratamiento.proceso import *
import utileria.generico as utl
from formulario.form_carga import FormularioCargaArchivo
from formulario.form_ventas_depa import FormularioVentaDep
from utileria.generico import *

class FormularioMain(tk.Tk):

    def archivo_nuevo_presionado(self):
        FormularioCargaArchivo()
    
    def ventas_departamento(self):
        FormularioVentaDep()

    def __init__(self):
        super().__init__()
        self.config_window()
        self.menu()
        self.panel()
        self.mainloop()
    
    def config_window(self):
        self.title('Analisis de bienes raices')
        w, h = 900, 500
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='white')
        utl.centrar_ventana(self, w, h)

    def menu(self):
        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
            label="Carga",
            command=self.archivo_nuevo_presionado,
            compound=tk.LEFT
        )
        menu_archivo.add_command(
            label="Ventas por departamento",
            command=self.ventas_departamento,
            compound=tk.LEFT
        )
        menu_archivo.add_separator()
        menu_archivo.add_command(
            label="Salir",
            command=self.destroy)
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
        self.config(menu=barra_menus)

    def panel(self):
        self.logo = utl.leer_imagen("./formulario/img/logo.png", (200, 200))
        self.frame_logo = tk.Frame(self, bd=0, width=300,
                              relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        self.frame_logo.pack(side="left",expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(self.frame_logo, image=self.logo,bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)
