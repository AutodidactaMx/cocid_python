import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# crear un Frame
frame = tk.Frame(root, bg="light blue", padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# agregar un label y un botón al Frame
label = tk.Label(frame, text="¡Hola desde el Frame!", font=("Arial", 14))
label.pack(pady=10)

boton = tk.Button(frame, text="Haz clic")
boton.pack(pady=10)

root.mainloop()
