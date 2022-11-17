from IPython.external.qt_for_kernel import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QIcon, QPixmap
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QWidget, QPushButton, QGridLayout, QGroupBox, QHBoxLayout, \
    QColorDialog, QSlider, QToolButton


class ControllersBox(QFrame):
    colors = [
        '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
        '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
        '#f45b7a', '#81588d', '#bcb0c2', '#ffffff',
    ]

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.current_color = "#000000"

        layout = QVBoxLayout(self)
        layout.addStretch(1)

        self.tool_buttons_grid = QGridLayout()
        self.populate_tool_buttons_grid()
        button = QToolButton()
        button.setIconSize(QtCore.QSize(36, 36))
        button.setIcon(QIcon("./icons/paint-brush.png"))

        layout.addLayout(self.tool_buttons_grid)

        self.color_pallete = QGridLayout()
        self.populate_color_pallete()

        layout.addLayout(self.color_pallete)
        layout.addSpacing(10)

        self.current_color_button = QPushButton()
        self.current_color_button.setFixedSize(QtCore.QSize(36, 36))
        self.current_color_button.setStyleSheet("background-color: #000;")

        self.more_color_button = QPushButton()
        self.more_color_button.setFixedSize(QtCore.QSize(36, 36))
        self.more_color_button.setStyleSheet("background-color: #123;")
        self.more_color_button.clicked.connect(self.set_color_from_dialog)

        row_wrapper = QHBoxLayout()
        row_wrapper.addStretch(1)
        row_wrapper.addWidget(self.current_color_button)
        row_wrapper.addWidget(self.more_color_button)
        row_wrapper.addStretch(1)
        layout.addLayout(row_wrapper)

        layout.addSpacing(20)

        size_slider = QSlider()
        size_slider.setMinimum(1)
        size_slider.setMaximum(10)
        size_slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        size_slider.setTickInterval(1)

        slider_wrapper = QHBoxLayout()
        slider_wrapper.addStretch(1)
        slider_wrapper.addWidget(size_slider)
        slider_wrapper.addStretch(1)
        layout.addLayout(slider_wrapper)

        layout.addStretch(1)
        self._init_ui()

    def _init_ui(self):
        self.setObjectName("ControllersBox")
        self.setStyleSheet("""
            #ControllersBox {
                background-color: #f5f5f5;
                border-radius: 8px;
                border: 1px solid #000;
            }
            
            QToolButton {
                background: rgba(255, 255, 255, 0);
                border: none;
            }
        """)

    def test(self, parameter):
        print(parameter)

    def set_color_from_dialog(self):
        color = QColorDialog.getColor(QColor(self.current_color)).name()

        if color == self.current_color:
            return

        self.set_current_color(color)

    def set_current_color(self, color):
        self.current_color = color
        self.current_color_button.setStyleSheet("background-color: %s;" % color)
        self.game.canvas.change_tool_color(color)

    def change_current_tool(self, tool_name):
        self.game.canvas.change_current_tool(tool_name)

    def populate_tool_buttons_grid(self):
        tools = [ToolButton("./icons/paint-brush.png", self.change_current_tool, "brush"),
                 ToolButton("./icons/paint-brush.png", self.change_current_tool, "eraser"),
                 ToolButton("./icons/paint-brush.png", self.change_current_tool, "spray"),
                 ToolButton("./icons/paint-brush.png", self.change_current_tool, "bucket"),
                 ToolButton("./icons/save.png", self.test),
                 ToolButton("./icons/paint-brush.png", self.test),  # open
                 ToolButton("./icons/clear.png", self.test),
                 ToolButton("./icons/paint-brush.png", self.test),  # undo
                 ToolButton("./icons/paint-brush.png", self.test)]  # do

        row, clm = 0, 0

        for tool in tools:
            self.tool_buttons_grid.addWidget(tool, row, clm)

            if clm == 1:
                clm = 0
                row += 1
            else:
                clm = 1

    def populate_color_pallete(self):

        col, row = 0, 0

        for color in ControllersBox.colors:
            self.color_pallete.addWidget(ColorButton(color, self), col, row)

            if row != 2:
                row += 1
            else:
                row = 0
                col += 1


class ToolButton(QToolButton):

    def __init__(self, icon_path, slot, parameter=None):
        super().__init__()
        self.setIconSize(QtCore.QSize(36, 36))
        self.setIcon(QIcon(icon_path))

        if parameter:
            self.clicked.connect(lambda: slot(parameter))
        else:
            self.clicked.connect(slot)


class ColorButton(QPushButton):

    def __init__(self, color, controller_box):
        super().__init__()
        self.color = color
        self.setFixedSize(QtCore.QSize(24, 24))
        self.setStyleSheet("background-color: %s;" % color)
        self.clicked.connect(lambda: controller_box.set_current_color(color))
