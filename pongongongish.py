#pong.py
#Olivia Simon
#1.1.19
#Computer Programmming Period 4
#other sources: 
    #(platformer) https://github.com/oliviaosimon/Platformer/blob/master/platformer.py
    #https://stackoverflow.com/questions/13881395/in-python-what-is-a-global-statement
    
from math import sqrt
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, Frame
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

lightBlue = Color(0x2EFEC8, 1.0)
black = Color(0x000000, 1.0)
pink = Color(0xFF00FF, 1.0)
red = Color(0xFF5733, 1.0)
white = Color(0xFFFFFF, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
darkBlue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
grey = Color(0xC0C0C0, 1.0)

thinline = LineStyle(2, black)
blkline = LineStyle(1, black)
noline = LineStyle(0, white)
coolline = LineStyle(1, grey)
blueline = LineStyle(2, darkBlue)
redline = LineStyle(1, red)
greenline = LineStyle(1, green)
gridline = LineStyle(1, grey)
grid=RectangleAsset(30,30,gridline,white)

class Paddle(Sprite):
    def __init__(self, position):
        rect = RectangleAsset(10, 100, blkline, lightBlue)
        super().__init__(rect, position)
        self.vx = 0
        self.vy = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        
class Ball(Sprite):
    def __init__(self, position):
        global myapp
        #self.c = color
        #self.d = diameter
        self.vy = 0
        self.vx = 0
        rollypolly = CircleAsset(7, thinline, white)
        #myapp.listenKeyEvent('keydown', 'space', self.spaceKey)
        super().__init__(rollypolly, position)
        self.direction = 1
        self.go = True

    def step(self):
        global myapp
        if self.go:
            self.x += self.direction
        if self.x + self.width > myapp.width or self.x < 0:
            self.x -= self.direction
            #reverse(Ball)
        self.vy *= 0.99
        self.vx *= 0.99
        self.y += self.vy
        self.x += self.vx
        
        if sqrt((self.vy**2)+(self.vx**2)) < 1:
            self.vy = 0
            self.vx = 0
            
        #print("step")

        #paddleclap = self.collidingWith(myapp.paddle)
        paddleclap = self.collidingWithSprites(Paddle)
        if paddleclap:
            self.vx = self.vx*-1
    
        wallclapOne = self.collidingWithSprites(border1)
        if wallclapOne:
            self.vx = self.vx*-1
        
        wallclapTwo = self.collidingWithSprites(borderUp)
        if wallclapTwo:
            self.vx = self.vx*-1
            
        wallclapThree = self.collidingWithSprites(borderLow)
        if wallclapThree:
            self.vx = self.vx*-1

        gameDeath = self.collidingWithSprites(backwall)
        if gameDeath:
            self.destroy()
            myapp.ball = None
            print("GAME OVER!!!")
        
class border1(Sprite):
    def __init__(self, position):
        rect = RectangleAsset(8, 800, noline, black)
        super().__init__(rect, position)

class borderUp(Sprite):
    def __init__(self, position):
        rect = RectangleAsset(1500, 8, noline, black)
        super().__init__(rect, position)
    
class borderLow(Sprite):
    def __init__(self, position):
        rect = RectangleAsset(1500, 8, noline, black)
        super().__init__(rect, position)
    
class backwall(Sprite):
    def __init__(self, position):
        rect = RectangleAsset(8, 800, noline, black)
        super().__init__(rect, position)

class Background(Sprite):
    def __init__(self, position):
        background = ImageAsset("images/starfield.jpg")
        super().__init__(background, position)
        self.scale = 3
        
class Pongish(App):
    def __init__(self, width, height):
        super().__init__(width,height)
        print("  WELCOME to PONG-ISH! ")
        print("try and hit the ball as many times as possible.")
        print("try not to let it go past you.")
        print("to move your paddle,")
        print("Use the up and down arrow keys.")
        print("Click p to start.")
        print("ENJOY!")
        
        Background((0,0))
        border1((1260,0))
        borderUp((0,0))
        borderLow((0,710))
        backwall((0,0))
        pelota = None
        count = []
        
        self.ball = None
        self.paddle = None
        
        # Listen key events -----------------------------------------------
        Pongish.listenKeyEvent("keydown", "p", self.newPaddle)
        Pongish.listenKeyEvent("keydown", "up arrow", self.up)
        Pongish.listenKeyEvent("keydown", "down arrow", self.down)
        
    def newPaddle(self, event):
        self.paddle = Paddle((400, 300))
        self.ball = Ball((400, 300))

    def up(self, event):
        for s in self.getSpritesbyClass(Paddle):
            s.vy = -2
            
    def down(self, event):
        for s in self.getSpritesbyClass(Paddle):
            s.vy = 2
            
    def step(self):
        if self.ball:
            self.ball.step()
        if self.paddle:
            self.paddle.step()

myapp = Pongish(1270,720)
myapp.run()