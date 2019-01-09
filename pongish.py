#pong.py
#Olivia Simon
#1.1.19
#Computer Programmming Period 4
#other sources: 
    #(platformer) https://github.com/oliviaosimon/Platformer/blob/master/platformer.py
    #https://stackoverflow.com/questions/13881395/in-python-what-is-a-global-statement
    
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
    rect = RectangleAsset(10, 50, blkline, lightBlue)
    def __init__(self, position):
        super().__init__(rect, position)
        self.vx = 0
        self.vy = 0
        
class Ball(Sprite):
    ball_asset = CircleAsset(5, blkline, red) #radi, line, color
    def __init__(self, position):
        super().__init__(ball_asset, position)
        
class ball(Sprite):

    def __init__(self, color, diameter, x, y):

        global myapp

        self.c = color

        self.d = diameter

        self.vy = 0

        self.vx = 0

        theball = CircleAsset(self.d, thinline, self.c)

        myapp.listenKeyEvent('keydown', 'space', self.spaceKey)

        super().__init__(theball, (x, y))

    def step(self):
        self.vy *= 0.99
        self.vx *= 0.99
        self.y += self.vy
        self.x += self.vx
        
        if sqrt((self.vy**2)+(self.vx**2)) < 1:
            self.vy = 0
            self.vx = 0
        collisionList = self.collidingWith(paddle)
        
        if collisionList:
            xpt = self.x
            ypt = self.y
            xvect = xpt-805
            yvect = ypt-110
            unitxvect = xvect/(sqrt((yvect**2)+(xvect**2)))
            unityvect = yvect/(sqrt((yvect**2)+(xvect**2)))
            self.x = self.x + (-.5*unitxvect)
            self.y = self.y + (-.5*unityvect)
            self.vx = 0
            self.vy = 0
            #scoreboard = TextAsset("Score: "+str(len(scorecounter)), style="bold 15pt Arial", width=250)
            #Sprite(scoreboard, (760, 82))
        
class Background(Sprite):
    background = ImageAsset("images/starfield.jpg")
    def __init__(self, position):
        super().__init__(background, position)
        self.scale = 1.5
        
class Pongish(App):
        print("""
WELCOME to PONG-ISH!

try and hit the ball 
as many times as possible 
try not to let it go past you

to move your paddle,
Use the up and down arrow keys
Click "p" to start
ENJOY!
        """)
        Background((0,0))
        # Listen key events -----------------------------------------------
        Pongish.listenKeyEvent("keydown", "p", self.newPaddle)
        Pongish.listenKeyEvent("keydown", "right arrow", self.right)
        Pongish.listenKeyEvent("keydown", "left arrow", self.left)

    def __init__(self, width, height):
        super().__init__(width,height)
        
    def newPaddle(self, event):
        Paddle((400, 300))
            
    def right(self, event):
        for s in self.getSpritesbyClass(Paddle):
            s.vx = 2
            
    def left(self, event):
        for s in self.getSpritesbyClass(Paddle):
            s.vx = -2
            
myapp = Pongish(1270,720)
myapp.run()








