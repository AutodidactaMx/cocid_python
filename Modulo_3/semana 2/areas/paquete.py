from tkinter import *
root = Tk()
root.geometry("300x400")

btn_fill = Button(root, text="Button fill")
btn_fill.pack(fill=X)

btn_expand = Button(root, text="Button expand ")
btn_expand.pack(expand=YES)

btn_side = Button(root, text="Button side")
btn_side.pack(side=LEFT)
root.mainloop()
