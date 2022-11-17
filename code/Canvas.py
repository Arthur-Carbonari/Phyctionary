from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt6.QtWidgets import QWidget, QFileDialog

from DrawingTool import PaintBrush, PaintSpray, Eraser


class Canvas(QWidget):

    def __init__(self):
        super().__init__()
        self.canvas_background = QPixmap()  # documentation: https://doc.qt.io/qt-6/qpixmap.html
        self.canvas_background.fill(Qt.GlobalColor.white)

        self.image = QPixmap("./icons/canvas.png")  # documentation: https://doc.qt.io/qt-6/qpixmap.html
        self.image.fill(Qt.GlobalColor.transparent)  # documentation: https://doc.qt.io/qt-6/qpixmap.html#fill

        self.tool_kit = {
            "brush": PaintBrush(self),
            "eraser": Eraser(self),
            "spray": PaintSpray(self)
        }

        self.current_tool = self.tool_kit["brush"]

        # Draw settings (default)
        self.drawing = False
        self.tool_size = 3
        self.tool_color = "#000000"  # documentation: https://doc.qt.io/qt-6/qt.html#GlobalColor-enum

        # Reference to last point recorded by mouse
        self.last_point = QPoint()  # documentation: https://doc.qt.io/qt-6/qpoint.html

    # Slots ========================================

    def change_current_tool(self, tool_name):
        print(tool_name)
        self.current_tool = self.tool_kit[tool_name]

    def change_tool_size(self, px_size):
        self.tool_size = px_size

    def change_tool_color(self, color):
        self.tool_color = color

    def clear(self):
        self.image.fill(Qt.GlobalColor.white)  # fill the image with white
        self.update()  # call the update method of the widget which calls the paintEvent of this class

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if file_path == "":  # if the file path is empty
            return  # do nothing and return
        self.image.save(file_path)  # save file image to the file path

    # Events =======================================
    def mousePressEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:  # if the pressed button is the left button
            self.drawing = True  # enter drawing mode
            self.current_tool.mouse_press(event)
            self.update()

    def mouseMoveEvent(self, event):

        if self.drawing:

            self.current_tool.mouse_drag(event)

            # call the update method of the widget which calls the paintEvent of this class
            self.update()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:  # if the released button is the left button
            self.drawing = False  # exit drawing mode

    def paintEvent(self, event):
        # you should only create and use the QPainter object in this method, it should be a local variable
        canvas_painter = QPainter(self)  # create a new QPainter object, docs: https://doc.qt.io/qt-6/qpainter.html
        canvas_painter.drawPixmap(QPoint(), self.canvas_background)
        canvas_painter.drawPixmap(QPoint(), self.image)  # draw image, https://doc.qt.io/qt-6/qpainter.html#drawImage-1

    def resizeEvent(self, event):
        self.image = self.image.scaled(self.width(), self.height())
