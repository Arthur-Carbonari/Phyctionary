"""
Student name: Arthur Carbonari Martins
Student number: 3028568
"""

import csv
import random
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from WelcomeDialog import WelcomeDialog

from GameWindow import GameWindow


class PictionaryGame:

    def __init__(self):
        self.game_window = GameWindow()
        self.welcome_dialog = WelcomeDialog(self.game_window)

    def start(self):
        self.game_window.show()
        self.welcome_dialog.exec()


# This code will be executed if it is the main module but not if the module is imported
if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = PictionaryGame()
    game.start()
    app.exec()  # start the event loop running
