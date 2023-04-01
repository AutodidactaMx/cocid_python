import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
var = tk.StringVar()
l = tk.Label(window, bg='white', width=100, text='empty')
l.pack()


def print_selection():
    l.config(text='el valor que has seleccionado ' + var.get() )


r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r3.pack()

window.mainloop()
