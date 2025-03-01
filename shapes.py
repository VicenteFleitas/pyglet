# import sys
# import os

# sys.path.append(os.path.dirname(os.path.dirname(__file__) + "/../util"))

from pyglet import app, shapes
from pyglet.window import Window
import pyglet

# from util.constant import *

window = Window(width=512, height=256)

batch = pyglet.graphics.Batch()

square = shapes.Rectangle(
    x=0, y=0,
    width=32, height=32, color=(155,25,25), batch=batch
)
square.anchor_position = 16, 16

@window.event
def on_draw():
    window.clear()
    batch.draw()

app.run()