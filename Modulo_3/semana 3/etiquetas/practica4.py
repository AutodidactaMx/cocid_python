from tkinter import *
root = Tk()
label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor=CENTER)
label.config(fg="blue", bg="green", font=("Verdana", 24))
root.mainloop()
