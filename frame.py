import os
from time import sleep
import ctypes
kernel32 = ctypes.windll.kernel32

MAX_FRAME_RATE = 60

class FrameWriter:
    def __init__(self):
        self.currrent_frame_data = ""
        self.on_render_function = None
        self.dt = 0
        self.previous_frame_data = None
        self.frame_rate = MAX_FRAME_RATE
        self.first_drawcall = True

    def quickedit(self, enabled): # This is a patch to the system that sometimes hangs
        if enabled:
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x40|0x100))
        elif enabled == 0:
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4|0x80|0x20|0x2|0x10|0x1|0x00|0x100))
    
    def start(self):
        self.quickedit(0)
        while True:
            try:
                if self.currrent_frame_data != self.previous_frame_data:
                    os.system('cls')
                    print(self.currrent_frame_data)

                if self.on_render_function:
                    self.on_render_function()

                # set DT
                self.dt = 1 / MAX_FRAME_RATE

                # sleep
                sleep(self.dt)

                # set previous frame data
                self.previous_frame_data = self.currrent_frame_data

                # set first drawcall
                self.first_drawcall = False
            except KeyboardInterrupt:
                self.quickedit(1) 
                exit()

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
