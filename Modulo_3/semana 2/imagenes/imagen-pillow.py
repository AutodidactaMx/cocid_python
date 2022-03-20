from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.title('PythonGuides')
ventana.geometry('500x400')
ventana.config(bg='#C2C2C2')


def redimensionar_func():
    image = Image.open("./logo.png")
    w = int(width.get())
    h = int(height.get())
    resize_img = image.resize((w, h))
    img = ImageTk.PhotoImage(resize_img)
    disp_img.config(image=img)
    disp_img.image = img


frame = Frame(ventana)
frame.pack()

Label(frame, text='Ancho' ).pack(side=LEFT)
width = Entry(frame, width=10)
width.insert(END, 300)
width.pack(side=LEFT)

Label( frame, text='Alto' ).pack(side=LEFT)

height = Entry(frame, width=10)
height.insert(END, 350)
height.pack(side=LEFT)

boton = Button( frame,
    text='Redimensionar',
    command=redimensionar_func
)
boton.pack(side=LEFT)

disp_img = Label()
disp_img.pack(pady=20)


ventana.mainloop()
