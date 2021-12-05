from p5_code.vector import Vector


class Grid:
    def __init__(self):
        self.res = 20
        self.num_cols = int(width/self.res)
        self.num_rows = int(height/self.res)
        self.size = Vector(self.num_cols,self.num_rows)
    