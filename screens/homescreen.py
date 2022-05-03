from ui_elements import *
from pynput.keyboard import Key, Listener
import curses
from curses import panel

class HomeScreen:
    def __init__(self, parent):
        self.parent = parent
        self.dimensions = self.parent.parent.stdscr.getmaxyx()

        # Make all the panels
        self.panels = {
            "side-navbar": panel.new_panel(self.parent.parent.stdscr),
        }

        self.listener = Listener(on_press=self.on_key_press)
        self.listener.start()

        self.num = 0

    def on_key_press(self, key):
        pass

    def render(self):
        self.dimensions = self.parent.parent.stdscr.getmaxyx()

        self.panels["side-navbar"] = panel.new_panel(self.parent.parent.stdscr)
        win = self.panels["side-navbar"].window()
        win.resize(self.dimensions[0], 30)

        win.clear()
        win.border()
        win.addstr(1, 1, str(self.num))
        self.num += 1

        return "SDF"
