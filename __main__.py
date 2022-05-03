from player import *
from frame import *

dimensions = get_dimensions()
frame_writer = FrameWriter()
_screens = Player(frame_writer)

if __name__ == '__main__':
    frame_writer.on_render(_screens.render)
    frame_writer.start()
