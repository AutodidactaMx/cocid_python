from tkinter import *
from PIL import ImageTk, Image

ventana = Tk()
ventana.title('PythonGuides')
ventana.geometry("400x400")
img = Image.open("./imagenes/python.jpg")


bg = ImageTk.PhotoImage(img)
label = Label( ventana, image=bg )
label.place(x=0,y=0,relwidth=1, relheight=1)


label1 = Label(ventana, text="Hola", fg="white" , bg="#000")
label1.pack(side="top")

ventana.mainloop()