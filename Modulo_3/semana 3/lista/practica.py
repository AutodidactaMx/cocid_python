from tkinter import *

top = Tk()

listbox = Listbox(top, height=10,
                  width=15,
                  bg="grey",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="yellow")
top.geometry("300x250")
label = Label(top, text="Lista de comida")
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

label.pack()
listbox.pack()
top.mainloop()

