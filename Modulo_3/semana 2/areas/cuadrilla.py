from tkinter import *
root = Tk()
root.geometry("300x400")

#column

btn_fila2_column1 = Button(root, text="Fila 2 Columna 1 ....................")
btn_fila2_column1.grid(column=1, row=2)

btn_fila_column1 = Button(root, text="Fila 1 Columna 1")
btn_fila_column1.grid(column=1, row=1,sticky=NW)

btn_fila_column2 = Button(root, text="Fila 2 Columna 2")
btn_fila_column2.grid(column=2, row=1)

btn_fila_column3 = Button(root, text="Fila 1 Columna 3")
btn_fila_column3.grid(column=3, row=1)

#columnspan
#btn_columnspan = Button(root, text="Uso de columnaspan de 3")
#btn_columnspan.grid(columnspan=3)

#ipadx
#btn_ipadx = Button(root, text="ipadx de 4")
#btn_ipadx.grid(ipadx=4)

#ipady
#btn_ipady = Button(root, text="ipady de 4")
#btn_ipady.grid(ipady=4)

#btn_padx
#btn_padx = Button(root, text="padx de 4")
#btn_padx.grid(padx=4)

#pady
#btn_pady = Button(root, text="pady de 4")
#btn_pady.grid(pady=4)

#row
#btn_row = Button(root, text="Fila row 2")
#btn_row.grid(row=2)

#rowspan
#btn_rowspan = Button(root, text="Rowspan de 2")
#btn_rowspan.grid(rowspan=2)

#sticky
#btn_sticky = Button(root, text="Noroeste")
#btn_sticky.grid(sticky=NE)

root.mainloop()
