import os
from time import sleep
import ctypes
import rich # print rich text
kernel32 = ctypes.windll.kernel32

def get_dimensions():
    import os
    size = os.get_terminal_size()
    return size.columns * 2, size.lines * 2

def _cls(nrow = 0):
    if nrow == 0:
        os.system('cls')
    else:
        print('\033[F'*nrow)

def _display(chars):
    print(''.join(chars))
    return len(chars)

MAX_FRAME_RATE = 60

class FrameWriter:
    def __init__(self):
        self.currrent_frame_data = ""
        self.on_render_function = lambda: None
        self.previous_frame_data = None
        self.frame_rate = MAX_FRAME_RATE
        self.first_drawcall = True

        self.frame = 0
        self.nrow = 0
        self.i = 0

    def quickedit(self, enabled): # This is a patch to the system that sometimes hangs
        if enabled:
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x40|0x100))
        elif enabled == 0:
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100))
    
    def start(self):
        self.quickedit(0)
        os.system('mode horizontalSizeInNumber or horizontalSizeInNumber_setToZero and verticalSizeInNumber')
        while True:
            try:
                if self.first_drawcall:
                    self.first_drawcall = False
                    self.on_render_function()

                if self.previous_frame_data != self.currrent_frame_data:
                    array = self.currrent_frame_data.split("\n")

                    self.i+=1

                    if self.i >= len(array):
                        self.i = 0

                    rich.print(array[self.i])

                    self.nrow = _display(self.currrent_frame_data)

                # set previous frame data
                self.previous_frame_data = self.currrent_frame_data

                self.on_render_function()
            except KeyboardInterrupt:
                self.quickedit(1) 
                break
            self.frame += 1
        self.quickedit(1)

    def on_render(self, func):
        self.on_render_function = func

    def write(self, data):
        self.previous_frame_data = self.currrent_frame_data
        self.currrent_frame_data = data

    def clear(self):
        self.currrent_frame_data = ""

# test
if __name__ == '__main__':
    frame_writer = FrameWriter()
    frame_writer.write("Hello World!")
    frame_writer.start()
