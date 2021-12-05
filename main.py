from p5 import run
from sketch_manager import SketchManager

# This talks to Processing p5.py and includes
# the setup, draw and run() functions needed to run p5 sketches

# SketchManager is added for object oriented definition of setup and draw
sketch = SketchManager()


def setup():
    sketch.setup()


def draw():
    sketch.draw()


def key_pressed(event):
    sketch.key_pressed(event)


run()
