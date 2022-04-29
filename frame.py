import curses
from curses import wrapper

stdscr = curses.initscr()

class FrameWriter:
    def __init__(self):
        self.currrent_frame_data = "Initializing..."
        self.on_render_function = lambda: None
        self.frame = 0

    def start(self):
        while True:
            self.render()
            self.frame += 1

    def render(self):
        try:
            stdscr.clear()
            stdscr.addstr(self.currrent_frame_data)
            self.on_render_function()
            stdscr.refresh()
        except:
            curses.endwin()
            raise

    def on_render(self, func):
        self.on_render_function = func

    def write(self, data):
        self.currrent_frame_data = data

    def clear(self):
        self.currrent_frame_data = ""

# test
if __name__ == '__main__':
    frame_writer = FrameWriter()
    frame_writer.write("Hello World!")
    frame_writer.start()
