from p5_code.vector import Vector
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
        self.body = np.append(self.body, Vector(0,0))
        self.body = np.reshape(self.body, (self.length,1, 3))
        print(self.body)


    def move(self):
        for i in reversed(range(len(self.body))):
            self.body[i] = self.body[i-1]
        self.body[0] = self.head
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

