from tkinter import *      

ventana = Tk()
ventana.title('PythonGuides')
ventana.geometry('500x500')

canvas = Canvas(ventana, width = 500,  height = 500)      
canvas.pack()      
img = PhotoImage(file='./imagenes/logo.png')      
img = img.subsample(3, 3)

canvas.create_image( 10,10,  anchor=NW, image=img )      
ventana.mainloop()  