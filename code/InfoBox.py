from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QFormLayout, QFrame


class InfoBox(QFrame):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.current = QLabel("-")

        self.team_name = [QLabel("-"), QLabel("-")]

        self.team_score = [QLabel("-"), QLabel("-")]

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
        form_layout.addRow(QLabel("Player 1:"), self.team_name[0])
        form_layout.addRow(QLabel("Score:"), self.team_score[0])
        info_layout.addLayout(form_layout)

        info_layout.addSpacing(20)

        form_layout = QFormLayout()
        form_layout.addRow(QLabel("Player 2:"), self.team_name[1])
        form_layout.addRow(QLabel("Score:"), self.team_score[1])
        info_layout.addLayout(form_layout)

        info_layout.addStretch(1)
        info_layout.addWidget(QPushButton("Skip Turn"))

        info_layout.addSpacing(10)

    def set_team_names(self, team_1, team_2):
        self.team_name[0].setText(team_1)

        self.team_name[1].setText(team_2)
