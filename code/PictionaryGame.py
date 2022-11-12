"""
Student name: Arthur Carbonari Martins
Student number: 3028568
"""

import csv
import random
import sys

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QIcon, QPainter, QPen, QAction, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QDockWidget, QPushButton, QVBoxLayout, \
    QLabel

from MyMenuBar import MyMenuBar
from InfoDock import InfoDock
from WelcomeDialog import WelcomeDialog


class PictionaryGame(QMainWindow):
    """
    Painting Application class
    """

    def __init__(self):
        super().__init__()

        self.player_1 = None
        self.player_2 = None

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

        # image settings (default)
        self.image = QPixmap("./icons/canvas.png")  # documentation: https://doc.qt.io/qt-6/qpixmap.html
        self.image.fill(Qt.GlobalColor.white)  # documentation: https://doc.qt.io/qt-6/qpixmap.html#fill
        main_widget = QWidget()
        main_widget.setMaximumWidth(300)

        # Draw settings (default)
        self.drawing = False
        self.brushSize = 3
        self.brushColor = Qt.GlobalColor.black  # documentation: https://doc.qt.io/qt-6/qt.html#GlobalColor-enum

        # Reference to last point recorded by mouse
        self.lastPoint = QPoint()  # documentation: https://doc.qt.io/qt-6/qpoint.html

        # Create and set the Menu Bar
        menu_bar = MyMenuBar(self)
        self.setMenuBar(menu_bar)

        # Side Docks

        # Info Dock
        self.info_dock = InfoDock(self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.info_dock)

        self.word_list = []

    def set_players(self, player_one, player_two):
        self.player_1, self.player_2 = player_one, player_two
        self.info_dock.set_players(player_one, player_two)

    # EVENT HANDLERS ============================================================

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:  # if the pressed button is the left button
            self.drawing = True  # enter drawing mode
            self.lastPoint = event.pos()  # save the location of the mouse press as the lastPoint
            print(self.lastPoint)  # print the lastPoint for debugging purposes

    def mouseMoveEvent(self, event):
        if self.drawing:
            painter = QPainter(self.image)  # object which allows drawing to take place on an image

            # allows the selection of brush colour, brish size, line type, cap type, join type.
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap,
                                Qt.PenJoinStyle.RoundJoin))

            # draw a line from the point of the original press to the point to where the mouse was dragged to
            painter.drawLine(self.lastPoint, event.pos())

            # set the last point to refer to the point we have just moved to, this helps when drawing the next segment
            self.lastPoint = event.pos()

            # call the update method of the widget which calls the paintEvent of this class
            self.update()

    def mouseReleaseEvent(self, event):
        # when the mouse is released

        if event.button() == Qt.MouseButton.LeftButton:  # if the released button is the left button
            self.drawing = False  # exit drawing mode

    def paintEvent(self, event):
        # you should only create and use the QPainter object in this method, it should be a local variable
        canvas_painter = QPainter(self)  # create a new QPainter object, docs: https://doc.qt.io/qt-6/qpainter.html
        canvas_painter.drawPixmap(QPoint(), self.image)  # draw image, https://doc.qt.io/qt-6/qpainter.html#drawImage-1

    def resizeEvent(self, event):
        self.image = self.image.scaled(self.width(), self.height())

    # slots
    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if file_path == "":  # if the file path is empty
            return  # do nothing and return
        self.image.save(file_path)  # save file image to the file path

    def clear(self):
        self.image.fill(Qt.GlobalColor.white)  # fill the image with white
        self.update()  # call the update method of the widget which calls the paintEvent of this class

    def change_brush_size(self, px_size):
        self.brushSize = px_size

    def change_brush_color(self, color):
        self.brushColor = Qt.GlobalColor[color]

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

    def open(self):
        """
        This is an additional function which is not part of the tutorial. It will allow you to:
         - open a file dialog box,
         - filter the list of files according to file extension
         - set the QImage of your application (self.image) to a scaled version of the file
         - update the widget
        """

        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                   "PNG(*.png);;JPG(*.jpg *.jpeg);;All Files (*.*)")
        if file_path == "":  # if not file is selected exit
            return
        with open(file_path, 'rb') as f:  # open the file in binary mode for reading
            content = f.read()  # read the file
        self.image.loadFromData(content)  # load the data into the file
        width = self.width()  # get the width of the current QImage in your application
        height = self.height()  # get the height of the current QImage in your application
        self.image = self.image.scaled(width, height)  # scale the image from file and put it in your QImage
        self.update()  # call the update method of the widget which calls the paintEvent of this class

    def start(self):
        WelcomeDialog(self)
        self.show()


# This code will be executed if it is the main module but not if the module is imported
if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = PictionaryGame()
    game.start()
    app.exec()  # start the event loop running
