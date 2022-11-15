"""
Student name: Arthur Carbonari Martins
Student number: 3028568
"""

import csv
import random
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QHBoxLayout, QLabel, \
    QVBoxLayout

from MyMenuBar import MyMenuBar
from InfoDock import InfoDock
from WelcomeDialog import WelcomeDialog
from Canvas import Canvas


class PictionaryGame(QMainWindow):
    """
    Painting Application class
    """

    def __init__(self):
        super().__init__()

        self.player_1 = ""
        self.player_2 = ""

        self.current_player = ""

        # set window title
        self.setWindowTitle("Phyctionary")

        # set the windows dimensions
        top = 400
        left = 400
        width = 800
        height = 600
        self.setGeometry(top, left, width, height)

        # set the icon
        self.setWindowIcon(QIcon("./icons/paint-brush.png"))

        # Create the canvas and set it as the central widget
        self.canvas = Canvas()

        main_layout = QHBoxLayout()
        central_widget = QWidget()
        central_widget.setObjectName("body")
        central_widget.setStyleSheet("""
            #body {
                background-image: url("./icons/background.png");
                border: 2px solid #fff;
            }
        """)
        t = QLabel("another one")

        main_layout.addWidget(t, 1)

        right_layout = QVBoxLayout()

        canvas_wrapper = QWidget()
        canvas_wrapper.setStyleSheet("""
            background-color: white;
            border-radius: 8px;
            border: 1px solid #000;
        """)

        canvas_wrapper_layout = QVBoxLayout()
        canvas_wrapper_layout.addWidget(self.canvas)
        canvas_wrapper_layout.setContentsMargins(3, 3, 3, 3)

        canvas_wrapper.setLayout(canvas_wrapper_layout)

        right_layout.addWidget(canvas_wrapper, 5)
        right_layout.setSpacing(20)

        input_box = QWidget()
        input_box.setStyleSheet("""
            background-color: white;
            border-radius: 8px;
            border: 1px solid #000;
        """)

        right_layout.addWidget(input_box, 2)

        main_layout.addLayout(right_layout, 2)

        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(40)

        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)
        # Create and set the Menu Bar
        # menu_bar = MyMenuBar(self)
        # self.setMenuBar(menu_bar)

        # Side Docks

        # Info Dock
        # self.info_dock = InfoDock(self)
        # self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.info_dock)

        self.word_list = []

    def set_players(self, player_one, player_two):
        self.player_1, self.player_2 = player_one, player_two
        self.info_dock.set_players(player_one, player_two)

    def next_turn(self):

        if self.current_player == self.player_1 or self.current_player == "":
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

        #   update current player in info dock

        self.get_word()

    # slots
    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if file_path == "":  # if the file path is empty
            return  # do nothing and return
        self.canvas.image.save(file_path)  # save file image to the file path

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


# This code will be executed if it is the main module but not if the module is imported
if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = PictionaryGame()
    game.start()
    app.exec()  # start the event loop running
