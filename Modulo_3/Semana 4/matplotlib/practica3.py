import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

data = {
            'Enero': 12300,
            'Febrero': 23400,
            'Marzo': 303400,
            'Abril': 432290,
            'Mayo': 39838
        }
clave = data.keys()
valor = data.values()

ventana= tk.Tk() 
  
figura = plt.Figure(figsize=(6,5), dpi=100)
lienzo_figura = FigureCanvasTkAgg(figura, ventana)
lienzo_figura.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

ax1 = figura.add_subplot()
ax1.set_title('Ventas')
ax1.fill_between(clave, valor)
ax1.set_ylabel('$')
ax1.set_xlabel('Meses')

toolbar =NavigationToolbar2Tk(lienzo_figura, ventana)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.Y)
ventana.mainloop()