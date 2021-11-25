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
        self.food_position = Vector(0,0)
        self.num_cols = floor(width/self.res)
        self.num_rows = floor(height/self.res)



    def new_food_position(self):
        x = randint(0,self.num_cols)*self.res
        y = randint(0,self.num_rows)*self.res

        self.food_position = Vector(x,y)
               
    def get_size(self):
        return self.size


    def eat(self):
        if self.position == self.food_position:
            self.new_food_position()
        else:
            pass
        
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

