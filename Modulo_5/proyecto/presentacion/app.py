import pandas as pd
from presentacion.app_designer import AppDesigner
from presentacion.form_edades.formEdades import FormEdades
from presentacion.form_ubicacion.formAUbicacion import FormUbicacion
from presentacion.form_precio.formAPrecio import FormPrecio

from util.constant import PATH_FILE

class App(AppDesigner):
    df = None
    
    def abrir_estadistico_ubicacion(self):
        FormUbicacion(self.df).mainloop()
    
    def abrir_estadistico_edad(self):
        FormEdades(self.df).mainloop()
        
    def abrir_estadistico_precio_area(self):
        FormPrecio(self.df).mainloop()

    def __init__(self):
        super().__init__()
        self.initialize_component() 
        self.carga_df() 
        self.carga_tabla()      
        
    def carga_df(self):
        self.df = pd.read_csv(PATH_FILE)
        self.df = self.df.replace(' ', pd.NA)
        self.df = self.df.dropna(subset=['edad_compra'])
        self.df = self.df.dropna(subset=['anio_venta'])
        self.df['edad_compra'] = pd.to_numeric(self.df['edad_compra'])
        self.df["anio_venta"] = self.df["anio_venta"].astype(str)
        self.df["Mes_venta"] = self.df["Mes_venta"].astype(
            str).str.pad(width=2, side='left', fillchar='0')
        
    def carga_tabla(self):
        self.tablaDatosDf.model.df = self.df