import tkinter as tk
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from controlador.mediciones_controlador import Mediciones
from presentacion.app_designer import AppDesigner

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
        
        