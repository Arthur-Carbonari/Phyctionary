from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout


class WelcomeDialog(QDialog):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.selected = False

        self.setWindowTitle("Dialog")
        self.setModal(True)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Welcome to our game\nPlease select your desired game mode:"))

        button_box = QHBoxLayout()

        easy_button = QPushButton("Easy")
        button_box.addWidget(easy_button)
        easy_button.clicked.connect(lambda: self.set_choice("easy"))

        hard_button = QPushButton("Hard")
        button_box.addWidget(hard_button)
        hard_button.clicked.connect(lambda: self.set_choice("hard"))

        layout.addLayout(button_box)
        self.setLayout(layout)

        self.exec()

    def set_choice(self, choice):
        self.parent.get_list(choice)
        self.selected = True
        self.close()

    def closeEvent(self, e):
        if not self.selected:
            exit()
