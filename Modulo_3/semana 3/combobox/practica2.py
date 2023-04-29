import tkinter as tk
from tkinter import ttk

def cambiar_texto(event):
    labelResultado.config(text=f"{comboExample.get()}")

app = tk.Tk()
app.geometry('200x100')

labelResultado = tk.Label(app, text="Texto inicial")
labelResultado.pack()

labelTop = tk.Label(app,
                    text="Selecciona tu mes favorito")
labelTop.pack()

comboExample = ttk.Combobox(app,
                            values=[
                                "Enero",
                                "Febrero",
                                "Marzo",
                                "Abril"])
comboExample.bind("<<ComboboxSelected>>", cambiar_texto)

comboExample.pack()
comboExample.current(1)



app.mainloop()
