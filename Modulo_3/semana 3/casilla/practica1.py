from tkinter import *

root = Tk()
root.config(bd=15)

leche = IntVar()      # 1 si, 0 no
azucar = IntVar()    # 1 si, 0 no

Label(root,text="¿Cómo quieres el café?").pack()
Checkbutton(root, text="Con leche", variable=leche,
            onvalue=1, offvalue=0).pack()
Checkbutton(root, text="Con azúcar",variable=azucar,
            onvalue=1, offvalue=0).pack()

root.mainloop()

