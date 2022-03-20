from tkinter import *

ventas = Tk()
ventas.title('PythonGuides')


img = PhotoImage(file='./click.png')
Button(
    ventas,
    image=img,
    command=None
).pack()

ventas.mainloop()