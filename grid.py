from p5 import floor, Vector

class Grid:
    def __init__(self):
        self.res = 20
        self.num_cols = floor(width/self.res)
        self.num_rows = floor(height/self.res)
        self.size = Vector(self.num_cols,self.num_rows)
    