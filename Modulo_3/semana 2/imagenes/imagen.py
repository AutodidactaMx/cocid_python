from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title('PythonGuides')


img = PhotoImage(file='./imagenes/logo.png')
img = img.subsample(4, 4)
Label(ventana, image=img ).pack(fill="both")

ventana.mainloop()