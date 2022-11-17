from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt6.QtWidgets import QWidget


class Canvas(QWidget):

    def __init__(self):
        super().__init__()

        self.image = QPixmap("./icons/canvas.png")  # documentation: https://doc.qt.io/qt-6/qpixmap.html
        self.image.fill(Qt.GlobalColor.white)  # documentation: https://doc.qt.io/qt-6/qpixmap.html#fill

        # Draw settings (default)
        self.drawing = False
        self.tool_size = 3
        self.tool_color = "#000000"  # documentation: https://doc.qt.io/qt-6/qt.html#GlobalColor-enum

        # Reference to last point recorded by mouse
        self.last_point = QPoint()  # documentation: https://doc.qt.io/qt-6/qpoint.html

    # Slots ========================================
    def change_tool_size(self, px_size):
        self.tool_size = px_size

    def change_tool_color(self, color):
        self.tool_color = color

    def clear(self):
        self.image.fill(Qt.GlobalColor.white)  # fill the image with white
        self.update()  # call the update method of the widget which calls the paintEvent of this class

    # Events =======================================
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:  # if the pressed button is the left button
            self.drawing = True  # enter drawing mode
            self.last_point = event.pos()  # save the location of the mouse press as the lastPoint
            print(self.last_point)  # print the lastPoint for debugging purposes

    def mouseMoveEvent(self, event):
        if self.drawing:
            painter = QPainter(self.image)  # object which allows drawing to take place on an image

            # allows the selection of brush colour, brish size, line type, cap type, join type.
            painter.setPen(QPen(QColor(self.tool_color), self.tool_size, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap,
                                Qt.PenJoinStyle.RoundJoin))

            # draw a line from the point of the original press to the point to where the mouse was dragged to
            painter.drawLine(self.last_point, event.pos())

            # set the last point to refer to the point we have just moved to, this helps when drawing the next segment
            self.last_point = event.pos()

            # call the update method of the widget which calls the paintEvent of this class
            self.update()

    def mouseReleaseEvent(self, event):
        # when the mouse is released

        if event.button() == Qt.MouseButton.LeftButton:  # if the released button is the left button
            self.drawing = False  # exit drawing mode

    def paintEvent(self, event):
        # you should only create and use the QPainter object in this method, it should be a local variable
        canvas_painter = QPainter(self)  # create a new QPainter object, docs: https://doc.qt.io/qt-6/qpainter.html
        canvas_painter.drawPixmap(QPoint(), self.image)  # draw image, https://doc.qt.io/qt-6/qpainter.html#drawImage-1

    def resizeEvent(self, event):
        self.image = self.image.scaled(self.width(), self.height())
