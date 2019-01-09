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

class Paddle(Sprite):
    def __init__(self, position):
        rect = RectangleAsset(10, 50, blkline, lightBlue)
        super().__init__(rect, position)
        

class Ball(Sprite):
    def __init__(self, position):
        ball_asset = CircleAsset(5, blkline, red) #radi, line, color
        super().__init__(ball_asset, position)
        
class Background(Sprite):
    def __init__(self, position):
        background = ImageAsset("images/starfield.jpg")
        super().__init__(self, position)
        self.sccale = 1.5
        
        
class Pongish(App):
    def __init__(self, width, height):
        super().__init__(width,height)
        print("""
        WELCOME to PONG-ISH!
        
        try and hit the ball as many times as possible 
        without letting it go past you
        
        Use the up and down arrow keys to move your paddle
        Click "p" to start
        ENJOY!
        """)
        Background((0,0))
        
# Listen key events -----------------------------------------------
        Pong.listenKeyEvent("keydown", "p", self.newPaddle)
        self.listenKeyEvent("keydown", "up arrow", self.moveKey)
        self.listenKeyEvent("keydown", "down arrow", self.moveKey)
        
        def newPaddle(self, event):
            Paddle((x,y))









