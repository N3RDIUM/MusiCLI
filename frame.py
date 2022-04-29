import curses
from curses import wrapper

stdscr = curses.initscr()

FRAME_RATE_LIMIT = 60

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
            # convert to array
            data = self.currrent_frame_data.split("\n")
            # limit rows and columns
            rows, columns = stdscr.getmaxyx()
            if len(data) > rows:
                data = data[:rows]
            for i in range(len(data)):
                if len(data[i]) > columns:
                    data[i] = data[i][:columns]
            # write to screen
            for i in range(len(data)):
                stdscr.addstr(i, 0, data[i])
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
