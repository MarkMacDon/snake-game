from p5 import rect
from snake import Snake
from grid import Grid
from food import Food

class GameManager:
    def __init__(self):
        self.snake = Snake()
        self.grid = Grid()
        self.food = Food()

    def update(self):
        self.snake.move()
        self.check_food()
        # rect((self.snake.head*self.grid.res), self.snake.size.x,self.snake.size.y)
        rect((self.food.position*self.grid.res), self.food.size.x, self.food.size.y)
        for part in self.snake.body:
            rect((part*self.grid.res), self.snake.size.x,self.snake.size.y)
            

    def check_food(self):
        if self.snake.head == self.food.position:
            self.food.new_position()
            self.snake.grow()
        else:
            pass