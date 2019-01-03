#pong.py
#Olivia Simon
#1.1.19
#Computer Programmming Period 4
#other sources: 
    #(platformer) https://github.com/oliviaosimon/Platformer/blob/master/platformer.py
    
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

myapp = App()

#Ball
class Ball(Sprite):
    def __init__(self, position):
        ball_asset = ImageAsset("images/orb-150545_640.png") #pull from repository
        #ball = Sprite(ball_asset, (0, 400))
        ball_asset.scale = 0.07
        # custom attributes
        ball_asset.direction = 1
        ball_asset.go = True
        # Sounds
        pew1_asset = SoundAsset("sounds/pew1.mp3")
        pew1 = Sound(pew1_asset)
        pop_asset = SoundAsset("sounds/reappear.mp3")
        pop = Sound(pop_asset)
        super().__init__(ball_asset, position)

        
    # reverse - change the ball direction
    def reverse(b):
        pop.play()
        b.direction *= -1
    
    # Bounce
    def step():
        if ball.go:
            ball.x += ball.direction
            if ball.x + ball.width > myapp.width or ball.x < 0:
                ball.x -= ball.direction
                reverse(ball)

#Paddle Playah
class Paddle(Sprite):
    def __init__(self, position, w, h):
        w = 20 
        h = 60
        x = 400
        y = 400
        rect = RectangleAsset(w, h, blkline, lightBlue)
        super().__init__(rect, position)
        
    def move(self,key):
        if key == "up arrow":
            self.y += -5
        elif key == "down arrow":
            self.y += 5

#keys
#def reverseKey(event):
 #   reverse(ball)

# Handle the mouse click
#def mouseClick(event):
 #   pew1.play()
  #  ball.x = event.x
   # ball.y = event.y
    
# Set up event handlers for the app
#myapp.listenKeyEvent('keydown', 'r', reverseKey)
#myapp.listenMouseEvent('click', mouseClick)
   
class Pong(App):
    def __init__(self):
        super().__init__()
        self.p = None
        self.pos = (0,0)
        ocean = Color(0x00fff0, 1)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        #background
        bg_asset = RectangleAsset(myapp.width, myapp.height, noline, ocean)
        bg = Sprite(bg_asset, (0,0))
        Ball((0,400))
        
        Pong.listenKeyEvent("keydown", "p", self.newPaddle)
        self.listenKeyEvent("keydown", "up arrow", self.moveKey)
        self.listenKeyEvent("keydown", "down arrow", self.moveKey)
        
        
    def newPaddle(self, event):
        for p in Pong.getSpritesbyClass(Paddle):
            p.destroy()
            self.p = None
        self.p = Paddle((400, 400), 20, 60)
    
    def moveKey(self, event):
        if self.p:
            self.p.move(event.key)


myapp = Pong()
myapp.run