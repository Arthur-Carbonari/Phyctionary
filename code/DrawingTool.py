import abc

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor


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


class PaintBrush(DrawingTool):

    def mouse_press(self, event):
        self.last_point = event.pos()  # save the location of the mouse press as the lastPoint

    def mouse_drag(self, event):
        painter = QPainter(self.canvas.image)  # object which allows drawing to take place on an image

        # allows the selection of brush colour, brish size, line type, cap type, join type.
        painter.setPen(QPen(QColor(self.canvas.tool_color), self.canvas.tool_size, Qt.PenStyle.SolidLine,
                            Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))

        # draw a line from the point of the original press to the point to where the mouse was dragged to
        painter.drawLine(self.last_point, event.pos())

        # set the last point to refer to the point we have just moved to, this helps when drawing the next segment
        self.last_point = event.pos()
