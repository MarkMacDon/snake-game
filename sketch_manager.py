from p5 import size, background, rect
from game_manager import GameManager


class SketchManager:
    def __init__(self):
        self.gm = GameManager()

    def setup(self):
        size(400,400)

    def draw(self):
        background(0)
        self.gm.update()

    def key_pressed(self, event):
        if event.key == "UP":
            self.gm.snake.direction("UP")

        if event.key == "DOWN":
            self.gm.snake.direction("DOWN")

        if event.key == "LEFT":
            self.gm.snake.direction("LEFT")

        if event.key == "RIGHT":
            self.gm.snake.direction("RIGHT")

        if event.key == " ":  # space
            self.gm.food.new_position()

