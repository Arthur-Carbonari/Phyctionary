from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDockWidget, QWidget, QVBoxLayout, QLabel, QPushButton


class InfoDock(QDockWidget):

    def __init__(self, parent):
        super().__init__()

        # Widget inside the Dock
        info_widget = QWidget()
        info_layout = QVBoxLayout()
        info_widget.setLayout(info_layout)
        info_widget.setMaximumSize(100, parent.height())
        # Add controls to custom widget
        info_layout.addWidget(QLabel("Current Turn: -"))
        info_layout.addSpacing(20)
        info_layout.addWidget(QLabel("Scores:"))
        info_layout.addWidget(QLabel("Player 1: -"))
        info_layout.addWidget(QLabel("Player 2: -"))
        info_layout.addStretch(1)
        info_layout.addWidget(QPushButton("Button"))

        # Setting colour of dock to gray
        info_widget.setAutoFillBackground(True)
        p = info_widget.palette()
        p.setColor(info_widget.backgroundRole(), Qt.GlobalColor.gray)
        info_widget.setPalette(p)

        # Set widget for dock
        self.setWidget(info_widget)
