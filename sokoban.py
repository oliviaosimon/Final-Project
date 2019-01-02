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
        
class Playah(Sprite):
    def __init__(self, x, y, app):
        self.vx = self.vy = 0
        w = 10 
        h = 10
        x = 200
        y = 250
        super().__init__(x, y, w, h, lightBlue, app)
        
        #walking walk waddle?
        Playah.direction = 1
        Playah.go = False
    
    #Reverse function
    def reverse(b): 
        b.direction *= -1

    # Set up function for handling screen refresh
    #def step():
        #if Playah.go:
         #   Playah.x += Playah.direction
          #  if Playah.x + Playah.width > myapp.width or Playah.x < 0: #fix so if going out past walls ?
           #     Playah.x -= Playah.direction
            #        reverse(Playah)
        
    
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
        elif key == "up arrow":
            self.vy = -5
        elif key == "down arrow":
            self.vy = 5

class Crates(Blocks):
    def __init__(self, x,y):
        super().__init__(x,y,60,60,brown)     #(self, x, y, w, h, color)

#Glossarix
class Game(App):
    def __init__(self):
        super().__init__()
        self.p = None
        self.pos = (0,0)
        self.listenKeyEvent("keydown", "p", self.newPlayah)
        self.listenKeyEvent("keydown", "left arrow", self.moveKey)
        self.listenKeyEvent("keydown", "right arrow", self.moveKey)
        self.listenKeyEvent("keydown", "up arrow", self.moveKey)
        self.listenKeyEvent("keydown", "down arrow", self.moveKey)
        self.listenKeyEvent("keyup", "left arrow", self.stopMoveKey)
        self.listenKeyEvent("keyup", "right arrow", self.stopMoveKey)
        self.listenKeyEvent("keyup", "up arrow", self.stopMoveKey)
        self.listenKeyEvent("keyup", "down arrow", self.stopMoveKey)
        
        self.KillList = []
        
        
    def newPlayah(self, event):
        for p in Game.getSpritesbyClass(Playah):
            p.destroy()
            self.p = None
        self.p = Playah(self.pos[0], self.pos[1], self)
        
    def moveKey(self, event):
        if self.p:
            self.p.move(event.key)
    
    def stopMoveKey(self, event):
        if self.p:
            self.p.stopMove(event.key)
            
    def step(self):
        if self.p:
            self.p.step()
        for s in self.FallingJumpers:      # problem fixed, empty list in Game added for fallingjumpers
            s.step()
        for k in self.KillList:
            k.destroy()
        self.KillList = []
    
    def killMe(self, obj):
        if obj in self.FallingJumpers:
            self.FallingJumpers.remove(obj)
        elif obj == self.p:
            self.p = None
        if not obj in self.KillList:
            self.KillList.append(obj)


app = Game()
app.run()

         
