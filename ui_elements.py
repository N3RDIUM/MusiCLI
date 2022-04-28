class UIElementBase():
    def __init__(self, parent):
        self.parent = parent

DEFAULT_SCROLLING_TEXT_LENGTH = 25

class ScrollingText(UIElementBase):
    def __init__(self, parent, text, length=DEFAULT_SCROLLING_TEXT_LENGTH):
        super().__init__(parent)
        self.frame = 0
        self.text = text
        self.length = length

        self.index = 0

    def render(self):
        # increment frame
        self.frame += 1

        if self.frame % 4000 == 0:
            self.index += 1

        if self.index >= len(self.text):
            self.index = 0

        string = self.text[self.index:self.index + self.length] + " "

        if len(string) < self.length:
            string += self.text[:self.length - len(string)]

        return "[" + string + "]"

