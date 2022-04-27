from player import *
from frame import *

dimensions = get_dimensions()
frame_writer = FrameWriter()
_screens = Player(frame_writer)

def onrender():
    dimensions = get_dimensions()
    frame_writer.write(_screens.render(dimensions))

if __name__ == '__main__':
    frame_writer.on_render(onrender)
    frame_writer.start()
