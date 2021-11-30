from random import randint
from p5.pmath.vector import Vector
from p5 import floor

class Food:
    def __init__(self):
        self.res = 20
        self.position = Vector(4,4)
        self.size = Vector(self.res,self.res)

    def new_position(self):
        x = randint(0,self.res)
        y = randint(0,self.res)
        self.position = Vector(x,y)
        print(self.position)
               