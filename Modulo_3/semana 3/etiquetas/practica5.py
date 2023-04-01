from tkinter import *
root = Tk()
texto = StringVar()
texto.set("Un nuevo texto")
label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor=CENTER)
label.config(fg="blue", bg="green",
font=("Verdana", 24), textvariable=texto)
root.mainloop()
