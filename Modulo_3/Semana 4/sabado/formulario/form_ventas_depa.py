import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tratamiento.proceso import *
import utileria.generico as utl
from modelos.modelo_cbx import ModeloCombo
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class FormularioVentaDep(tk.Toplevel):

    def __init__(self):
        super().__init__()
        self.comboList = []
        self.seleccionadoDepa = 0
        self.config_window()
        self.componente()

    def consulta(self):
        for i in self.tv.get_children():
            self.tv.delete(i)
        ventas: list = ProcesoVentasDepartameto(self.seleccionadoDepa)
        if ventas:
            for ref, v in enumerate(ventas):
                self.tv.insert(parent='', index=ref, iid=ref, text='', values=(
                    v.tienda, v.departamento, v.ventas))
        departamentos = list(map(lambda v : v.departamento, ventas))
        total_ventas = list(map(lambda v : v.ventas, ventas))
        #clear subplots        
        self.graficaBar.cla()        
        self.graficaBar.set_title('Ventas por departamento')
        self.graficaBar.set_ylabel('Ventas')
        self.graficaBar.set_xlabel('Departamentos')           
        self.graficaBar.bar(departamentos, total_ventas,width = 0.5)
        self.canvas_figure_plot.draw()  
        

    def comboDepartamento(self):
        self.comboList = []
        self.comboList.append(ModeloCombo(0, f"Todos"))
        self.comboList.extend(ObtenerDepartementos())
        self.combo['values'] = self.comboList
        self.combo.set("Todos")

    def seleccionDepa(self, event):        
        valor = list(filter(lambda x: x.descripcion == self.combo.get(), self.comboList)).pop()
        self.seleccionadoDepa = valor.id
        self.consulta()

    def config_window(self):
        self.title('Analisis de ventas')
        w, h = 800, 500
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='white')
        utl.centrar_ventana(self, w, h)
        self.focus()

    def componente(self):
        # Zona arriba
        self.frame_zone_top = tk.Frame(self, bd=0, height=200, relief=tk.SOLID, bg='white')
        self.frame_zone_top.pack(side="top",fill=tk.X)

         # Titulo
        self.labelTitulo = tk.Label(self.frame_zone_top, text="Ventas por departamento")
        self.labelTitulo.config(
            fg="#666a88", font=("Verdana", 15), bg='#fcfcfc')
        self.labelTitulo.pack(side="top")
        
         # Label departamentos
        self.labelTitulo = tk.Label(self.frame_zone_top, text="Departamentos")
        self.labelTitulo.config(
            fg="#666a88", font=("Verdana", 12), bg='#fcfcfc')
        self.labelTitulo.pack(side="top")
        # Combo
        self.combo = ttk.Combobox(self.frame_zone_top, state="readonly")
        self.combo.bind("<<ComboboxSelected>>", self.seleccionDepa)
        self.combo.pack(side="top")

        #Zona abajo
    
        self.frame_zone_bottom = tk.Frame(self, bd=0, height=200, relief=tk.SOLID, bg='white')
        self.frame_zone_bottom.pack(side="bottom",expand=tk.YES,fill=tk.X)

        self.frame_zone_bottom_left = tk.Frame(self.frame_zone_bottom, bd=0,  relief=tk.SOLID, bg='white')
        self.frame_zone_bottom_left.pack(side="left",expand=tk.YES,fill=tk.BOTH)        
    
        # Tabla
        self.tv = ttk.Treeview(self.frame_zone_bottom_left, show='headings')
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
        

        # Grafica        
        self.frame_zone_bottom_rigth = tk.Frame(self.frame_zone_bottom, bd=0, relief=tk.SOLID, bg='red')
        self.frame_zone_bottom_rigth.pack(side="right",expand=tk.YES,fill=tk.BOTH)        
        self.figure_plot = plt.Figure()
        
        self.canvas_figure_plot = FigureCanvasTkAgg(self.figure_plot, self.frame_zone_bottom_rigth)
        self.canvas_figure_plot.get_tk_widget().pack(side=tk.TOP,expand=tk.YES, fill=tk.BOTH)
        self.graficaBar = self.figure_plot.add_subplot() 
        
        self.comboDepartamento()
        self.consulta()

       
