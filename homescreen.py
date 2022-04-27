from pynput.keyboard import Key, Listener

class HomeScreen:
    def __init__(self, parent):
        self.parent = parent
        self.latest_key = None

    def on_key_press(self, key):
        try:
            self.latest_key = key.char
        except:
            pass

    def render(self, dimensions):
        # center the text
        x = int(dimensions[0] / 2)
        y = int(dimensions[1] / 2)

        width = len("Hello World!" + "" if self.latest_key is None else self.latest_key + ":confetti:")
        height = 1

        string = ""
        
        for i in range(0, int(y / 2)):
            string += "\n"
        
        for i in range(0, int(x / 2) - width):
            string += " "
        
        string += "Hello World!" + "" if self.latest_key is None else self.latest_key

        for i in range(0, int(y / 2)):
            string += "\n"



        return string
