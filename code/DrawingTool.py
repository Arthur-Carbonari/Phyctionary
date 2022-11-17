import abc
import random

from PyQt6.QtCore import Qt, QRect, QPoint, QSize
from PyQt6.QtGui import QPainter, QPen, QColor


class DrawingTool:

    def __init__(self, canvas):
        self.canvas = canvas
        self.last_point = None

    def mouse_press(self, event):
        # save the location of the mouse press as the lastPoint
        self.last_point = event.pos()

    @abc.abstractmethod
    def mouse_drag(self, event):
        pass


class PaintBrush(DrawingTool):

    def mouse_drag(self, event):
        painter = QPainter(self.canvas.image)  # object which allows drawing to take place on an image

        # allows the selection of brush colour, brish size, line type, cap type, join type.
        painter.setPen(QPen(QColor(self.canvas.tool_color), self.canvas.tool_size, Qt.PenStyle.SolidLine,
                            Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))

        # draw a line from the point of the original press to the point to where the mouse was dragged to
        painter.drawLine(self.last_point, event.pos())

        # set the last point to refer to the point we have just moved to, this helps when drawing the next segment
        self.last_point = event.pos()


class Eraser(DrawingTool):

    def mouse_press(self, event):
        super().mouse_press(event)
        self._erase(event)

    def mouse_drag(self, event):
        self._erase(event)

    def _erase(self, event):
        painter = QPainter(self.canvas.image)

        painter.setPen(QPen(QColor(255, 255, 255, 0), 1, Qt.PenStyle.SolidLine,
                            Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))

        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Clear)

        rec = QRect(QPoint(), self.canvas.tool_size * 5 * QSize())
        rec.moveCenter(event.pos())
        painter.eraseRect(rec)

        self.last_point = event.pos()


class PaintSpray(DrawingTool):

    def __init__(self, canvas):
        super(PaintSpray, self).__init__(canvas)

        self.spray_particles = 100

    def mouse_press(self, event):
        self._spray(event)

    def mouse_drag(self, event):
        self._spray(event)

    def _spray(self, event):
        painter = QPainter(self.canvas.image)
        painter.setPen(QPen(QColor(self.canvas.tool_color), 1))

        for n in range(self.spray_particles):
            xo = random.gauss(0, self.canvas.tool_size)
            yo = random.gauss(0, self.canvas.tool_size)

            painter.drawPoint(int(event.position().x() + xo), int(event.position().y() + yo))
