from tkinter import *
from tkinter.ttk import Notebook

ws = Tk()
ws.geometry('400x300')
ws.title('Python Guides Notebook')

notebook = Notebook(ws)
notebook.pack(pady=10, expand=True)

frame1 = Frame(notebook, width=400, height=280)
frame2 = Frame(notebook, width=400, height=280)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

notebook.add(frame1, text='Tab 1')
notebook.add(frame2, text='Tab 2')

ws.mainloop()
