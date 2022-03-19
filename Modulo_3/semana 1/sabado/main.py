import tkinter as tk
from  presentacion.formulario import FormularioPersona

def centrar_ventana(ventana):
    aplicacion_ancho = 550
    aplicacion_largo = 650
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")

try:    
    ventana=tk.Tk()
    centrar_ventana(ventana)
    ventana.title("Formulario")    
    ventana.config(bg='#fff')                        
    form = FormularioPersona(ventana)      
    
    ventana.mainloop()  
    
except Exception as e:
    print("Existe un error : ", e)
