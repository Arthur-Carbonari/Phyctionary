from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QPixmap, QColor
from PyQt6.QtWidgets import QWidget, QFileDialog

from DrawingTool import PaintBrush, PaintSpray, Eraser, PaintBucket


class Canvas(QWidget):

    def __init__(self):
        super().__init__()
        self.canvas_background = QPixmap()  # documentation: https://doc.qt.io/qt-6/qpixmap.html
        self.canvas_background.fill(QColor("#f5f5f5"))

        self.drawing = QPixmap("./icons/canvas.png")  # documentation: https://doc.qt.io/qt-6/qpixmap.html
        self.drawing.fill(Qt.GlobalColor.transparent)  # documentation: https://doc.qt.io/qt-6/qpixmap.html#fill
        self.drawing.toImage()

        self.tool_kit = {
            "brush": PaintBrush(self),
            "eraser": Eraser(self),
            "spray": PaintSpray(self),
            "bucket": PaintBucket(self)
        }

        self.undo_stack = []
        self.redo_stack = []

        self.current_tool = self.tool_kit["brush"]

        # Draw settings (default)
        self.is_drawing = False
        self.tool_size = 3
        self.tool_color = "#000000"  # documentation: https://doc.qt.io/qt-6/qt.html#GlobalColor-enum

        # Reference to last point recorded by mouse
        self.last_point = QPoint()  # documentation: https://doc.qt.io/qt-6/qpoint.html

    def reset(self):
        self.clear()
        self.undo_stack = []
        self.redo_stack = []

        self.current_tool = self.tool_kit["brush"]

    # Slots ========================================

    def change_current_tool(self, tool_name):
        print(tool_name)
        self.current_tool = self.tool_kit[tool_name]

    def change_tool_size(self, px_size):
        self.tool_size = px_size

    def change_tool_color(self, color):
        self.tool_color = color

    def clear(self):
        self.drawing.fill(Qt.GlobalColor.transparent)  # fill the drawing with transparent
        self.canvas_background.fill(Qt.GlobalColor.white)  # fill the drawing with transparent
        self.update()  # call the update method of the widget which calls the paintEvent of this class

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if file_path == "":  # if the file path is empty
            return  # do nothing and return
        self.drawing.save(file_path)  # save file drawing to the file path

    def undo(self):

        if len(self.undo_stack) == 0:
            return

        previous_state = self.undo_stack.pop()

        self.redo_stack.append(self.drawing)
        self.drawing = previous_state

        self.update()

    def redo(self):

        if len(self.redo_stack) == 0:
            return

        new_state = self.redo_stack.pop()

        self.undo_stack.append(self.drawing)
        self.drawing = new_state

        self.update()

    def open(self):

        img = self._read_image_from_file()

        if not img:
            return

        self.canvas_background = img
        self.canvas_background = self.canvas_background.scaled(self.width(), self.height())  # scale the drawing from file
        self.update()  # call the update method of the widget which calls the paintEvent of this class

    def insert_image(self):

        img = self._read_image_from_file()

        if not img:
            return

        self.drawing = img

        self.drawing = self.drawing.scaled(self.width(), self.height())  # scale the drawing from file
        self.update()  # call the update method of the widget which calls the paintEvent of this class

    # Events =======================================
    def mousePressEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:  # if the pressed button is the left button
            self.is_drawing = True  # enter is_drawing mode

            if len(self.redo_stack) > 0:
                self.redo_stack = []

            if len(self.undo_stack) > 9:
                self.undo_stack.pop(0)

            self.undo_stack.append(self.drawing.copy())

            self.current_tool.mouse_press(event)
            self.update()

    def mouseMoveEvent(self, event):

        if self.is_drawing:

            self.current_tool.mouse_drag(event)

            # call the update method of the widget which calls the paintEvent of this class
            self.update()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:  # if the released button is the left button
            self.is_drawing = False  # exit is_drawing mode

    def paintEvent(self, event):
        # you should only create and use the QPainter object in this method, it should be a local variable
        canvas_painter = QPainter(self)  # create a new QPainter object, docs: https://doc.qt.io/qt-6/qpainter.html
        canvas_painter.drawPixmap(QPoint(), self.canvas_background)
        canvas_painter.drawPixmap(QPoint(), self.drawing)  # draw drawing, https://doc.qt.io/qt-6/qpainter.html#drawImage-1

    def resizeEvent(self, event):
        self.drawing = self.drawing.scaled(self.width(), self.height())

    # helper methods

    def _read_image_from_file(self):

        pm = QPixmap()

        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                   "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if file_path == "":  # if not file is selected exit
            return None
        with open(file_path, 'rb') as f:  # open the file in binary mode for reading
            content = f.read()  # read the file
        pm.loadFromData(content)  # load the data into the file

        return pm
