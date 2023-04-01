import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

data = {
            'Morelos': 10,
            'Zacatecas': 50,
            'Hidalgo': 10,
            'Guerrero': 20,
            'Veracruz': 10
        }
clave = data.keys()
valor = data.values()

ventana= tk.Tk() 
  
figura = plt.Figure(figsize=(6,5), dpi=100)
lienzo_figura = FigureCanvasTkAgg(figura, ventana)
lienzo_figura.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

ax1 = figura.add_subplot()
ax1.set_title('Recepcion de turistas')
ax1.pie(x=list(valor),labels=list(clave))


toolbar =NavigationToolbar2Tk(lienzo_figura, ventana)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.Y)
ventana.mainloop()