from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title('PythonGuides')


img = PhotoImage(file='./logo.png')
img = img.subsample(3, 3)
Label( ventana, image=img ).pack(fill="both")

ventana.mainloop()