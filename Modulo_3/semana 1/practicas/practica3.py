import tkinter as tk
from tkinter import messagebox, ttk


def saludar(event=None):
    messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")


root = tk.Tk()
root.config(width=300, height=200)
root.title('Practica 3')
root.title("Botón en Tk")
boton = ttk.Button(text="¡Hola, mundo!", command=saludar)
boton.bind("<Return>", saludar)
boton.place(x=50, y=50)
root.mainloop()