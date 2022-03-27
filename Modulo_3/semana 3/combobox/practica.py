import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('200x100')

labelTop = tk.Label(app,
                    text="Selecciona tu mes favorito")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app,
                            values=[
                                "Enero",
                                "Febrero",
                                "Marzo",
                                "Abril"])
print(dict(comboExample))
comboExample.grid(column=0, row=1)
comboExample.current(1)

print(comboExample.current(), comboExample.get())

app.mainloop()
