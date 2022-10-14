import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

class ImageLabel(tk.Label):
    """
    Una etiqueta que muestra imágenes y las reproduce si son gifs
    una instancia de imagen PIL o un nombre de archivo de cadena
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

#demo :
root = tk.Tk()
lbl = ImageLabel(root)
lbl.pack()
lbl.load('gatito.gif')
root.mainloop()