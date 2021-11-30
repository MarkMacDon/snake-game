from p5 import size, background, rect
from game_manager import GameManager


class SketchManager:
    def __init__(self):
        self.game = GameManager()

    def setup(self):
        size(400,400)

    def draw(self):
        background(0)
        self.game.update()

    def key_pressed(self, event):
        if event.key == "UP":
            self.game.snake.direction("UP")

        if event.key == "DOWN":
            self.game.snake.direction("DOWN")

        if event.key == "LEFT":
            self.game.snake.direction("LEFT")

        if event.key == "RIGHT":
            self.game.snake.direction("RIGHT")

        if event.key == " ":  # space
            self.game.snake.grow()

