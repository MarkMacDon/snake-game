from random import randint
from p5.pmath.vector import Vector
from p5 import floor
import numpy as np

class Snake:
    def __init__(self):
        self.res = 20
        self.head = Vector(0,0)
        self.velocity = Vector(0,0)
        self.size = Vector(self.res,self.res)
        self.length = 0
        self.body = np.array([Vector(0,0), Vector(0,0), Vector(0,0)])

    
    def grow(self):
        self.length += 1
        np.append(self.body, Vector(0,0))
        
    def move(self):
        self.body[2]= self.body[1]
        self.body[1]= self.body[0]
        self.head += self.velocity
        self.body[0]= self.head

        print(self.body)

    def direction(self, direction):
        if direction == "UP":
            self.velocity = Vector(0,-1)
        if direction == "DOWN":
            self.velocity = Vector(0,1)
        if direction == "LEFT":
            self.velocity = Vector(-1,0)
        if direction == "RIGHT":
            self.velocity = Vector(1,0)

