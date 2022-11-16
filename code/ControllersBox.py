from PyQt6.QtWidgets import QFrame, QVBoxLayout, QWidget


class ControllersBox(QFrame):

    def __init__(self, game):
        super().__init__()
        layout = QVBoxLayout(self)
        wid = QWidget()
        layout.addWidget(wid, 1)
        self._init_ui()

    def _init_ui(self):
        self.setObjectName("ControllersBox")
        self.setStyleSheet("""
            #ControllersBox {
                background-color: #142d4c;
                opacity: 0,5;
                border-radius: 8px;
                border: 1px solid #000;
            }
        """)
