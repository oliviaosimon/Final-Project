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
    ball_asset = ImageAsset("images/orb-150545_640.png") #pull from repository
    ball = Sprite(ball_asset, (0, 0))
    ball.scale = 0.07

    # custom attributes
    ball.direction = 1
    ball.go = True
    # Sounds
    pew1_asset = SoundAsset("sounds/pew1.mp3")
    pew1 = Sound(pew1_asset)
    pop_asset = SoundAsset("sounds/reappear.mp3")
    pop = Sound(pop_asset)
    
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
    def __init__(self, x, y, app):
        w = 20 
        h = 60
        super().__init__(x, y, w, h, lightBlue, app)

#keys
# Handle the "reverse" key
def reverseKey(event):
    reverse(ball)

# Handle the mouse click
def mouseClick(event):
    pew1.play()
    ball.x = event.x
    ball.y = event.y
    
# Set up event handlers for the app
myapp.listenKeyEvent('keydown', 'r', reverseKey)
myapp.listenMouseEvent('click', mouseClick)
   
class Pong(App):
    def __init__(self):
        super().__init__()
        ocean = Color(0x00fff0, 1)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        #background
        bg_asset = RectangleAsset(myapp.width, myapp.height, noline, ocean)
        bg = Sprite(bg_asset, (0,0))
        
        Paddle((100,100))
        Ball((300,300))


myapp = Pong()
myapp.run




