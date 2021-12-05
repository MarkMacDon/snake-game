from p5 import size, background
from game_manager import GameManager
from request import HttpInput


class SketchManager:
    def __init__(self):
        self.game = GameManager()
        self.input_mode = 0
        self.http_input = HttpInput()

    def setup(self):
        size(400, 400)
        self.input_mode = input(
            "input_mode - Enter 0 for keyboard or 1 for gesture over http")

    def draw(self):
        background(0)
        self.game.update()
        if self.input_mode == "1":
            print(self.http_input.get_input())

            self.http_control(self.http_input.get_input())

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

    def http_control(self, event):
        if event == "Up":
            self.game.snake.direction("UP")

        if event == "Down":
            self.game.snake.direction("DOWN")

        if event == "Left":
            self.game.snake.direction("LEFT")

        if event == "Right":
            self.game.snake.direction("RIGHT")

        if event == " ":  # space
            self.game.snake.grow()
