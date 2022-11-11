from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton


class WelcomeDialog(QDialog):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.game_ready = False

        self.setWindowTitle("Phyctionary")
        self.setModal(True)

        self.player_one = QLineEdit(self)
        self.player_two = QLineEdit(self)

        self.easy = QRadioButton("Easy")
        self.hard = QRadioButton("Hard")

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

        layout.addWidget(self.easy)
        layout.addWidget(self.hard)

        button_box = QHBoxLayout()
        button_box.addStretch()
        start_button = QPushButton("Start")
        button_box.addWidget(start_button)
        button_box.addStretch()

        start_button.click.connect(self.start_game)

        layout.addLayout(button_box)
        self.setLayout(layout)

    def set_choice(self, choice):
        self.parent.get_list(choice)
        self.selected = True
        self.close()

    def closeEvent(self, e):
        if not self.game_ready:
            exit()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape:
            return
