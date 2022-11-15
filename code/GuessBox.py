from PyQt6.QtWidgets import QWidget, QStyleOption, QStyle, QFrame, QLineEdit, QVBoxLayout, QTextEdit


class GuessBox(QFrame):

    def __init__(self):
        super().__init__()

        self.output_field = QTextEdit()
        self.output_field.setReadOnly(True)

        self.input_field = QLineEdit(self)

        self.setStyleSheet("""
                    background-color: white;
                    border-radius: 8px;
                    border: 1px solid #000;
        """)

    # def paintEvent(self, e):
    #     opt = QStyleOption()
    #     opt.initFrom(self)
    #     painter = QPainter(self)
    #     self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, opt, painter, self)

