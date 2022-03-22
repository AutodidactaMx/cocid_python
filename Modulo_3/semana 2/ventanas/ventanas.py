import tkinter as tk 
ventana_raiz = tk.Tk()
ventana_raiz.geometry("400x400")
label1 = tk.Label(ventana_raiz, text="""La raiz""")
label1.pack()

ventana_extra = tk.Toplevel(ventana_raiz)
label2 = tk.Label(ventana_extra, text="""Ventana extra""")
ventana_extra.geometry("300x300")
label2.pack()

ventana_extra2 = tk.Toplevel(ventana_raiz)
label2 = tk.Label(ventana_extra2, text="""Ventana extra2""")
ventana_extra2.geometry("200x200")
label2.pack()
ventana_raiz.mainloop()
