from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDockWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QFormLayout, QSpacerItem


class InfoDock(QDockWidget):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.current = QLabel("-")

        self.player_1 = QLabel("-")
        self.player_2 = QLabel("-")

        self.score_p1 = QLabel("0")
        self.score_p2 = QLabel("0")

        self.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.setTitleBarWidget(QWidget())

        self._init_ui()

    def _init_ui(self):

        # Widget inside the Dock
        info_widget = QWidget()
        info_layout = QVBoxLayout()
        info_widget.setLayout(info_layout)
        info_widget.setMaximumWidth(int(self.parent.height() * 0.2))

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

        # Setting colour of dock to gray
        info_widget.setAutoFillBackground(True)
        p = info_widget.palette()
        p.setColor(info_widget.backgroundRole(), Qt.GlobalColor.gray)
        info_widget.setPalette(p)

        # Set widget for dock
        self.setWidget(info_widget)

    def set_players(self, p1, p2):
        self.player_1.setText(p1)

        self.player_2.setText(p2)
