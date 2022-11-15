from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle, QFrame, QLineEdit, QVBoxLayout, QTextEdit


class GuessBox(QFrame):

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)

        self.input_field = QLineEdit(self)

        self.setStyleSheet("""
                    background-color: white;
                    border-radius: 8px;
                    border: 1px solid #000;
        """)

        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.output_field, 3)
        layout.addWidget(self.input_field, 1)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Return or e.key() == Qt.Key.Key_Enter:
            guess = self.input_field.text().strip()
            self.input_field.setText("")
            if guess:
                self.game.make_a_guess(guess)

    # def paintEvent(self, e):
    #     opt = QStyleOption()
    #     opt.initFrom(self)
    #     painter = QPainter(self)
    #     self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

