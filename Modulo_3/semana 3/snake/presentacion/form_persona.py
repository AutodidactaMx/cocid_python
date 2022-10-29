from tkinter import ttk, messagebox
import tkinter as tk
import dominio.controlador.controlador_flujo as controlador
from persistencia.modelos import Persona
import utileria.generico as utl

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


    def __init__(self):                
        ventana=tk.Tk()        
        ventana.title("Formulario")     
        ventana.config(bg='#fcfcfc') 
        utl.centrar_ventana(ventana,550,650)        
        
        #Titulo
        self.label = tk.Label(ventana, text = "Formulario de persona")
        self.label.config(fg="#666a88",font=("Verdana",15),bg='#fcfcfc') 
        self.label.pack(side="top" )

        #Curp
        self.label_curp = tk.Label(ventana, text = 'Curp :', fg="#666a88",font=('calibre',10, 'bold') , bg='#fcfcfc')
        self.label_curp.place(x=20, y=60)
        self.entry_curp = ttk.Entry(ventana, width = 65)
        self.entry_curp.place(x=100, y=60)

        #Nombre
        self.label_nombre = tk.Label(ventana, text = 'Nombre :', fg="#666a88",font=('calibre',10, 'bold'), bg='#fcfcfc')
        self.label_nombre.place(x=20, y=100)
        self.entry_nombre = ttk.Entry(ventana, width = 65)
        self.entry_nombre.place(x=100, y=100)

        #Edad
        self.label_edad = tk.Label(ventana, text = 'Edad :', fg="#666a88",font=('calibre',10, 'bold'), bg='#fcfcfc')
        self.label_edad.place(x=20, y=140)
        self.entry_edad = ttk.Entry(ventana, width = 65)
        self.entry_edad.place(x=100, y=140)

        #Correo
        self.label_correo = tk.Label(ventana, text = 'Correo :',fg="#666a88", font=('calibre',10, 'bold'),bg='#fcfcfc')
        self.label_correo.place(x=20, y=180)
        self.entry_correo = ttk.Entry(ventana, width = 65)
        self.entry_correo.place(x=100, y=180)

        #Telefono
        self.label_telefono = tk.Label(ventana, text = 'Telefono :', fg="#666a88",font=('calibre',10, 'bold'),bg='#fcfcfc')
        self.label_telefono.place(x=20, y=220)
        self.entry_telefono = ttk.Entry(ventana, width = 65)
        self.entry_telefono.place(x=100, y=220)

         #Guardar
        self.boton_guardar = tk.Button(ventana, text="Guardar", 
                                       font=("Calibri", 12, "bold"), fg="white", padx=5, 
                                       bg="#3a7ff6", bd=0,command=self.guardar)        
        self.boton_guardar.place(x=370, y=280)
        self.boton_guardar.bind("<Return>", (lambda event: self.guardar ()))

        #Eliminar
        self.boton_eliminar = tk.Button(ventana,text="Eliminar",
                                         font=("Calibri", 12, "bold"), fg="white",  padx=5,
                                         bg="#c0392b",bd=0, command=self.eliminar)        
        self.boton_eliminar.bind("<Return>", (lambda event: self.eliminar()))
        self.boton_eliminar.place(x=460, y=280)
        #Limpiar
        self.boton_limpiar = tk.Button(ventana,text="Limpiar",
                                        font=("Calibri", 12, "bold"), fg="white",  padx=5,
                                        bg="#f39c12",bd=0, command=self.limpiar_campos)        
        self.boton_limpiar.place(x=285, y=280)
        self.boton_limpiar.bind("<Return>", (lambda event: self.limpiar_campos()))
        
        #CONSTRUIR
        self.boton_guardar = tk.Button(ventana, text="Construir", 
                                       font=("Calibri", 12, "bold"), fg="white", padx=5, 
                                       bg="#3a7ff6", bd=0,command=self.construir)        
        self.boton_guardar.place(x=0, y=0)
        self.boton_guardar.bind("<Return>", (lambda event: self.construir()))
        
        #Tabla
        self.tv = ttk.Treeview(ventana,show='headings', height=8)
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
                
        ventana.mainloop()
        
        
    