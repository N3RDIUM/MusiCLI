from ui_elements import *
from pynput.keyboard import Key, Listener
import curses
from curses import panel

def make_panel(x, y, width, height):
    _panel = curses.newwin(height, width, y, x)
    _panel = panel.new_panel(_panel)
    _panel.top()
    return _panel

class HomeScreen:
    def __init__(self, parent):
        self.parent = parent
        self.dimensions = self.parent.parent.stdscr.getmaxyx()

        # Make all the panels
        self.panels = {
            "side-navbar": make_panel(0, 0, 30, self.dimensions[0]),
            "main-content": make_panel(30, 0, self.dimensions[1] - 30, self.dimensions[0])
        }

        self.listener = Listener(on_press=self.on_key_press)
        self.listener.start()

        self.num = 0

    def on_key_press(self, key):
        pass

    def render(self):
        self.dimensions = self.parent.parent.stdscr.getmaxyx()

        win = self.panels["side-navbar"].window()
        win.border()
        win.addstr(1, 1, "Sidebar")
        win.refresh()

        win = self.panels["main-content"].window()
        win.border()
        win.addstr(1, 1, "Home")
        win.refresh()

        return ""
