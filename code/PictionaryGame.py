"""
Student name: Arthur Carbonari Martins
Student number: 3028568

Extra features:

There are quite a few extra features in this application:

Eraser: A eraser tool that the user can utilize to delete drawings on the canvas.

Spray can: A painting tool the user can utilize to paint the canvas in a spray pattern.

Fill bucket (NOT WORKING): Unfortunately, there was not enough time to implement a fill function, but I left the icon in
the Controller Box to even the number of buttons in it.

Open file: Allows the user to select and open an image file to use as background for the canvas.

Insert image: Allows the user to insert an image into the canvas that can be interacted with as if it was painted by the
 user in the top layer of the canvas.

Redo and Undo Button: Allows the user to undo or redo the last actions performed on the canvas.

Color Selection Dialog: Allows the user to select a customizable color to paint with.

"""

import sys

from PyQt6.QtWidgets import QApplication

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
