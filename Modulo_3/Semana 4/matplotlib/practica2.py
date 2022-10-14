import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

data = {
            '0-9': 5000,
            '10-19': 2000,
            '20-29': 30000,
            '30-39': 43490,
            '40-49': 39898
        }
clave = data.keys()
valor = data.values()

ventana= tk.Tk() 
  
figura = plt.Figure(figsize=(6,5), dpi=100)
lienzo_figura = FigureCanvasTkAgg(figura, ventana)
lienzo_figura.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

ax1 = figura.add_subplot()
ax1.set_title('Habitantes')
ax1.barh(list(clave), list(valor))
ax1.set_ylabel('Rango de edad')
ax1.set_xlabel('Cantidad')

toolbar =NavigationToolbar2Tk(lienzo_figura, ventana)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.Y)
ventana.mainloop()