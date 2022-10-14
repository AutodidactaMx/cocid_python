import tkinter as tk
from tkinter import ttk, messagebox


class Formulario_Inicio_Sesion(tk.Tk):
     
    def verificar(self):
        usu = self.usuario.get()
        password = self.password.get()        
        if(usu == "root" and password == "1234") :
            messagebox.showinfo(message="Mensaje Correcto",title="Mensaje")           
        else:
            messagebox.showerror(message="La contraseña no es correcta",title="Mensaje")           
                 
    def frame_logo(self):
        self.frame_logo = tk.Frame(self, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10,bg='#3a7ff6')
        self.frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)       

    def frame_form(self):
        self.frame_form = tk.Frame(self, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        self.frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)

    def frame_form_top(self):
        self.frame_form_top = tk.Frame(self.frame_form,height = 50, bd=0, relief=tk.SOLID,bg='black')
        self.frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(self.frame_form_top, text="Inicio de sesion",font=('Times', 30), fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

    def frame_form_fill(self):
        self.frame_form_fill = tk.Frame(self.frame_form,  bd=0, relief=tk.SOLID,bg='#fcfcfc')
        self.frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)    

    def etiqueta_usuario(self):
        self.etiqueta_usuario = tk.Label(self.frame_form_fill, text="Usuario", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        self.etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)

    def entry_usuario(self):
        self.usuario = ttk.Entry(self.frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)
    
    def etiqueta_password(self):
        etiqueta_password = tk.Label(self.frame_form_fill, text="Contraseña", font=('Times', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
    
    def entry_password(self):
        self.password = ttk.Entry(self.frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")
    
    def boton_inicio(self):
        inicio = tk.Button(self.frame_form_fill,text="Iniciar sesion",font=('Times', 15),bg='#3a7ff6', bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20)   
    
    def config_ventana(self):
        self.title('Inicio de sesion')
        self.geometry('800x500')
        self.config(bg='#fcfcfc')
        self.resizable(width=0, height=0) 

    def __init__(self):  
        super().__init__()         
        self.config_ventana()                  
        self.frame_logo()   
        self.frame_form()
        self.frame_form_top()
        self.frame_form_fill()
        self.etiqueta_usuario()
        self.entry_usuario()
        self.etiqueta_password()
        self.entry_password()
        self.boton_inicio()

