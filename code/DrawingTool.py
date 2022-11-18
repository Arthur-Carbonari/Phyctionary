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
        painter = QPainter(self.canvas.drawing)  # object which allows is_drawing to take place on a drawing

        # allows the selection of brush colour, brish size, line type, cap type, join type.
        painter.setPen(QPen(QColor(self.canvas.tool_color), self.canvas.tool_size, Qt.PenStyle.SolidLine,
                            Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin))

        # draw a line from the point of the original press to the point to where the mouse was dragged to
        painter.drawLine(self.last_point, event.pos())

        # set the last point to refer to the point we have just moved to, this helps when is_drawing the next segment
        self.last_point = event.pos()


class Eraser(DrawingTool):

    def mouse_press(self, event):
        super().mouse_press(event)
        self._erase(event)

    def mouse_drag(self, event):
        self._erase(event)

    def _erase(self, event):
        painter = QPainter(self.canvas.drawing)

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
        painter = QPainter(self.canvas.drawing)
        painter.setPen(QPen(QColor(self.canvas.tool_color), 1))

        for n in range(self.spray_particles):
            xo = random.gauss(0, self.canvas.tool_size)
            yo = random.gauss(0, self.canvas.tool_size)

            painter.drawPoint(int(event.position().x() + xo), int(event.position().y() + yo))


class PaintBucket(DrawingTool):

    def __init__(self, canvas):
        super().__init__(canvas)

        self.img = canvas.drawing.toImage()
        self.h = self.img.height()
        self.w = self.img.width()

    def mouse_press(self, event):
        self.img = self.canvas.drawing.toImage()

        self.h = self.img.height()
        self.w = self.img.width()

        click_x, click_y = event.pos().x(), event.pos().y()

        target_color = self.img.pixel(click_x, click_y)

        painter = QPainter(self.canvas.drawing)
        painter.setPen(QColor(self.canvas.tool_color))

        check_queue = [(click_x, click_y)]
        already_checked = set()

        while check_queue:
            current_x, current_y = check_queue.pop()

            if self.img.pixel(current_x, current_y) == target_color:

                # Fills the pixel with the active tool color
                painter.drawPoint(current_x, current_y)

                # Adds the surrounding pixels to the check_queue
                check_queue = self._get_surrounding_pixels(already_checked, current_x, current_y) + check_queue

        self.canvas.update()

    def mouse_drag(self, event):
        pass

    def _get_surrounding_pixels(self, already_checked, center_x, center_y):
        points = []

        for x_var, y_var in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            x = center_x + x_var
            y = center_y + y_var

            if 0 <= x < self.w and 0 <= y < self.h:
                if (x, y) not in already_checked:
                    points.append((x, y))
                    already_checked.add((x, y))
                else:
                    print("already checked")

        return points


