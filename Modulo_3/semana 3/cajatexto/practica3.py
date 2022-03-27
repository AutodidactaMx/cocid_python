from tkinter import *
root = Tk()
texto = StringVar()
entry = Entry(root, textvariable=texto)
entry.pack(side=RIGHT)
label = Label(root, text="Nombre")
label .pack(side=LEFT)
root.mainloop()
