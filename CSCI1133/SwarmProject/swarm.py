import turtle
import math
import random
from entities import Base,Position,Light,Creature
import collision
import configuration


'''
its important that you use the collision file I uploaded because I know that it works

Known Bugs: an object gets sandwitched into a wall, sometimes it glitches through
            it also runs kinda slowly
            also, if objects happen to swawn inside eachother bad things happen
                this almost never happens
'''
# if you run this with like 5 attracted ones its really cool
# also I hate the arctan function after this, the attraction function took
# me like 10 hours to get it to stop looping.





# dimension of display window
WINDOW_XDIM = 900
WINDOW_YDIM = 800
BUFFER = 150
# dimension of area in which robot moves
SCREEN_XDIM = WINDOW_XDIM - BUFFER
SCREEN_YDIM = WINDOW_YDIM - BUFFER
### of the robot ...
##MAX_XPOS = SCREEN_XDIM//2 - RADIUS
##MAX_YPOS = SCREEN_YDIM//2 - RADIUS 

class Arena:
    def __init__(self):
        self.Sc = turtle.getscreen()
        self.drawingWindow = turtle.Turtle()
        self.drawingWindow.ht()
        self.Sc.setup(WINDOW_XDIM,WINDOW_YDIM)
        self.drawPlayArea()
        self.lights = []
        self.creatures = []
        self.elements = []
    def drawPlayArea(self) :
        # robot moves only within the filled in play area
        self.drawingWindow.hideturtle()
        self.drawingWindow.pu()
        self.drawingWindow.goto(-SCREEN_XDIM//2,-SCREEN_YDIM//2)
        self.drawingWindow.color('black','light blue')
        self.drawingWindow.pd()
        self.drawRectangle( self.drawingWindow, SCREEN_XDIM, SCREEN_YDIM )
    def drawRectangle(self, inTurtle, width, height) :
        # assumes fill color already specified for inTurtle
        inTurtle.begin_fill()
        inTurtle.begin_poly()  
        for el in [ width, height, width, height ]:
            inTurtle.fd(el)          
            inTurtle.left(90)
        inTurtle.end_poly()
        inTurtle.end_fill()
    def addLight(self,light): # setter for adding lights
        self.lights.append(light)
        self.elements.append(light)
        light.draw()
    def addCreature(self,creature): # setter for adding Creatures
        self.creatures.append(creature)
        self.elements.append(creature)
        creature.draw()
    def HeadingBound(self): #bounds the headings between -pi and pi for easier arctan to angle comparisons
        for el in self.elements:
            if el.heading > math.pi:
                el.heading -= 2* math.pi
            if el.heading < -math.pi:
                el.heading += 2*math.pi
            
    def Update(self): #the updater
        for li in self.lights:
            if li.random == True:
                if random.randint(0,1000) == 1:
                    li.RandomHeading() #a one in a thousand chance to randomly change direction if it is allowed to
            else:
                None
        for cr in self.creatures:
            cr.ClosestLight(self.lights)
            cr.HeadingModify()
            cr.CreatureRepulsion(self.creatures)
        self.HeadingBound()
        for el in self.elements:
            el.move(1)
            el.checkCollisionEntity(self.elements)
            el.checkCollisionWall()
            el.draw()
            turtle.update()
    def ConfigEntities(self,ClassList): #incharge of getting entity data from the config file
        # assumes the order of the entities is Creature Creature Lights, based on the two config examples, this was a fair assumtion
        CreatureA = ClassList[0]
        CreatureB = ClassList[1]
        Lights        = ClassList[2]
        for i in range(Lights.count):
            self.addLight((Light(Lights.speed,Lights.random)))
        for i in range(CreatureA.count):
            self.addCreature(Creature(CreatureA.speed,CreatureA.attract,CreatureA.space))
        for i in range(CreatureB.count):
            self.addCreature(Creature(CreatureB.speed,CreatureB.attract,CreatureB.space))

def main(): # it actually contains a minimal amount of code this time :)
    arena = Arena()
    arena.ConfigEntities(configuration.example[0]) #this is where you change the configuration
    turtle.tracer(0,0)
    try:
        while True:
            arena.Update()
    except KeyboardInterrupt:
        print('Swarming Complete')
    

if __name__ == '__main__':
    main()

'''
Drawing function and the Base class were derived from the Robot example given in the class repository
'''
