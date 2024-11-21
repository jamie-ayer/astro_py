from tkinter import *
from PIL import Image, ImageTk
from Ship import *

class Game:
    
    def __init__(self, root: Tk) -> None:
        
        self.width = 800
        self.height = 800
        self.master = root
        self.master.title('Astro')
        self.score = 0
        self.score_label = StringVar()
        self.score_label.set(f'Score: {self.score}')
        
        self.pv = 0
        self.pause = StringVar()
        self.pause.set('0')
        self.master.bind('<Key>', self.movement)
        
        im: Image = Image.open('spacebg.png')
        print(im.size)
        im = im.resize((1600, 1560))
        print(im.size)
        self.bg = ImageTk.PhotoImage(image=im)
        
        self.board_setup()
        self.game_setup()
        
        
    def board_setup(self):
        
        self.canvas = Canvas(self.master, width=self.width, height=self.height+20)
        Label(self.master, textvariable=self.score_label).place(x=150, y=800)
        
        
        for line in range(0, self.width, 20):
            self.canvas.create_line([(line, 0), (line, self.height)], fill='black', tags='grid_line_w')
        for line in range(0, self.height, 20):
            self.canvas.create_line([(0, line), (self.width, line)], fill='black', tags='grid_line_h')
            
        self.canvas.create_rectangle(0, 798, 805, 825, fill='black', tags='bottomBar')
        self.canvas.grid(row=0, column=0)
        self.canvas.create_image(20, 20, image=self.bg, tags='bg')
        
        #self.canvas.pack()
        
    def movement(self, e: Event):
        
        if e.char == 'a':
            self.direction = 'Left'
        if e.char == 'd':
            self.direction = 'Right'
        if e.char == 's':
            self.direction = 'Stop'
            
    def draw_ship(self):
        
        self.canvas.delete('ship')
        self.canvas.create_rectangle(self.ship.coords[0], self.ship.coords[1], self.ship.coords[0]+20, self.ship.coords[1]+20, fill='red', tags='ship')
            
    def game_setup(self):
        
        self.ship = Ship()
        self.gameOverFlag = False
        self.gameSpeed = 10
        self.direction = 'Stop'
        
        self.game_loop()
        
    def ship_direction(self):
        
        if self.direction == 'Left':
            self.ship.left()
        if self.direction == 'Right':
            self.ship.right()
        if self.direction == 'Slow':
            self.ship.slow()
            
    def game_loop(self):
        
        if self.gameOverFlag == False:
            
            self.ship_direction()
            self.draw_ship()
            print(self.ship.acc)
            
            
            if self.gameOverFlag == False:
                self.master.after(self.gameSpeed, self.game_loop)
        