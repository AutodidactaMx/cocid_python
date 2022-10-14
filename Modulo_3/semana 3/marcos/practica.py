from tkinter import *
root = Tk()

# Hijo de root, no ocurre nada
frame = Frame(root)

# Empaqueta el frame en la raíz
frame.pack()

# Como no tenemos ningún elemento dentro del frame,
# no tiene tamaño y aparece ocupando lo mínimo posible, 0*0 px

# Color de fondo, background
frame.config(bg="lightblue")

# Podemos establecer un tamaño,
# la raíz se adapta al frame que contiene
frame.config(width=480,height=320)

root.mainloop()
