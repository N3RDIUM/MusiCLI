from ui_elements import *
from pynput.keyboard import Key, Listener

class HomeScreen:
    def __init__(self, parent):
        self.parent = parent
        self.scrolling_text = ScrollingSelector(self, ["How are you?", "MusiCLI is a music player for Windows.", "Press enter to start.", "How are you?", "MusiCLI is a music player for Windows.", "Press enter to start.", "How are you?", "MusiCLI is a music player for Windows.", "Press enter to start.", ])
        self.key = None

        self.listener = Listener(on_press=self.on_key_press)
        self.listener.start()

    def on_key_press(self, key):
        self.scrolling_text.on_key_press(key)
        self.key = key

    def render(self, dimensions):
        return self.scrolling_text.render() + "\n" + str(self.key)
