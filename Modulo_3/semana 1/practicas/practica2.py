from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('500x500')
root.title('Practica 2')
style = Style()

style.configure('TButton', font=('calibri', 20, 'bold'), borderwidth='4')

style.map('TButton', foreground=[('pressed', 'blue'), ('active', 'red')])

btn1 = Button(root, text='Quit !', command=root.destroy)
btn1.grid(row=0, column=3, padx=100)

btn2 = Button(root, text='Click me !', command=None)
btn2.grid(row=1, column=3, pady=10, padx=100)

root.mainloop()
