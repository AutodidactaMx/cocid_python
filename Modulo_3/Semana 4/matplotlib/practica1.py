import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

data = {
            'Perro': 87,
            'Gato': 333,
            'Pajaro': 98,
            'Pez': 22,
            'Reptil': 100
        }
clave = data.keys()
valor = data.values()

ventana= tk.Tk() 
  
figura = plt.Figure(figsize=(6,5), dpi=100)
lienzo_figura = FigureCanvasTkAgg(figura, ventana)
lienzo_figura.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

ax1 = figura.add_subplot()
ax1.set_title('Que clase de ,mascota tienes?')
ax1.bar(clave, valor)
ax1.set_ylabel('Cantidades')
ax1.set_xlabel('Animales')

toolbar =NavigationToolbar2Tk(lienzo_figura, ventana)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.Y)
ventana.mainloop()