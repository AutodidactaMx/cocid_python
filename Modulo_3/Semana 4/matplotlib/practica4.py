import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

data = {
            'Basquet': 11,
            'Futbol': 222,
            'Natacion': 121,
            'Esqui': 321,
            'Tenis': 44
        }
clave = data.keys()
valor = data.values()

ventana= tk.Tk() 
  
figura = plt.Figure(figsize=(6,5), dpi=100)
lienzo_figura = FigureCanvasTkAgg(figura, ventana)
lienzo_figura.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

ax1 = figura.add_subplot()
ax1.set_title('Alumnos')
ax1.plot(clave, valor)
ax1.set_ylabel('Cantidad alumnos')
ax1.set_xlabel('Materias')

toolbar =NavigationToolbar2Tk(lienzo_figura, ventana)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.Y)
ventana.mainloop()