from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFormLayout, QFrame


class InfoBox(QFrame):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.current = QLabel("-")

        self.player_1 = QLabel("-")
        self.player_2 = QLabel("-")

        self.score_p1 = QLabel("0")
        self.score_p2 = QLabel("0")

        self.setObjectName("InfoBox")
        self.setStyleSheet("""
            #InfoBox {
                background-color: gray;
                border-radius: 8px;
                border: 1px solid #000;
            }
                """)

        self._init_ui()

    def _init_ui(self):

        # Widget inside the Dock
        info_layout = QVBoxLayout()
        self.setLayout(info_layout)

        info_layout.addSpacing(10)

        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Current Turn:"), self.current)
        info_layout.addLayout(form_layout)

        info_layout.addSpacing(20)

        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Player 1:"), self.player_1)
        form_layout.addRow(QLabel("Score:"), self.score_p1)
        info_layout.addLayout(form_layout)

        info_layout.addSpacing(20)

        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Player 2:"), self.player_2)
        form_layout.addRow(QLabel("Score:"), self.score_p2)
        info_layout.addLayout(form_layout)

        info_layout.addStretch(1)
        info_layout.addWidget(QPushButton("Skip Turn"))

        info_layout.addSpacing(10)

    def set_players(self, p1, p2):
        self.player_1.setText(p1)

        self.player_2.setText(p2)
