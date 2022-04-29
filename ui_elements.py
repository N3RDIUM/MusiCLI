from pynput.keyboard import Key

class UIElementBase():
    def __init__(self, parent):
        self.parent = parent

class Text(UIElementBase):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.text = text

    def render(self):
        return self.text

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

        if self.frame % 400 == 0:
            self.index += 1

        if self.index >= len(self.text):
            self.index = 0

        string = self.text[self.index:self.index + self.length] + " "

        if len(string) < self.length:
            string += self.text[:self.length - len(string)]

        return "[" + string + "]"

class ScrollingSelector(UIElementBase):
    def __init__(self, parent, options, selected_index=0, heightrange = 2):
        super().__init__(parent)
        self.options = options
        self.selected_index = selected_index
        self.heightrange = heightrange
        self.frame = 0

        self.selected = None

        self.current_animation = [">", "-", "—", "-"]
        self.current_animation_index = 0

    def on_key_press(self, key):
        if key == Key.up:
            self.selected_index -= 1
            if self.selected_index < 0:
                self.selected_index = len(self.options) - 1
        elif key == Key.down:
            self.selected_index += 1
            if self.selected_index >= len(self.options):
                self.selected_index = 0
        elif key == Key.enter:
            self.selected = self.options[self.selected_index]

    def render(self):
        # increment frame
        self.frame += 1

        if self.frame % 400 == 0:
            self.current_animation_index += 1

            if self.current_animation_index >= len(self.current_animation) - 1:
                self.current_animation_index = 0

        string = ""

        _range = range(self.selected_index - self.heightrange, self.selected_index + self.heightrange + 1)
        for i in _range:
            if i < 0 or i >= len(self.options):
                continue

            if i == self.selected_index:
                string += self.current_animation[self.current_animation_index] + " " + self.options[i] + "\n"
            else:
                string += "  " + self.options[i] + "\n"

        if len(string) < self.heightrange * 2 + 1:
            string = "  " * (self.heightrange - len(_range) / 2) + string

        # if a selection has been made, return it
        if self.selected is not None:
            return string + "\n" + self.selected

        return string
