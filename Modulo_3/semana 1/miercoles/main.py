import tkinter as tk
from  presentacion.formulario import FormularioPersona

def centrar_ventana(master):
    aplicacion_ancho = 450
    aplicacion_largo = 350
    pantall_ancho = master.winfo_screenwidth()
    pantall_largo = master.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return master.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")

try:    
    master=tk.Tk()
    centrar_ventana(master)
    master.title("Formulario")    
    master.config(bg='#fff')                    
    
    form = FormularioPersona(master)      
    
    master.mainloop()  
    
except Exception as e:
    print("Existe un error : ", e)
