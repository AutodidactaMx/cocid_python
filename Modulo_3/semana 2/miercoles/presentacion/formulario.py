from tkinter import ttk, messagebox
import tkinter as tk
import dominio.controlador.controlador_flujo as controlador
from dominio.objetos.persona import Persona

class FormularioPersona:
    
    def construir(self):
        error = controlador.construir()
        if(error == 1):
            messagebox.showerror(message=f"La tabla debe de existir", title="Error")  
        else:
            messagebox.showinfo(message=f"La tabla creada", title="Error")    
                
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
            self.consulta()
            self.limpiar_campos()
    
    def eliminar(self):                
        curItem = self.tv.focus()
        fila = self.tv.item(curItem)
        afectados =controlador.eliminar_persona(fila["values"][0])
        if(afectados == 0):
            messagebox.showerror(message=f"Error al eliminar verifique la calve que no este repetida", title="Error")    
        else :
            messagebox.showinfo(message=f"Elimino con exito {afectados} registro", title="Eliminar")   
            self.consulta()
            self.limpiar_campos()
        
    
    def consulta(self):
        for i in self.tv.get_children():
            self.tv.delete(i)
        personas:list = controlador.consultar_persona()
        for idx, persona in enumerate(personas):        
            self.tv.insert(parent='', index=idx, iid=idx, text='', values=(persona.curp, persona.nombre,persona.edad,persona.correo,persona.telefono))


    def __init__(self, master):                
        
        master.config(bg='#0E9149') 
        
        #Crear tabla
        self.boton_construir = tk.Button(master, text="Construir", 
                                       font=("Calibri", 12, "bold"), fg="white", 
                                       bg="#2980b9", bd=0,command=self.construir)                       
        self.boton_construir.place(x=0, y=0)
        
        #Titulo
        self.label = tk.Label(master, text = "Formulario de persona")
        self.label.config(fg="white",font=("Verdana",15),bg='#747491') 
        self.label.pack(side="top" )

        #Curp
        self.label_curp = tk.Label(master, text = 'Curp :', fg="white",font=('calibre',10, 'bold') , bg='#747491')
        self.label_curp.place(x=20, y=60)
        self.entry_curp = tk.Entry(master, width = 65)
        self.entry_curp.place(x=100, y=60)

        #Nombre
        self.label_nombre = tk.Label(master, text = 'Nombre :', fg="white",font=('calibre',10, 'bold'), bg='#747491')
        self.label_nombre.place(x=20, y=100)
        self.entry_nombre = tk.Entry(master, width = 65)
        self.entry_nombre.place(x=100, y=100)

        #Edad
        self.label_edad = tk.Label(master, text = 'Edad :', fg="white",font=('calibre',10, 'bold'), bg='#747491')
        self.label_edad.place(x=20, y=140)
        self.entry_edad = tk.Entry(master, width = 65)
        self.entry_edad.place(x=100, y=140)

        #Correo
        self.label_correo = tk.Label(master, text = 'Correo :',fg="white", font=('calibre',10, 'bold'),bg='#747491')
        self.label_correo.place(x=20, y=180)
        self.entry_correo = tk.Entry(master, width = 65)
        self.entry_correo.place(x=100, y=180)

        #Telefono
        self.label_telefono = tk.Label(master, text = 'Telefono :', fg="white",font=('calibre',10, 'bold'),bg='#747491')
        self.label_telefono.place(x=20, y=220)
        self.entry_telefono = tk.Entry(master, width = 65)
        self.entry_telefono.place(x=100, y=220)

         #Guardar
        self.boton_guardar = tk.Button(master, text="Guardar", 
                                       font=("Calibri", 12, "bold"), fg="white", 
                                       bg="#16a085", bd=0,command=self.guardar)        
        self.boton_guardar.place(x=370, y=280)
        #Eliminar
        self.boton_eliminar = tk.Button(master,text="Eliminar",
                                         font=("Calibri", 12, "bold"), fg="white", 
                                         bg="#c0392b",bd=0, command=self.eliminar)        
        self.boton_eliminar.place(x=460, y=280)
        #Limpiar
        self.boton_limpiar = tk.Button(master,text="Limpiar",
                                        font=("Calibri", 12, "bold"), fg="white", 
                                        bg="#f39c12",bd=0, command=self.limpiar_campos)        
        self.boton_limpiar.place(x=285, y=280)
        
        #Tabla
        self.tv = ttk.Treeview(master,show='headings', height=8)
        self.tv['columns']=('Curp', 'Nombre', 'Edad','Correo','Telefono')
        self.tv.column('#0', width=0)
        self.tv.column('Curp',  width=100)
        self.tv.column('Nombre',  width=120)
        self.tv.column('Edad',  width=80)
        self.tv.column('Correo',  width=110)
        self.tv.column('Telefono',  width=100)

        self.tv.heading('#0', text='')
        self.tv.heading('Curp', text='Curp')
        self.tv.heading('Nombre', text='Nombre')
        self.tv.heading('Edad', text='Edad')
        self.tv.heading('Correo', text='Correo')
        self.tv.heading('Telefono', text='Telefono')
        
        self.tv.place(x=20, y=350)
        
        self.consulta()

        

    