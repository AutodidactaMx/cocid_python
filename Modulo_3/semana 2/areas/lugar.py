from tkinter import *
root = Tk()
root.geometry("500x500")

btn_height = Button(root, text="100px high")
btn_height.place(x=0, rely=0.5)

btn_width = Button(root, text="100px wide")
btn_width.place(relx=0.5, y=100)

#btn_relheight = Button(root, text="Relheight of 0.6")
#btn_relheight.place(relheight=0.6)

#btn_relwidth= Button(root, text="Relwidth of 0.2")
#btn_relwidth.place(relwidth=0.2)

#btn_relx=Button(root, text="Relx of 0.3")
#btn_relx.place(relx=0.3)

#btn_rely=Button(root, text="Rely of 0.7")
#btn_rely.place(rely=0.7)

#btn_x=Button(root, text="X = 400px")
#btn_x.place(x=400)

#btn_y=Button(root, text="Y = 321")
#btn_y.place(y=321)
root.mainloop()