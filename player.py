from pynput.keyboard import Key, Listener
import win32gui

import homescreen

def get_dimensions():
    import os
    size = os.get_terminal_size()
    return size.columns * 2, size.lines * 2

def get_console_window_focus():
    import ctypes
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetConsoleWindow()
    if handle == win32gui.GetForegroundWindow():
        return True
    return False

class Player:
    def __init__(self, parent):
        self.parent = parent

        self.current = "home"

        self.screens = {
            "home": homescreen.HomeScreen(self),
        }

        self.state = {}
    
        # keylogger
        self.listener = Listener(on_press=self.on_key_press)
        self.listener.start()

    def on_key_press(self, *args, **kwargs):
        if get_console_window_focus():
            self.screens[self.current].on_key_press(*args, **kwargs)

    def render(self, dimensions):
        return self.screens[self.current].render(dimensions)

    def set_screen(self, screen):
        self.current = screen
