from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Botón en Tk")
window.geometry('400x200')
#Forma Tradicional
botonOriginal = Button(window, text="¡Botón Original!")
#Forma Tematica
botonTematico = ttk.Button(text="¡Botón Tematico!")
Button(window, text="¡Botón Original!")
botonTematico.place(x=100, y=100)
window.mainloop()