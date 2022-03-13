import tkinter
from tkinter import ttk

master=tkinter.Tk()
master.title("Botón en Tk")
master.geometry("450x350")

button1=ttk.Button(master, text="button1")
button1.place(x=100, y=100)

button2=tkinter.Button(master, text="button2")
button2.place(x=100, y=25)


master.mainloop()