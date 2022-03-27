from tkinter import *

ws = Tk()
ws.title('Python List')
ws.geometry('400x300')
ws.config(bg='#5f9ea0')


def showSelected():
    show.config(text=lb.get(lb.curselection()[0]))


lb = Listbox(ws)
lb.pack()
lb.insert(0, 'rojo')
lb.insert(1, 'verde')
lb.insert(2, 'amarillo')
lb.insert(3, 'azul')

Button(ws, text='Mostar seleccionado', command=showSelected).pack(pady=20)
show = Label(ws)
show.pack()

ws.mainloop()
