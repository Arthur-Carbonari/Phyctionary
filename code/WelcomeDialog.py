from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton


class WelcomeDialog(QDialog):

    def __init__(self, game_window):
        super().__init__()

        self.game_window = game_window
        self.game_ready = False

        self.setWindowTitle("Phyctionary")
        self.setModal(True)

        self.player_1 = QLineEdit(self)
        self.player_2 = QLineEdit(self)

        self.easy = QRadioButton("Easy")
        self.hard = QRadioButton("Hard")

        self.init_ui()

    def init_ui(self):

        self.setFixedSize(250, 250)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Welcome, please enter your team`s name\nAnd select the desired game mode:"))

        layout.addStretch(1)

        layout_one = QFormLayout()
        layout_one.addRow(QLabel("Player 1: "), self.player_1)
        layout.addLayout(layout_one)

        layout.addStretch(1)

        layout_two = QFormLayout()
        layout_two.addRow(QLabel("Player 2: "), self.player_2)
        layout.addLayout(layout_two)

        layout.addStretch(1)

        layout.addWidget(self.easy)
        layout.addWidget(self.hard)

        layout.addStretch(1)

        button_box = QHBoxLayout()
        button_box.addStretch()
        start_button = QPushButton("Start Game")
        button_box.addWidget(start_button)
        button_box.addStretch()

        start_button.clicked.connect(self.start_game)

        layout.addLayout(button_box)
        self.setLayout(layout)

    def start_game(self):
        p1 = self.player_1.text()
        p2 = self.player_2.text()

        if not (p1 and p2):
            return

        if self.easy.isChecked():
            game_mode = self.easy.text()
        elif self.hard.isChecked():
            game_mode = self.hard.text()
        else:
            return

        self.game_window.set_team_names(p1, p2)
        self.game_window.get_list(game_mode)

        self.game_ready = True

        self.close()

        self.game_window.start_game()

    def closeEvent(self, e):
        if not self.game_ready:
            exit()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape:
            return
