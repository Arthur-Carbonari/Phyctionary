import abc


class DrawingTool:

    def __init__(self, canvas):
        self.canvas = canvas
        self.last_point = None

    @abc.abstractmethod
    def mouse_press(self, event):
        pass

    @abc.abstractmethod
    def mouse_drag(self, event):
        pass
