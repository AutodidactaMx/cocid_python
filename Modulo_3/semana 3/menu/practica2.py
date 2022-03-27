import tkinter as tk
from tkinter import filedialog


def onOpen():
    print(filedialog.askopenfilename(initialdir="/", title="Open file",
                                     filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))


def onSave():
    print(filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                       filetypes=(("Python files", "*.py;*.pyw"), ("All files", "*.*"))))


app = tk.Tk()
app.geometry('300x200')
app.title("Menu Bar Command")

menubar = tk.Menu(app)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=onOpen)
filemenu.add_command(label="Save", command=onSave)
filemenu.add_command(label="Exit", command=app.quit)

menubar.add_cascade(label="File", menu=filemenu)

app.config(menu=menubar)

app.mainloop()
