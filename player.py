import homescreen

def get_dimensions():
    import os
    size = os.get_terminal_size()
    return size.columns * 2, size.lines * 2

class Player:
    def __init__(self, parent):
        self.parent = parent

        self.current = "home"

        self.screens = {
            "home": homescreen.HomeScreen(self),
        }

    def render(self, dimensions):
        return self.screens[self.current].render(dimensions)

    def set_screen(self, screen):
        self.current = screen
