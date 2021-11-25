from p5 import size, background, rect
from snake import Snake

class SketchManager:
    def __init__(self):
        self.snake = Snake()

    def setup(self):
        size(400,400)

    def draw(self):
        background(0)
        self.snake.move()
        self.snake.eat()
        rect((self.snake.position), self.snake.size.x,self.snake.size.y)
        rect((self.snake.food_position), self.snake.size.x, self.snake.size.y)
        
    def key_pressed(self, event):
        if event.key == "UP":
            self.snake.direction("UP")

        if event.key == "DOWN":
            self.snake.direction("DOWN")

        if event.key == "LEFT":
            self.snake.direction("LEFT")

        if event.key == "RIGHT":
            self.snake.direction("RIGHT")

        if event.key == " ":  # space
            self.snake.new_food_position()

