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
        self.length = 3
        self.body = np.array([[Vector(0,0)], [Vector(0,0)], [Vector(0,0)]])


    def grow(self):
        self.length += 1
        # print(f"Body at grow state:{self.body}")
        # print(f"Body shape at grow state:{self.body.shape, type(self.body)}")
        self.body = np.append(self.body, Vector(0,0))
        self.body = np.reshape(self.body, (self.length,1, 3))
        print(f"body after grow state {self.body}")

        print(f"Body shape after grow state:{self.body.shape, type(self.body)}")


    def move(self):
        for i in reversed(range(len(self.body))):
            self.body[i] = self.body[i-1]
        self.body[0] = self.head
        # print(self.head, self.body[0])
        self.head += self.velocity

    def direction(self, direction):
        if direction == "UP":
            self.velocity = Vector(0,-1)
        if direction == "DOWN":
            self.velocity = Vector(0,1)
        if direction == "LEFT":
            self.velocity = Vector(-1,0)
        if direction == "RIGHT":
            self.velocity = Vector(1,0)

