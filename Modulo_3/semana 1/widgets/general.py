from tkinter import *
from tkinter import ttk

#Frame
root = Tk()
root.geometry("1240x850")
frame = Frame(root)
frame.pack()

#label
label = Label(frame, text = "Hola")
label.pack()

#Button
button1 = Button(frame, text = "Boton")
button1.pack()

#Entry
my_entry = Entry(frame, width = 20)
my_entry.insert(0,'Usuario')
my_entry.pack(padx = 5, pady = 5)

#CheckButton
Var1 = IntVar()
Var2 = IntVar()
ChkBttn = Checkbutton(frame, width = 15, variable = Var1, text="opcion1")
ChkBttn.pack(padx = 5, pady = 5)
ChkBttn2 = Checkbutton(frame, width = 15, variable = Var2, text="opcion2")
ChkBttn2.pack(padx = 5, pady = 5)

#RadioButton
Var1 = StringVar()
RBttn = Radiobutton(frame, text = "Option1", variable = Var1,
                    value = 1)
RBttn.pack(padx = 5, pady = 5)
RBttn2 = Radiobutton(frame, text = "Option2",
                     value = 2)
RBttn2.pack(padx = 5, pady = 5)

#Menu
def save():
    #Code to be written
    pass
 
def load():
    #Code to be written
    pass   

mainmenu = Menu(frame)
mainmenu.add_command(label = "Guarda", command= save)  
mainmenu.add_command(label = "Cargar", command= load)
mainmenu.add_command(label = "Salir", command= root.destroy)
 
root.config(menu = mainmenu)

#ComboBox
vlist = ["Opcion1", "Opcion2", "Opcion3",
          "Opcion4", "Opcion5"]
 
Combo = ttk.Combobox(frame, values = vlist)
Combo.set("Pick an Option")
Combo.pack(padx = 5, pady = 5)


listbox = Listbox(root)  
   
listbox.insert(1,"Pan")  
listbox.insert(2, "Leche")  
listbox.insert(3, "Carne")  
listbox.insert(4, "Queso")
listbox.insert(5, "Vegetales")  
   
listbox.pack()  

#Menu
MenuBttn = Menubutton(frame, text = "Comida favorita", relief = RAISED)
 
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()

Menu1 = Menu(MenuBttn, tearoff = 0)
Menu1.add_checkbutton(label = "Pizza", variable = Var1)
Menu1.add_checkbutton(label = "Hamburguesa", variable = Var2)
Menu1.add_checkbutton(label = "Ensalada", variable = Var3)
MenuBttn["menu"] = Menu1
 
MenuBttn.pack()

#Canvas
canvas = Canvas(frame,bg='white', width = 300,height = 300)
 
coordinates = 20, 50, 210, 230
arc = canvas.create_arc(coordinates, start=0, extent=250, fill="blue")
arc = canvas.create_arc(coordinates, start=250, extent=50, fill="red")
arc = canvas.create_arc(coordinates, start=300, extent=60, fill="yellow")
 
canvas.pack(expand = True, fill = BOTH)
 


root.mainloop()


