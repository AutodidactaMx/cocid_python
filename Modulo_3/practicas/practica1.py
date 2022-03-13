from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('250x100')
root.title('Practica 1')
Label(root, text='Ejercicio con botones', font=(
    'Verdana', 15)).pack(side=TOP, pady=10)

photo = PhotoImage(file=r"C:/Users/jesus/OneDrive/Imágenes/click.png")

# Resizing image to fit on button
photoimage = photo.subsample(3, 3)

Button(root, text='Click Me !', image=photoimage,
       compound=LEFT).pack(side=TOP)

mainloop()
