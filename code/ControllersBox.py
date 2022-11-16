from PyQt6.QtWidgets import QFrame, QVBoxLayout, QWidget, QPushButton
from PyQt6.uic.properties import QtCore


class ControllersBox(QFrame):

    colors = [
        '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970', '#5ebb49',
        '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245', '#a15c3e', '#a42f3b',
        '#f45b7a', '#c24998', '#81588d', '#bcb0c2', '#ffffff',
    ]

    def __init__(self, game):
        super().__init__()
        layout = QVBoxLayout(self)
        color_controllers = QFrame()
        layout.addWidget(color_controllers)
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


class ColorButton(QPushButton):

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.setFixedSize(QtCore.QSize(24, 24))
        self.setStyleSheet("background-color: %s;" % color)
