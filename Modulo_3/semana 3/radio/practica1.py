from tkinter import *
root = Tk()
root.config(bd=15)
selected = StringVar()
r1 = Radiobutton(root, text='Option 1', value='Value 1', 
variable=selected).pack()
r2 = Radiobutton(root, text='Option 2', value='Value 2', 
variable=selected).pack()
r3 = Radiobutton(root, text='Option 3', value='value 3', 
variable=selected).pack()
root.mainloop()
