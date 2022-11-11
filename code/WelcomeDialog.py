from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFormLayout, QLineEdit


class WelcomeDialog(QDialog):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.selected = False

        self.setWindowTitle("Phyctionary")
        self.setModal(True)

        self.player_one = QLineEdit(self)
        self.player_two = QLineEdit(self)

        self.init_ui()

        self.exec()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Welcome to our game\nPlease select your desired game mode:"))

        layout_one = QFormLayout()
        layout_one.addRow(QLabel("Player 1: "), self.player_one)
        layout.addLayout(layout_one)

        layout_two = QFormLayout()
        layout_two.addRow(QLabel("Player 2: "), self.player_two)
        layout.addLayout(layout_two)

        button_box = QHBoxLayout()

        easy_button = QPushButton("Easy")
        button_box.addWidget(easy_button)

        hard_button = QPushButton("Hard")
        button_box.addWidget(hard_button)

        # Connect signals to slots
        easy_button.clicked.connect(lambda: self.set_choice("easy"))
        hard_button.clicked.connect(lambda: self.set_choice("hard"))

        layout.addLayout(button_box)
        self.setLayout(layout)

    def set_choice(self, choice):
        self.parent.get_list(choice)
        self.selected = True
        self.close()

    def closeEvent(self, e):
        if not self.selected:
            exit()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape:
            return

