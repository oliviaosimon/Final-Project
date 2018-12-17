#sokoban.py
#Olivia Simon
#12.17.18
#Computer Programmming Period 4
#other sources: 
    #(platformer) https://github.com/oliviaosimon/Platformer/blob/master/platformer.py
    


from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

myapp = App()

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

class Blocks(Sprite):
    def __init__(self, x, y, w, h, color):
        grid = lambda X : X - X % w
        super().__init__(
            RectangleAsset(w-1, h-1, LineStyle(0,Color(0, 1.0)), color),(grid(x), grid(y)))
        #collisions
        collisioncontra =self.collidingWithSprites(type(self))
        if len(collisioncontra):
            collisioncontra[0].destroy()

class Wall(Blocks):
    def __init__(self,x,y):
        super().__init__(x,y,60,60,grey)      #(self, x, y, w, h, color)
        
class Playah(Newton):
    def __init__(self, x, y, app):
        w = 10 
        h = 10
        super().__init__(x-w//2, y-h//2, w, h, lightBlue, app)
        
    def step(self):
        Jumpers = self.collidingWithSprites(Jumper)    #interference with Jumpers
        if len(Jumpers):
            self.vy = -16    #y -- y positioning jump boost
            self.resting = False
        super().step()
        
    def move(self, key):
        if key == "left arrow":
            if self.vx > 0:
                self.vx = 0
            else:
                self.vx = -5
        elif key == "right arrow":
            if self.vx < 0:
                self.vx = 0
            else:
                self.vx = 5
        elif key == "space" and self.resting:
            self.vy = -12
            self.resting = False
            