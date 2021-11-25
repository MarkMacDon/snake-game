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
        rect((self.snake.position), self.snake.size.x,self.snake.size.y)
        rect((self.food.position), self.food.size.x, self.food.size.y)


    def check_food(self):
        if self.snake.position == self.food.position:
            self.food.new_position()
        else:
            pass