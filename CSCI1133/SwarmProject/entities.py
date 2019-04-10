import math
import turtle
import random
import collision
from collision import Vector,Velocity,DetermineNewHeading


class Position :
    # A data structure to conveniently hold an x,y position
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Base:
    def __init__(self,SPEED):
        self.radius = 10
        self.position = Position(random.randint(-350,350),random.randint(-300,300))
        self.heading = random.uniform(0, 2*math.pi)
        self.robot = turtle.Turtle()
        self.robot.hideturtle()
        self.speed = SPEED;
        self.MAX_XPOS = 365
        self.MAX_YPOS = 310
        self.vel = None
        self.type = 'light'
        self.color = 'yellow'
        

    def draw(self) :
        self.robot.speed(0)
        self.robot.clear()
        self.robot.hideturtle()
        self.robot.color(self.color)
        self.robot.penup()
        self.robot.goto(self.position.x, self.position.y)
        self.robot.dot(self.radius*2)
        deltaX = self.radius*math.cos(self.heading)
        deltaY = self.radius*math.sin(self.heading)
        self.robot.goto(self.position.x+deltaX,self.position.y+deltaY)
        self.robot.dot(self.radius*.75)

    def move(self, dt ):
        distance = dt*self.speed
        deltaX = distance*math.cos(self.heading)
        deltaY = distance*math.sin(self.heading)
        self.position.x += deltaX
        self.position.y += deltaY
    def checkCollisionWall(self):
        if self.position.x > self.MAX_XPOS or self.position.x < -1*self.MAX_XPOS:
            self.bouncex()
        if self.position.y > self.MAX_YPOS or self.position.y < -1*self.MAX_YPOS:
            self.bouncey()
    def bouncex(self): #bouncex and bouncy are for wall collision.
        self.heading = math.pi - self.heading
        
    def bouncey(self):
        self.heading =-1*self.heading

    def checkCollisionEntity(self,elements): #elements is a list of entities in the arena
        new_elements = [el for el in elements]
        if self in new_elements:
            new_elements.remove(self)
        self.vel = Velocity(self.heading,self.speed)
        for el in new_elements:
            #distance is center to center
            distance = ((self.position.x-el.position.x)**2 + (self.position.y - el.position.y)**2)**(.5)
            if distance - 2* self.radius <= 1:
                DetermineNewHeading(self,el)
                self.move(1)
        

class Light(Base):
    def __init__(self,SPEED,RANDOM):
        Base.__init__(self,SPEED)
        self.random = RANDOM
    def RandomHeading(self):
        self.heading = random.uniform(-math.pi,math.pi)

class Creature(Base):
    def __init__(self,SPEED,attracted,SPACE):
        Base.__init__(self,SPEED)
        self.radius = 5
        self.attracted = attracted
        self.type = 'creature'
        self.color = None
        self.closest_light = None
        self.DetermineColor()
        self.speed = SPEED
        self.space = SPACE
    def DetermineColor(self): # determines the color of the creature based on whether or not it is attracted to the light
        if self.attracted == True:
            self.color = 'green'
        else:
            self.color = 'red'
    def ChangeRepelled(self,angle_to,distance,multiplier): # the thing that actually changes the heading if it is repelled
        if self.heading > 0 and angle_to > 0:
            if self.heading > angle_to:
                self.heading -= (.1/(distance)**.35)*multiplier
            else:
                self.heading += (.1/(distance)**.35)*multiplier
        elif self.heading < 0 and angle_to < 0:
            if self.heading > angle_to:
                self.heading -= (.1/(distance)**.35)*multiplier
            else:
                self.heading += (.1/(distance)**.35)*multiplier
        elif self.heading > 0 and angle_to < 0:
            if self.heading - math.pi < angle_to:
                self.heading -= (.1/(distance)**.35)*multiplier
            else:
                self.heading += (.1/(distance)**.35)*multiplier
        elif self.heading < 0 and angle_to > 0:
            if self.heading + math.pi > angle_to:
                self.heading += (.1/(distance)**.35)*multiplier
            else:
                self.heading -= (.1/(distance)**.2)*multiplier
    def RepelledHeading(self): #the base repell from light function
        d_x = -(self.position.x - self.closest_light.position.x)
        d_y = -(self.position.y - self.closest_light.position.y)
        angle_to = math.atan2(d_y,d_x) - math.pi
        if angle_to < - math.pi:
            angle_to += 2*math.pi
        distance = (d_x**2 + d_y**2)**.5
        if distance > 250:
            None
        else:
            self.ChangeRepelled(angle_to,distance,2)
    def AttractedHeading(self): # determines heading if attracted. This made me want to die.
        d_x = -(self.position.x - self.closest_light.position.x)
        d_y = -(self.position.y - self.closest_light.position.y)
        angle_to = math.atan2(d_y,d_x)
        distance = (d_x**2 + d_y**2)**.5
        if distance < 25:
            None
        else: #the nested if loop; its gotta happen at least once
            if self.heading > 0 and angle_to > 0:
                if self.heading > angle_to:
                    self.heading -= .1/(distance)**.2
                else:
                    self.heading += .1/(distance)**.2
            elif self.heading < 0 and angle_to < 0:
                if self.heading > angle_to:
                    self.heading -= .1/(distance)**.2
                else:
                    self.heading += .1/(distance)**.2
            elif self.heading > 0 and angle_to < 0:
                if self.heading - math.pi < angle_to:
                    self.heading -= .1/(distance)**.2
                else:
                    self.heading += .1/(distance)**.2
            elif self.heading < 0 and angle_to > 0:
                if self.heading + math.pi > angle_to:
                    self.heading += .1/(distance)**.2
                else:
                    self.heading -= .1/(distance)**.2
    def Spacing(self,DistList): # helper for passing into the Repell function
        creatures = [el[0] for el in DistList]
        angles = [el[2] for el in DistList]
        distances = [el[1] for el in DistList]
        for i in range(len(creatures)):
            self.ChangeRepelled(angles[i],distances[i],3)
            
        
    def CreatureRepulsion(self,Creatures): #creatures is the list of creatures
        new_creatures = [el for el in Creatures]
        within_bubble = []
        for el in new_creatures:
            distance = None
            d_x = (self.position.x - el.position.x)
            d_y = (self.position.y - el.position.y)
            angle_to = math.atan2(d_y,d_x)
            if angle_to < -math.pi:
                angle_to += 2*math.pi
            distance =  ((d_x**2)+(d_y**2))**.5
            if distance != 0 and distance < self.space:
                within_bubble.append((el,distance,angle_to))
        if within_bubble:
            self.Spacing(within_bubble)
        
                
        
        
    def HeadingModify(self): #sends the creature to the appropriate heading modifier
        if self.attracted == True:
            self.AttractedHeading()
        else:
            self.RepelledHeading()
    def ClosestLight(self,lights): #finds the closest light
        new_lights = [el for el in lights]
        light_distances = []
        for el in new_lights:
            distance = None
            distance = ((self.position.x-el.position.x)**2 + (self.position.y - el.position.y)**2)**.5
            light_distances.append(distance)
        min_distance = min(light_distances)
        for i in range(len(light_distances)):
            if light_distances[i] == min_distance: # i is also the index of the light in new_lights
                self.closest_light = new_lights[i]
                break
    
    














#
