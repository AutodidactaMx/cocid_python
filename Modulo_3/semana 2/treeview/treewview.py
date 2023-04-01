import tkinter as tk 
from tkinter import ttk 
from tkinter.messagebox import showinfo

#Disparo de evento al seleccionar
def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


root = tk.Tk()
tree=ttk.Treeview(root)
#Definimos las columnas
tree["columns"]=("uno","dos","tres")
tree.column("#0", width=0, minwidth=270, stretch=tk.NO)
tree.column("uno", width=150, minwidth=150, stretch=tk.NO)
tree.column("dos", width=400, minwidth=200)
tree.column("tres", width=80, minwidth=50, stretch=tk.NO)
#Definir encabezado
tree.heading("#0",text="Nombre",anchor=tk.W)
tree.heading("uno", text="Fecha",anchor=tk.W)
tree.heading("dos", text="Tipo",anchor=tk.W)
tree.heading("tres", text="Tamaño",anchor=tk.W)
#Anclamos bloques
tree.pack(side=tk.TOP)

#Insertar fila
tree.insert('', tk.END, values=["Fila uno","Fila dos"," Fila tres"])
tree.insert('', tk.END, values=["Fila2 uno","Fila2 dos"," Fila2 tres"])
tree.bind('<<TreeviewSelect>>', item_selected)


root.mainloop()