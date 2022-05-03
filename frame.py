import curses
from curses import wrapper

stdscr = curses.initscr()

FRAME_RATE_LIMIT = 60

class FrameWriter:
    def __init__(self):
        self.stdscr = stdscr
        self.on_render_function = lambda: None
        self.frame = 0

    def start(self):
        while True:
            self.render()
            self.frame += 1

    def render(self):
        try:
            self.stdscr.clear()

            self.on_render_function()
            stdscr.refresh()
        except:
            curses.endwin()
            raise

    def on_render(self, func):
        self.on_render_function = func

# test
if __name__ == '__main__':
    frame_writer = FrameWriter()
    frame_writer.write("Hello World!")
    frame_writer.start()
