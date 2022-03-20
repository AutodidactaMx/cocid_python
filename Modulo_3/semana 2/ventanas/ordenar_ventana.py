import tkinter as tk 
root = tk.Tk()
for i in range(4):
 window = tk.Toplevel(root)
 label = tk.Label(window,text="window {}".format(i))
 label.pack() 
 button = tk.Button(root, text = "lift window {}".format(i), command=window.lift)
 button.grid(row=i)
root.mainloop()