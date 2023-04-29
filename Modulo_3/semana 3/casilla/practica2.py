from tkinter import *

def cambiar_texto():
    labelResultado.config(text=f"{leche.get()} {azucar.get()}")

root = Tk()
root.config(bd=15)

leche = IntVar()      # 1 si, 0 no
azucar = IntVar()    # 1 si, 0 no

Label(root,text="¿Cómo quieres el café?").pack()
Checkbutton(root, text="Con leche", variable=leche, command=cambiar_texto,
            onvalue=1, offvalue=0).pack()
Checkbutton(root, text="Con azúcar",variable=azucar,
            onvalue=1, offvalue=0, command=cambiar_texto).pack()
# crear Label con texto inicial
labelResultado = Label(root, text="Texto inicial")
labelResultado.pack()


root.mainloop()
