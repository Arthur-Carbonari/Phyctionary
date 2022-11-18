"""
Student name: Arthur Carbonari Martins
Student number: 3028568
"""

import csv
import random

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from Canvas import Canvas
from GuessBox import GuessBox
from InfoBox import InfoBox
from ControllersBox import ControllersBox
from MyMenuBar import MyMenuBar


class GameWindow(QMainWindow):
    """
    Painting Application class
    """

    def __init__(self):
        super().__init__()

        self.team = [None, "", ""]
        self.score = [None, 0, 0]

        self.current_team = 0
        self.current_word = ""

        # set window title
        self.setWindowTitle("Phyctionary")  # Cause its python, get it?

        # set the windows minimum dimensions
        width = 1200
        height = 700
        self.setMinimumWidth(width)
        self.setMinimumHeight(height)

        # set the icon
        self.setWindowIcon(QIcon("./icons/paint-brush.png"))

        self.canvas = Canvas()

        self.info_box = InfoBox(self)

        self.controllers_box = ControllersBox(self)

        self.guess_box = GuessBox(self)

        self.setMenuBar(MyMenuBar(self))

        self._init_ui()

        self.word_list = []

    def _init_ui(self):

        # Sets up the central widget and adds it to the main window
        central_widget = QWidget()
        central_widget.setObjectName("container")  # Sets the object name for the stylesheet
        central_widget.setStyleSheet("""
            #container {
                background-image: url("./icons/background.png");
                border: 2px solid #fff;
            }
        """)

        self.setCentralWidget(central_widget)

        # Sets up the main layout for the window and adds it to the central widget
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(40)

        # Sets up the left layout and adds to the main layout
        left_layout = QVBoxLayout()
        left_layout.setSpacing(20)
        main_layout.addLayout(left_layout, 4)

        # Sets up the right layout and adds to the main layout
        right_layout = QHBoxLayout()
        right_layout.setSpacing(5)
        main_layout.addLayout(right_layout, 2)

        # Adds widgets to the left layout

        # ( A wrapper is needed for the canvas because we reimplement the paintEvent for the canvas class )
        canvas_wrapper = QWidget()  # Creates wrapper widget for the canvas...
        canvas_wrapper.setStyleSheet("""
                    background-color: white;
                    border-radius: 8px;
                    border: 1px solid #000;
                """)  # Sets the stylesheet for it...

        canvas_wrapper_layout = QVBoxLayout(canvas_wrapper)  # Create the layout for the wrapper...
        canvas_wrapper_layout.addWidget(self.canvas)  # Adds the canvas to the layout...
        canvas_wrapper_layout.setContentsMargins(3, 3, 3, 3)  # Set the margin for layout...

        left_layout.addWidget(canvas_wrapper, 5)  # Adds the wrapper to the right layout
        left_layout.addWidget(self.guess_box, 2)  # Adds the guess box to the right layout

        # Adds widgets to the right layout
        right_layout.addWidget(self.controllers_box, 1)
        right_layout.addWidget(self.info_box, 1)


    def set_team_names(self, team_1, team_2):
        self.team[1], self.team[2] = team_1, team_2
        self.info_box.set_team_names(team_1, team_2)

    def make_a_guess(self, guess: str):

        self.guess_box.output_field.append(self.team[self.current_team] + " :" + guess)

        if guess.casefold() == self.current_word.casefold():
            self.correct_guess()

        else:
            self.guess_box.output_field.append("Phyctionary: That is incorrect..")

    def correct_guess(self):
        self.guess_box.output_field.append("Phyctionary: That is correct!!!")
        self.guess_box.output_field.append("=================================")

        self.score[self.current_team] += 1
        self.info_box.set_team_score(self.current_team, self.score[self.current_team])
        self.next_turn()

    def next_turn(self):

        if self.current_team == 1:
            self.current_team = 2
        else:
            self.current_team = 1

        self.info_box.change_current_turn(self.team[self.current_team])

        self.guess_box.output_field.append("Phyctionary: It is your turn now team " + self.team[self.current_team])

        self.canvas.reset()

        self.current_word = self.get_word()
        self.info_box.set_current_word(self.current_word)

    # Get a random word from the list read from file
    def get_word(self):
        random_word = random.choice(self.word_list)
        print(random_word)
        return random_word

    # Read word list from file
    def get_list(self, mode):
        with open(mode + 'mode.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.word_list += row

    def start_game(self):
        self.current_team = 1
        self.current_word = self.get_word()
        self.info_box.set_current_word(self.current_word)
        self.guess_box.output_field.append("Phyctionary: Welcome, please click on 'show word' to see your word, and"
                                           " then click again to hide it and start drawing, carefully so that your "
                                           "partner dont see the word.\nGood Luck!")

    def skip_turn(self):
        self.guess_box.output_field.append("Team %s skipped their turn." % self.team[self.current_team])
        self.guess_box.output_field.append("=================================")

        self.next_turn()
