import tkinter as tk
from tkinter import ttk

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi programa")
        self.geometry("400x300")

        # Crear el menú
        menu = tk.Menu(self)
        archivo_menu = tk.Menu(menu, tearoff=0)
        archivo_menu.add_command(label="Nuevo")
        archivo_menu.add_command(label="Abrir")
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.quit)
        menu.add_cascade(label="Archivo", menu=archivo_menu)
        self.config(menu=menu)

        # Crear el frame principal
        frame_principal = tk.Frame(self)
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear el entry
        entry = ttk.Entry(frame_principal)
        entry.pack(fill=tk.X, padx=10, pady=5)

        # Crear el checkbutton
        check_var = tk.BooleanVar()
        check = ttk.Checkbutton(frame_principal, text="Marcar si es necesario", variable=check_var)
        check.pack(padx=10, pady=5)

        # Crear el combobox
        combobox = ttk.Combobox(frame_principal, values=["Opción 1", "Opción 2", "Opción 3"])
        combobox.pack(fill=tk.X, padx=10, pady=5)

        # Crear el label
        label = tk.Label(frame_principal, text="Este es un label")
        label.pack(padx=10, pady=5)

        # Crear el frame secundario
        frame_secundario = tk.Frame(frame_principal, bg="gray", bd=1, relief=tk.SOLID)
        frame_secundario.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Crear el listbox
        listbox = tk.Listbox(frame_secundario)
        for i in range(10):
            listbox.insert(tk.END, f"Item {i}")
        listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Crear los radiobuttons
        radio_var = tk.StringVar()
        radio1 = ttk.Radiobutton(frame_secundario, text="Opción 1", variable=radio_var, value="opcion1")
        radio1.pack(padx=10, pady=5, anchor=tk.W)
        radio2 = ttk.Radiobutton(frame_secundario, text="Opción 2", variable=radio_var, value="opcion2")
        radio2.pack(padx=10, pady=5, anchor=tk.W)

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
