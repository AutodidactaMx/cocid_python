from tkinter import  Tk, Frame, Canvas, Button,Label, IntVar, ALL
import random
from pygame import mixer

mixer.init()


class FormSnake():    

    def __init__(self) -> None:        
        self.ventana = Tk() 
        self.variables_iniciales() 
        self.propiedades_ventana()      
        self.preparar_tablero()     
        self.prepararArena()     
        self.ventana.mainloop()
    
    def direccion_movimiento(self,event):        

        if event == 'left':
            if self.direccion != 'right':
                self.direccion = event
        elif event == 'right':
            if self.direccion != 'left':
                self.direccion = event
        elif event == 'up':
            if self.direccion != 'down':
                self.direccion = event
        elif event == 'down':
            if self.direccion != 'up':
                self.direccion = event

    
    def cruzar_snake(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2, 
            text=f"Perdiste 🍎",fill='red',
            font=('Arial',20,'bold'))

    def maximo_nivel(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2, 
            text=f"GANADOR 🍎🍎🍎",fill='green',
            font=('Arial',35,'bold'))

    
    def coordenadas_snake(self):        

        if self.direccion =='up': # arriba
            self.y =  self.y-30
            self.nueva_posicion[0:] = [(self.x, self.y)]
            if self.y >=495:
                self.y=15
            elif self.y <=0:
                self.y=465
        elif self.direccion =='down':  # abajo
            self.y = self.y+30 
            self.nueva_posicion[0:] = [(self.x, self.y)]
            if self.y >=495:
                self.y=15
            elif self.y <=0:
                self.y=15    
        elif self.direccion == 'left': # izquierda
            self.x = self.x-30
            self.nueva_posicion[0:] = [(self.x, self.y)]
            if self.x >=495:
                self.x = 0
            elif self.x <=0:
                self.x=465
        elif self.direccion == 'right':  # derecha
            self.x = self.x + 30
            self.nueva_posicion[0:] = [(self.x, self.y)]
            if self.x >=495:
                self.x=15
            elif self.x <=0:
                self.x=15

        self.posicion_snake = self.nueva_posicion + self.posicion_snake[:-1]

        for parte, lugar in zip(self.canvas.find_withtag("snake"), self.posicion_snake):
            self.canvas.coords(parte, lugar)

    
    def movimiento(self):
        self.posicion_comida, self.posicion_snake,self.nueva_posicion
        self.posiciones = [15, 45, 75,105,135,165, 195, 225, 255, 
        285, 315, 345, 375, 405, 435, 465] 

        self.coordenadas_snake()

        if self.posicion_comida == self.posicion_snake[0]:
            n = len(self.posicion_snake)

            self.cantidad['text'] = f'🍎 : {n}'

            self.posicion_comida = (random.choice(self.posiciones), random.choice(self.posiciones))
            self.posicion_snake.append(self.posicion_snake[-1])

            mixer.music.load("audio_snake.mp3")
            mixer.music.play(loops=0)

            if self.posicion_comida not in self.posicion_snake:
                self.canvas.coords(self.canvas.find_withtag("food"), self.posicion_comida)

            self.canvas.create_text(*self.posicion_snake[-1], text= '🐍', fill='#4c7af0', 
                font = ('Arial',20), tag ='snake')

        if self.posicion_snake[-1] == self.nueva_posicion[0] and len(self.posicion_snake)>=4: 
            self.cruzar_snake()

        for i in self.posicion_snake:
            if len(self.posicion_snake)==self.numero_ganador:
                self.maximo_nivel()     

        self.cantidad.after(300, self.movimiento)

    
    def variables_iniciales(self):
        self.numero_ganador =10
        self.x, self.y =15,15
        self.direccion = ''
        self.posicion_x = 15
        self.posicion_y = 15
        self.posicion_comida = (15,15)
        self.posicion_snake = [(75,75)]
        self.nueva_posicion =[(15,15)]
        
    def propiedades_ventana(self):
        self.ventana.config(bg='#4a752c')
        self.ventana.title('Snake')
        self.ventana.geometry('485x510')
        self.ventana.resizable(0,0) 
        
        self.ventana.bind("<KeyPress-Up>", lambda event:self.direccion_movimiento('up'))
        self.ventana.bind("<KeyPress-Down>", lambda event:self.direccion_movimiento('down'))
        self.ventana.bind("<KeyPress-Left>", lambda event:self.direccion_movimiento('left'))
        self.ventana.bind("<KeyPress-Right>",  lambda event:self.direccion_movimiento('right'))

    
    def prepararArena(self):
        self.marco_arena = Frame(self.ventana, width=485, height=490, bg='#aad751')
        self.marco_arena.grid(column=0, row=1)
        self.canvas = Canvas(self.marco_arena, bg='#aad751', width=479, height=479)
        self.canvas.pack()
        self.canvas.create_rectangle(0,0,30,30)
        for i in range(0,460,30):
            for j in range(0,460,30):
                self.canvas.create_rectangle(i,j,i+30, j+30,outline="#5a8d35")
        
        self.canvas.create_text(75,75, text='🍎', fill='red',
        font = ('Arial',18), tag = 'food')
        
    def preparar_tablero(self):
        self.tablero = Frame(self.ventana, width=485, height=25,bg='#4a752c')
        self.tablero.grid(column=0, row=0)

        self.boton_arranque = Button(self.tablero, text='Iniciar', font=('Arial',12, 'bold'), fg ='white',bd=0, bg='#a2d149',command = self.movimiento)
        self.boton_arranque.pack(side="left",padx=20, pady=10)

        self.cantidad =Label(self.tablero, text='🍎',  fg ='red',bg='#4a752c', font=('Arial',12, 'bold'))
        self.cantidad.pack(side="right",padx=20)
        self.cantidadtexto =Label(self.tablero, text='Cantidad:',  fg = 'white',bg='#4a752c', font=('Arial',12, 'bold'))
        self.cantidadtexto.pack(side="right",padx=20, pady=10)        


