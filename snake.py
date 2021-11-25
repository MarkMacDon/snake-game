from random import randint
from p5.pmath.vector import Vector
from p5 import floor

class Snake:
    def __init__(self):
        self.res = 20
        self.position = Vector(0,0)
        self.velocity = Vector(0,0)
        self.size = Vector(self.res,self.res)
        self.length = 0

    def move(self):
        self.position += self.velocity

    def direction(self, direction):
        if direction == "UP":
            self.velocity = Vector(0,-self.res)
        if direction == "DOWN":
            self.velocity = Vector(0,self.res)
        if direction == "LEFT":
            self.velocity = Vector(-self.res,0)
        if direction == "RIGHT":
            self.velocity = Vector(self.res,0)

