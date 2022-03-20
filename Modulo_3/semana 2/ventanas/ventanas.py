import tkinter as tk 
root = tk.Tk()
label1 = tk.Label(root, text="""La raiz""")
label1.pack()

extra_window = tk.Toplevel(root)
label2 = tk.Label(extra_window, text="""Ventana extra""")
label2.pack()
root.mainloop()
