from ui_elements import *

class HomeScreen:
    def __init__(self, parent):
        self.parent = parent
        self.latest_key = None

        self.scrolling_text = ScrollingText(self, "Hello World! You are using a MusiCLI Preview version!")

    def on_key_press(self, key):
        try:
            self.latest_key = key.char
        except:
            pass

    def render(self, dimensions):
        # center the text
        x = int(dimensions[0] / 2)
        y = int(dimensions[1] / 2)

        t = self.scrolling_text.render()

        width = len(t)
        height = 1

        string = ""
        
        for i in range(0, int(y / 2)):
            string += "\n"
        
        for i in range(0, int(x / 2) - width):
            string += " "
        
        string += t + "" if self.latest_key is None else self.latest_key

        for i in range(0, int(y / 2)):
            string += "\n"

        return string
