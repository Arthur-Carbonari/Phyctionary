from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QFormLayout, QFrame


class InfoBox(QFrame):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.current = QLabel("Current Turn: ")

        self.team_name = [None, QLabel("Team 1: -"), QLabel("Team 2: -")]

        self.team_score = [None, QLabel("Score: 0"), QLabel("Score: 0")]

        self.setObjectName("InfoBox")
        self.setStyleSheet("""
            #InfoBox {
                background-color: #f5f5f5;
                border-radius: 8px;
                border: 1px solid #000;
            }
        """)

        self._init_ui()

    def _init_ui(self):

        # Widget inside the Dock
        info_layout = QVBoxLayout()
        self.setLayout(info_layout)

        info_layout.addStretch(1)

        info_layout.addWidget(self.current)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setLineWidth(2)

        info_layout.addStretch(1)
        info_layout.addWidget(separator)
        info_layout.addStretch(1)

        info_layout.addWidget(self.team_name[1])
        info_layout.addSpacing(10)
        info_layout.addWidget(self.team_score[1])

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setLineWidth(1)

        info_layout.addStretch(1)
        info_layout.addWidget(separator)
        info_layout.addStretch(1)


        info_layout.addWidget(self.team_name[2])
        info_layout.addSpacing(10)
        info_layout.addWidget(self.team_score[2])

        info_layout.addStretch(5)
        info_layout.addWidget(QPushButton("Skip Turn"))

        info_layout.addSpacing(10)
        
        # Font size

        font_size = 18
        font = 'Times'

        self.current.setFont(QFont(font, font_size))

        self.team_name[1].setFont(QFont(font, font_size))
        self.team_name[2].setFont(QFont(font, font_size))

        self.team_score[1].setFont(QFont(font, font_size))
        self.team_score[2].setFont(QFont(font, font_size))

    def set_team_names(self, team_1: str, team_2: str):
        self.team_name[1].setText("Team 1: " + team_1)

        self.team_name[2].setText("Team 2: " + team_2)

        self.current.setText("Current Turn: " + team_1)

    def change_current_turn(self, team: str):
        self.current.setText("Current Turn: " + team)

    def set_team_score(self, team: int, new_score: int):
        self.team_score[team].setText("Score: %s" % new_score)
