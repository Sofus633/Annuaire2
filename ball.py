import pygame, random
from vector import Vector3
from settings import screen_size
import math

class Ball:
    def __init__(self,position=(random.randint(0, screen_size[0]), random.randint(0, screen_size[1]), 0), color=(0, 0, 0), radius=5, vector=Vector3((1, 0, 0)), destination=None, nom=None, num=None):
        #position
        self.position = position
        self.vector = vector
        self.radius = radius
        self.destination = destination
        self.oncontrole = False
        self.mindist = 1
        self.stabilise = False

        #display
        self.color = color
        self.nom = nom 
        self.num = num
        self.display = False
        self.font = pygame.font.SysFont('Consolas', self.radius)

    def update(self):
        # When f is pressed
        if self.oncontrole == True and self.destination is not None:
            dist = distance(self.position, self.destination)
            
            if dist > self.mindist:  
                vect = calculate_collision_direction(self.position, self.destination).normalize()
                force_magnitude = dist / 1000 
                self.vector += vect.neg("xy") * force_magnitude  
                self.mindist += 0.5 if not self.stabilise else 0.1
            else:
                
                if not self.stabilise:
                    self.stabilise = True
                
                if self.mindist != 1:
                    self.mindist = 1
                self.vector = Vector3((0, 0, 0))  
                self.position = self.destination  

        # pos update
        self.position = self.vector.updpos(self.position)
        
        # border collition 
        if self.position[0] >= screen_size[0] or self.position[0] <= 0 :
            self.vector = self.vector.neg("x")
        if ((self.position[1] >= screen_size[1]) if not self.oncontrole else False) or ((self.position[1] < 0) if not self.oncontrole else False): # no up and down collition while on controle (scroll mode)
            self.vector = self.vector.neg("y")

def distance(obj1, obj2):
    """ return distance between 2 balls or 2 positions """
    if type(obj1) == Ball and type(obj2) == Ball:
        return abs(obj1.position[0] - obj2.position[0]) + abs(obj1.position[1] - obj2.position[1])
    else:
        return abs(obj1[0] - obj2[0]) + abs(obj1[1] - obj2[1])

def calculate_collision_direction(ball1, ball2):
    """ return vector representing dirrection after colition """
    if type(ball1) == Ball and type(ball2) == Ball:
        return Vector3((ball1.position[0] - ball2.position [0], ball1.position[1] - ball2.position [1], 0)).normalize()
    else:
        return Vector3((ball1[0] - ball2[0] , ball1[1] - ball2[1], 0)).normalize()

def checkcollitions(balls):
    """ check if any ball is coliding (just checking distance)"""
    print('check coll')
    for i in range(0, len(balls)):
        for j in range(i + 1, len(balls)):
            dist = distance(balls[i], balls[j])
            if dist < 10:
                vect = calculate_collision_direction(balls[i], balls[j])
                balls[i].vector = vect * 1
                balls[j].vector = vect.neg("xy") * 1
    
def createballcircle(position, color=(0, 0, 0)):
    """ return list of ball object in a spiral form (at the origine it was mean to be a circle but i find out this shape and i like it)"""
    a = position[0]
    b = position[1]
    balls = []
    for r in range(0, 600, 3):
        x = a+r*math.cos(r)
        y = b+r*math.sin(r)
        if not x - a == 0 and not 0 == y- b:
            balls.append(Ball((x, y, 0), vector=Vector3((x - a, y- b, 0)).normalize(), color=color))
    return balls

def update_ball(balls):
    for ball in balls:
        ball.update()