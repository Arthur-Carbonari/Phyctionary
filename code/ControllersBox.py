from IPython.external.qt_for_kernel import QtCore
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QWidget, QPushButton, QGridLayout, QGroupBox


class ControllersBox(QFrame):
    colors = [
        '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
        '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
        '#f45b7a', '#81588d', '#bcb0c2', '#ffffff',
    ]

    def __init__(self, game):
        super().__init__()
        layout = QVBoxLayout(self)
        color_pallete = self.get_color_pallete()
        layout.addWidget(color_pallete)
        self._init_ui()

    def _init_ui(self):
        self.setObjectName("ControllersBox")
        self.setStyleSheet("""
            #ControllersBox {
                background-color: #142d4c;
                border-radius: 8px;
                border: 1px solid #000;
            }
        """)

    def get_color_pallete(self):
        color_pallete = QGroupBox()
        layout = QGridLayout()
        color_pallete.setLayout(layout)

        col, row = 0, 0

        for color in ControllersBox.colors:
            layout.addWidget(ColorButton(color, self), col, row)

            if row != 2:
                row += 1
            else:
                row = 0
                col += 1

        return color_pallete

    def change_selected_color(self, color):
        print(color)


class ColorButton(QPushButton):

    def __init__(self, color, controller_box):
        super().__init__()
        self.color = color
        self.setFixedSize(QtCore.QSize(24, 24))
        self.setStyleSheet("background-color: %s;" % color)
        self.clicked.connect(lambda: controller_box.change_selected_color(color))
