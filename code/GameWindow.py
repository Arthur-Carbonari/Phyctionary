"""
Student name: Arthur Carbonari Martins
Student number: 3028568
"""

import csv
import random
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QHBoxLayout, QVBoxLayout

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

        self.team_1 = ""
        self.team_2 = ""

        self.current_team = 1
        self.current_word = "test"

        # set window title
        self.setWindowTitle("Phyctionary")

        # set the windows minimum dimensions
        width = 1200
        height = 700
        self.setMinimumWidth(width)
        self.setMinimumHeight(height)

        # set the icon
        self.setWindowIcon(QIcon("./icons/paint-brush.png"))

        # Create the canvas and set it as the central widget
        self.info_box = InfoBox(self)

        self.controllers_box = ControllersBox(self)

        self.canvas = Canvas()

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
        left_layout = QHBoxLayout()
        left_layout.setSpacing(0)
        main_layout.addLayout(left_layout, 2)

        # Sets up the right layout and adds to the main layout
        right_layout = QVBoxLayout()
        right_layout.setSpacing(20)
        main_layout.addLayout(right_layout, 4)

        # Adds widgets to the left layout
        left_layout.addWidget(self.info_box, 1)  # Dummy widget
        left_layout.addWidget(self.controllers_box, 1)  # Dummy widget

        # Adds widgets to the right layout

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

        right_layout.addWidget(canvas_wrapper, 5)  # Adds the wrapper to the right layout
        right_layout.addWidget(self.guess_box, 2)  # Adds the guess box to the right layout

    def set_team_names(self, team_1, team_2):
        self.team_1, self.team_2 = team_1, team_2
        self.info_box.set_team_names(team_1, team_2)

    def make_a_guess(self, guess: str):
        if guess.casefold() == self.current_word.casefold():
            self.guess_box.output_field.append(self.current_word + " : That is right!")
            # TODO: increment score for current player
            # TODO: start next turn
        else:
            self.guess_box.output_field.append(guess + " : That is incorrect..")

    def next_turn(self):

        if self.current_team == self.team_1 or self.current_team == "":
            self.current_team = self.team_2
        else:
            self.current_team = self.team_1

        #   update current player in info dock

        self.current_word = self.get_word()

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

    def start(self):
        # WelcomeDialog(self)
        self.show()

    # def open(self):
    #     """
    #     This is an additional function which is not part of the tutorial. It will allow you to:
    #      - open a file dialog box,
    #      - filter the list of files according to file extension
    #      - set the QImage of your application (self.image) to a scaled version of the file
    #      - update the widget
    #     """
    #
    #     file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
    #                                                "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
    #     if file_path == "":  # if not file is selected exit
    #         return
    #     with open(file_path, 'rb') as f:  # open the file in binary mode for reading
    #         content = f.read()  # read the file
    #     self.image.loadFromData(content)  # load the data into the file
    #     width = self.width()  # get the width of the current QImage in your application
    #     height = self.height()  # get the height of the current QImage in your application
    #     self.image = self.image.scaled(width, height)  # scale the image from file and put it in your QImage
    #     self.update()  # call the update method of the widget which calls the paintEvent of this class
