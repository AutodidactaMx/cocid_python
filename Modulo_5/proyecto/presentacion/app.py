import pandas as pd
from presentacion.app_designer import AppDesigner
from presentacion.form_edades.formEdades import FormEdades
from presentacion.form_ubicacion.formAUbicacion import FormUbicacion
from presentacion.form_precio.formAPrecio import FormPrecio
from presentacion.form_agrupamiento.formAgrupamiento import FormAgrupamiento
from tkinter import messagebox

class App(AppDesigner):    
    
    def __init__(self):
        super().__init__()
        self.df = None
        self.initialize_component()         
        self.mainloop()  
        
    def abrir_estadistico_ubicacion(self):
        if(self.filename != None):
            FormUbicacion(self.df).mainloop()
        else :
            messagebox.showinfo(message="Debes elegir un archivo fuente",title="Mensaje")              
    
    def abrir_estadistico_edad(self):
        if(self.filename != None):
            FormEdades(self.df).mainloop()
        else :
            messagebox.showinfo(message="Debes elegir un archivo fuente",title="Mensaje")              
        
    def abrir_estadistico_precio_area(self):
        if(self.filename != None):
            FormPrecio(self.df).mainloop()
        else :
            messagebox.showinfo(message="Debes elegir un archivo fuente",title="Mensaje")              
    
    def abrir_estadistico_agrupamiento(self):
        if(self.filename != None):
            FormAgrupamiento(self.df).mainloop()
        else :
            messagebox.showinfo(message="Debes elegir un archivo fuente",title="Mensaje")              
           