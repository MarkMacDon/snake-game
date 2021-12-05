# This talks to Processing p5.py and includes 
# the setup, draw and run() functions needed to run p5 sketches

from p5 import *
from sketch_manager import SketchManager

sketch = SketchManager()


def setup():
    sketch.setup()


def draw():
    sketch.draw()


def key_pressed(event):
    sketch.key_pressed(event)


run()
