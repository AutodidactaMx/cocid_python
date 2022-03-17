from tkinter import ttk, messagebox
import tkinter as tk
import dominio.controlador.controlador_flujo as controlador
from dominio.objetos.persona import Persona

class FormularioPersona:
    
    def limpiar_campos(self):
        self.entry_curp.delete(0,"end")
        self.entry_nombre.delete(0,"end")
        self.entry_edad.delete(0,"end")
        self.entry_correo.delete(0,"end")
        self.entry_telefono.delete(0,"end")
    
    def guardar(self):        
        
        p = Persona()
        p.curp = self.entry_curp.get()
        p.nombre = self.entry_nombre.get()
        p.edad = self.entry_edad.get()
        p.correo = self.entry_correo.get()
        p.telefono = self.entry_telefono.get()
        
        afectados =controlador.insertar_persona(p)
        if(afectados == 0):
            messagebox.showerror(message=f"Error al guardar verifique la calve que no este repetida", title="Error")    
        else :
            messagebox.showinfo(message=f"Guardado con exito {afectados} registro", title="Salvar")   
        self.limpiar_campos()
           
    def __init__(self, master):                
        
        #Titulo
        self.label = tk.Label(master, text = "Formulario de persona")
        self.label.config(fg="#000",font=("Verdana",15),bg='#fff') 
        self.label.pack(side="top" )

        #Curp
        self.label_curp = tk.Label(master, text = 'Curp :', font=('calibre',10, 'bold') , bg='#fff')
        self.label_curp.place(x=20, y=60)
        self.entry_curp = tk.Entry(master, width = 50)
        self.entry_curp.place(x=100, y=60)

        #Nombre
        self.label_nombre = tk.Label(master, text = 'Nombre :', font=('calibre',10, 'bold'), bg='#fff')
        self.label_nombre.place(x=20, y=100)
        self.entry_nombre = tk.Entry(master, width = 50)
        self.entry_nombre.place(x=100, y=100)

        #Edad
        self.label_edad = tk.Label(master, text = 'Edad :', font=('calibre',10, 'bold'), bg='#fff')
        self.label_edad.place(x=20, y=140)
        self.entry_edad = tk.Entry(master, width = 50)
        self.entry_edad.place(x=100, y=140)

        #Correo
        self.label_correo = tk.Label(master, text = 'Correo :', font=('calibre',10, 'bold'),bg='#fff')
        self.label_correo.place(x=20, y=180)
        self.entry_correo = tk.Entry(master, width = 50)
        self.entry_correo.place(x=100, y=180)

        #Telefono
        self.label_telefono = tk.Label(master, text = 'Telefono :', font=('calibre',10, 'bold'),bg='#fff')
        self.label_telefono.place(x=20, y=220)
        self.entry_telefono = tk.Entry(master, width = 50)
        self.entry_telefono.place(x=100, y=220)

        #Guardar
        self.boton_guardar = ttk.Button(master,text="Guardar", command=self.guardar)        
        self.boton_guardar.place(x=240, y=280)
        #Limpiar
        self.boton_limpiar = ttk.Button(master,text="Limpiar", command=self.limpiar_campos)        
        self.boton_limpiar.place(x=320, y=280)


    