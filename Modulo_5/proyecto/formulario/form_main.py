import tkinter as tk
import pandas as pd
import utileria.generico as utl
from utileria.generico import *
from procesamiento.proceso_carga import CargaVentasDatos, CargaVentasServiciosDatos
from formulario.form_carga_ventas import FormularioCargaVentas
from formulario.form_carga_ventas_servicio import FormularioCargaVentasServicio
from formulario.form_secundario import FormularioSecundario
import procesamiento.proceso_arranque_principal as proceso
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class FormularioMain(tk.Tk):

    def tablero_secundario(self):
        FormularioSecundario()

    def actualizar(self):
        self.dataframeVentas, self.dataframeServicios = proceso.cargaInicialDatos()
        if not self.dataframeVentas.empty and not self.dataframeServicios.empty:
            self.agregar_graficaF1()
            self.agregar_graficaF2()
            self.agregar_graficaF3()
            self.agregar_graficaF4()

    def carga_ventas(self):
        FormularioCargaVentas()
    
    def carga_ventas_servicios(self):
        FormularioCargaVentasServicio()

    def __init__(self):
        super().__init__()
        self.config_window()
        self.menu()
        self.panel()
        self.dataframeVentas, self.dataframeServicios = proceso.cargaInicialDatos()
        if not self.dataframeVentas.empty and not self.dataframeServicios.empty:
            self.agregar_graficaF1()
            self.agregar_graficaF2()
            self.agregar_graficaF3()
            self.agregar_graficaF4()
        self.mainloop()

    def agregar_graficaF1(self):        
        figura = plt.Figure()
        lienzo_figura = FigureCanvasTkAgg(figura, self.frame1 )
        lienzo_figura.get_tk_widget().pack(fill='both', expand=True)
        local =  self.dataframeVentas
        local['fecha_hora_venta'] = pd.to_datetime(local['fecha_hora_venta']) 
        local['dia'] = local['fecha_hora_venta'].dt.date         
        ventas_por_mes = local.groupby('dia')['total'].sum()        
        ax1 = figura.add_subplot()
        ax1.set_title('Ventas diarias')
        ax1.plot(ventas_por_mes.index,ventas_por_mes.values)
        ax1.set_ylabel('Ventas por dia')
        ax1.set_xlabel('Fechas')
    
    def agregar_graficaF2(self):    

        dias_semana = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo' }
        figura = plt.Figure()
        lienzo_figura = FigureCanvasTkAgg(figura, self.frame2 )
        lienzo_figura.get_tk_widget().pack(fill='both', expand=True)
        local = self.dataframeVentas
        local['fecha_hora_venta'] = pd.to_datetime(local['fecha_hora_venta'])
        local['dia_semana'] = local['fecha_hora_venta'].dt.dayofweek
        local['dia_semana'] = local['dia_semana'].map(dias_semana)
        ventas_por_dia_semana = local.groupby('dia_semana')['total'].sum()        

        ax1 = figura.add_subplot()
        ax1.set_title('Ventas por día de la semana')
        ax1.bar(x = ventas_por_dia_semana.index, height = ventas_por_dia_semana.values)        
        ax1.set_ylabel('Total de ventas')
        ax1.set_xlabel('Día de la semana')
        

    def agregar_graficaF3(self):        
        figura = plt.Figure()
        lienzo_figura = FigureCanvasTkAgg(figura, self.frame3 )
        lienzo_figura.get_tk_widget().pack(fill='both', expand=True)
        local = self.dataframeServicios
        local["n"] = 1
        acumualdos = local.groupby('servicio')['n'].sum()  
        # Filtrar el top con la mayor cantidad de ventas
        top_n = 5  # Número de elementos en el top que deseas mostrar
        top_servicios = acumualdos.nlargest(top_n)      
        ax1 = figura.add_subplot()
        ax1.set_title('Cantidad de ventas por servicio')
        ax1.barh(y = top_servicios.index, width = top_servicios.values)        
        ax1.set_ylabel('Total de ventas')
        ax1.set_xlabel('Día')
        
        

    def agregar_graficaF4(self):        
        figura = plt.Figure()
        lienzo_figura = FigureCanvasTkAgg(figura, self.frame4)
        lienzo_figura.get_tk_widget().pack(fill='both', expand=True)                 
            
        pagos = self.dataframeVentas.groupby('modo_pago')['total'].sum()        
        ax1 = figura.add_subplot()
        ax1.set_title('Ventas por método de pago')
        ax1.pie(pagos.values, labels=pagos.index, autopct='%1.1f%%')                        
        ax1.set_xlabel('')


    
    def config_window(self):
        self.title('Analisis de ventas')
        w, h = 900, 500
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='white')
        self.state('zoomed')
        utl.centrar_ventana(self, w, h)

    def menu(self):
        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
            label="Carga de ventas",
            command=self.carga_ventas,
            compound=tk.LEFT
        )
        menu_archivo.add_command(
            label="Carga de ventas servicios",
            command=self.carga_ventas_servicios,
            compound=tk.LEFT
        )
        menu_archivo.add_command(
            label="Indicadores secundarios",
            command=self.tablero_secundario,
            compound=tk.LEFT
        )
        menu_archivo.add_command(
            label="Actualizar",
            command=self.actualizar,
            compound=tk.LEFT
        )
        menu_archivo.add_separator()
        menu_archivo.add_command(
            label="Salir",
            command=self.destroy)
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
        self.config(menu=barra_menus)

    def panel(self):  

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.frame1 = tk.Frame(self, bg="red")
        self.frame2 = tk.Frame(self, bg="green")
        self.frame3 = tk.Frame(self, bg="blue")
        self.frame4 = tk.Frame(self, bg="yellow")

        # Ubica los frames en la cuadrícula utilizando grid
        self.frame1.grid(row=0, column=0, sticky="nsew")
        self.frame2.grid(row=0, column=1, sticky="nsew")
        self.frame3.grid(row=1, column=0, sticky="nsew")
        self.frame4.grid(row=1, column=1, sticky="nsew")
