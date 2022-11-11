from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMenuBar


class MyMenuBar(QMenuBar):

    def __init__(self, parent):
        super().__init__()

        self.setNativeMenuBar(False)

        # Add menus to menu bar
        file_menu = self.addMenu(" File")  # Add file menu to the menu bar, "File" is reserved in Mac
        brush_size_menu = self.addMenu(" Brush Size")  # Add the "Brush Size" menu to the menu bar
        brush_color_menu = self.addMenu(" Brush Colour")  # Add the "Brush Colour" menu to the menu bar

        # Save Action
        save_action = QAction(QIcon("./icons/save.png"), "Save", parent)  # Create a save action with an icon
        save_action.setShortcut("Ctrl+S")  # Connect this save action to a keyboard shortcut
        file_menu.addAction(save_action)  # Add the save action to the file menu
        save_action.triggered.connect(parent.save)  # Connect action to respective slot

        # Clear Action
        clear_action = QAction(QIcon("./icons/clear.png"), "Clear", parent)  # Create a clear action with icon
        clear_action.setShortcut("Ctrl+C")  # Connect this clear action to a keyboard shortcut
        file_menu.addAction(clear_action)  # Add this action to the file menu
        clear_action.triggered.connect(parent.clear)  # Connect action to respective slot

        # Change Brush Thickness
        three_px_action = QAction(QIcon("./icons/three_px.png"), "3px", parent)
        three_px_action.setShortcut("Ctrl+3")
        brush_size_menu.addAction(three_px_action)  # connect the action to the function below
        three_px_action.triggered.connect(lambda: parent.change_brush_size(3))

        five_px_action = QAction(QIcon("./icons/five_px.png"), "5px", parent)
        five_px_action.setShortcut("Ctrl+5")
        brush_size_menu.addAction(five_px_action)
        five_px_action.triggered.connect(lambda: parent.change_brush_size(5))

        seven_px_action = QAction(QIcon("./icons/seven_px.png"), "7px", parent)
        seven_px_action.setShortcut("Ctrl+7")
        brush_size_menu.addAction(seven_px_action)
        seven_px_action.triggered.connect(lambda: parent.change_brush_size(7))

        nine_px_action = QAction(QIcon("./icons/nine_px.png"), "9px", parent)
        nine_px_action.setShortcut("Ctrl+9")
        brush_size_menu.addAction(nine_px_action)
        nine_px_action.triggered.connect(lambda: parent.change_brush_size(9))

        # Change Brush Colors
        black_action = QAction(QIcon("./icons/black.png"), "Black", parent)
        black_action.setShortcut("Ctrl+B")
        brush_color_menu.addAction(black_action)
        black_action.triggered.connect(lambda: parent.change_brush_color("black"))

        red_action = QAction(QIcon("./icons/red.png"), "Red", parent)
        red_action.setShortcut("Ctrl+R")
        brush_color_menu.addAction(red_action)
        red_action.triggered.connect(lambda: parent.change_brush_color("red"))

        green_action = QAction(QIcon("./icons/green.png"), "Green", parent)
        green_action.setShortcut("Ctrl+G")
        brush_color_menu.addAction(green_action)
        green_action.triggered.connect(lambda: parent.change_brush_color("green"))

        yellow_action = QAction(QIcon("./icons/yellow.png"), "Yellow", parent)
        yellow_action.setShortcut("Ctrl+Y")
        brush_color_menu.addAction(yellow_action)
        yellow_action.triggered.connect(lambda: parent.change_brush_color("yellow"))
