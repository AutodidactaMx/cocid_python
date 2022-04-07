import tkinter as tk
import util.generic as utl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from controlador.mediciones_controlador import Mediciones

class AppDesigner(tk.Tk):
    frame_zone_bottom = None
    frame_zone_top = None
    frame_zone_bottom_left = None
    frame_zone_bottom_rigth = None
    
    def __init__(self): 
        super().__init__()        
            
    def config_window(self):
        self.title('Master panel')        
        w, h = 1024,900                                                                     
        self.geometry("%dx%d+0+0" % (w, h))
        self.config(bg='#3a7ff6')            
        utl.centrar_ventana(self,w,h)           
    def frameZoneTop(self):
        self.frame_zone_top = tk.Frame(self, bd=1, height=500, relief=tk.SOLID, bg='white')
        self.frame_zone_top.pack(side="top",fill=tk.X)
    
    def frameZoneBottom(self):
        self.frame_zone_bottom = tk.Frame(self, bd=0, relief=tk.SOLID, bg='white')
        self.frame_zone_bottom.pack(side="bottom",expand=tk.NO,fill=tk.BOTH)
    
    def frameZoneBottomLeft(self):
        self.frame_zone_bottom_left = tk.Frame(self.frame_zone_bottom, bd=0, height=400, relief=tk.SOLID, bg='white')
        self.frame_zone_bottom_left.pack(side="left",expand=tk.YES,fill=tk.BOTH)        
    
    def frameZoneBottomRight(self):
        self.frame_zone_bottom_rigth = tk.Frame(self.frame_zone_bottom, bd=0, relief=tk.SOLID, bg='white')
        self.frame_zone_bottom_rigth.pack(side="right",expand=tk.YES,fill=tk.BOTH)        
    
    def grafica_ventas(self):        
        self.figure_plot = plt.Figure()
        self.figure_plot.set_figheight(utl.cm_to_pixel(300))        
        self.canvas_figure_plot = FigureCanvasTkAgg(self.figure_plot, self.frame_zone_top)
        self.canvas_figure_plot.get_tk_widget().pack(side=tk.TOP, fill=tk.X)
    
    def grafica_ciudades(self):        
        self.figure_city = plt.Figure()
        self.canvas_figure_city = FigureCanvasTkAgg(self.figure_city, self.frame_zone_bottom_rigth)
        self.canvas_figure_city.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, ipadx=5, ipady=10)
    
    def grafica_genero(self):        
        self.figure_gender= plt.Figure()
        self.canvas_figure_gender = FigureCanvasTkAgg(self.figure_gender, self.frame_zone_bottom_left)
        self.canvas_figure_gender.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, ipadx=5, ipady=10)

                
    def initialize_component(self):                
        self.config_window()
        self.frameZoneTop()
        self.frameZoneBottomLeft()
        self.frameZoneBottomRight()
        self.grafica_ventas()
        self.grafica_ciudades()
        self.grafica_genero()
        
class App(AppDesigner):       
                          
    def __init__(self):        
        super().__init__()
        self.initialize_component()  
        self.load_graphic_plot()
        self.load_graphic_bar()
        self.load_graphic_pie()
        
    def load_graphic_plot(self):    
        med = Mediciones().obtener_ventas_dia()        
        ax1 = self.figure_plot.add_subplot()
        ax1.set_title('Ventas por dia')
        ax1.plot_date(med["key"], med["values"],linestyle='solid', color='g')
        ax1.set_ylabel('Ventas')
        ax1.set_xlabel('Dias')        
        #ax1.set_xticklabels(med["key"], rotation=30, fontdict={'horizontalalignment': 'center'})
        toolbar =NavigationToolbar2Tk(self.canvas_figure_plot , self.frame_zone_top)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.Y)
    
    def load_graphic_bar(self):    
        med = Mediciones().obtener_total_ciudades()
        ax1 = self.figure_city.add_subplot()
        ax1.set_title('Ciudades')
        ax1.bar(med["key"],med["values"],color=['black', 'red', 'green', 'blue', 'cyan'])
        ax1.set_ylabel('Total')
        ax1.set_xlabel('Ciudad')
        toolbar =NavigationToolbar2Tk(self.canvas_figure_city , self.frame_zone_bottom_rigth)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.Y)
    
    def load_graphic_pie(self):    
        med = Mediciones().obtener_total_genero()
        ax1 = self.figure_gender.add_subplot()        
        ax1.set_title('Generos')
        ax1.pie(med["values"],labels=med["key"],autopct='%1.1f%%',shadow=True,explode=[0,0.08])
        toolbar =NavigationToolbar2Tk(self.canvas_figure_gender , self.frame_zone_bottom_left)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.Y)
        
        
              
