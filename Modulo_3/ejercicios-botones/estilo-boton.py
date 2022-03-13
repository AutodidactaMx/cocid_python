# Import Required Module
from tkinter import *
from tkinter.ttk import *

# Create Root Object
root = Tk()

# Set Geometry(widthxheight)
root.geometry('400x200')

style = Style()
style.configure(
    "MyButton.TButton",
    foreground="#ff0000",
    background="#000000",
    padding=20,
    font=("Times", 12),
    anchor="w"
)
boton = Button(text="¡Hola, mundo!", style="MyButton.TButton")
boton.place(x=50, y=50)

boton2 = Button(root,text="¡Hola, mundo2!", style="MyButton.TButton")
boton2.place(x=100, y=100)

# Execute Tkinter
root.mainloop()