from pynput.keyboard import Key, Listener

class HomeScreen:
    def __init__(self, parent):
        self.parent = parent

    def render(self, dimensions):
        # center the text
        x = int(dimensions[0] / 2)
        y = int(dimensions[1] / 2)

        width = len("Hello World!")
        height = 1

        string = ""
        
        for i in range(0, int(y / 2)):
            string += "\n"
        
        for i in range(0, int(x / 2) - width):
            string += " "

        string += "Hello World!"

        for i in range(0, int(y / 2)):
            string += "\n"



        return string
