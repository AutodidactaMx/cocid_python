from tkinter import *
from PIL import ImageTk, Image

ventana = Tk()
ventana.title('PythonGuides')
ventana.geometry("400x400")
img = Image.open("./imagenes/color.jpg")


bg = ImageTk.PhotoImage(img)

canvas = Canvas(ventana, width = 400,  height = 400)     
canvas.pack(fill="both",expand=True)
canvas.create_image( 0,0,  anchor=NW, image=bg )      


label1 = Label(ventana, text="Hola", fg="white" , bg="#000")
label1.pack(side="top")

canvas.create_window(10,10,  anchor=NW, window= label1)

ventana.mainloop()