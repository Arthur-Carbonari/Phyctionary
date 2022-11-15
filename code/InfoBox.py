from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QFormLayout, QFrame


class InfoBox(QFrame):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.current = QLabel("Current Turn: ")

        self.team_name = [QLabel("Team 1: -"), QLabel("Team 2: -")]

        self.team_score = [QLabel("Score: 0"), QLabel("Score: 0")]

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

        info_layout.addWidget(self.current)

        info_layout.addSpacing(20)

        info_layout.addWidget(self.team_name[0])

        info_layout.addSpacing(20)

        info_layout.addWidget(self.team_name[1])

        info_layout.addStretch(1)
        info_layout.addWidget(QPushButton("Skip Turn"))

        info_layout.addSpacing(10)

    def set_team_names(self, team_1: str, team_2: str):
        self.team_name[0].setText("Team 1: " + team_1)

        self.team_name[1].setText("Team 2: " + team_2)

        self.change_current_turn(team_1)

    def change_current_turn(self, team: str):
        self.current.setText("Current Turn: " + team)
