from PyQt6.QtGui import QAction, QIcon


class MyMenuBar:

    def __init__(self, parent):
        # Set up menus
        main_menu = parent.menuBar()  # Create a menu bar
        main_menu.setNativeMenuBar(False)
        file_menu = main_menu.addMenu(" File")  # Add file menu to the menu bar, "File" is reserved in Mac
        brush_size_menu = main_menu.addMenu(" Brush Size")  # add the "Brush Size" menu to the menu bar
        brush_color_menu = main_menu.addMenu(" Brush Colour")  # add the "Brush Colour" menu to the menu bar

        # Save menu item
        # create a save action with a png as an icon, docs: https://doc.qt.io/qt-6/qaction.html
        save_action = QAction(QIcon("./icons/save.png"), "Save", parent)
        # connect this save action to a keyboard shortcut, docs: https://doc.qt.io/qt-6/qaction.html#shortcut-prop
        save_action.setShortcut("Ctrl+S")
        # add the save action to the file menu, documentation: https://doc.qt.io/qt-6/qwidget.html#addAction
        file_menu.addAction(save_action)
        # when the menu option or shortcut is used the save slot is triggered
        # docs: https://doc.qt.io/qt-6/qaction.html#triggered
        save_action.triggered.connect(parent.save)

        # clear
        clear_action = QAction(QIcon("./icons/clear.png"), "Clear", parent)  # create a clear action with icon
        clear_action.setShortcut("Ctrl+C")  # connect this clear action to a keyboard shortcut
        file_menu.addAction(clear_action)  # add this action to the file menu
        # when the menu option is selected or the shortcut is used the clear slot is triggered
        clear_action.triggered.connect(parent.clear)

        # brush thickness
        three_px_action = QAction(QIcon("./icons/three_px.png"), "3px", parent)
        three_px_action.setShortcut("Ctrl+3")
        brush_size_menu.addAction(three_px_action)  # connect the action to the function below
        three_px_action.triggered.connect(parent.three_px)

        five_px_action = QAction(QIcon("./icons/five_px.png"), "5px", parent)
        five_px_action.setShortcut("Ctrl+5")
        brush_size_menu.addAction(five_px_action)
        five_px_action.triggered.connect(parent.five_px)

        seven_px_action = QAction(QIcon("./icons/seven_px.png"), "7px", parent)
        seven_px_action.setShortcut("Ctrl+7")
        brush_size_menu.addAction(seven_px_action)
        seven_px_action.triggered.connect(parent.seven_px)

        nine_px_action = QAction(QIcon("./icons/nine_px.png"), "9px", parent)
        nine_px_action.setShortcut("Ctrl+9")
        brush_size_menu.addAction(nine_px_action)
        nine_px_action.triggered.connect(parent.nine_px)

        # brush colors
        black_action = QAction(QIcon("./icons/black.png"), "Black", parent)
        black_action.setShortcut("Ctrl+B")
        brush_color_menu.addAction(black_action)
        black_action.triggered.connect(parent.black)

        red_action = QAction(QIcon("./icons/red.png"), "Red", parent)
        red_action.setShortcut("Ctrl+R")
        brush_color_menu.addAction(red_action)
        red_action.triggered.connect(parent.red)

        green_action = QAction(QIcon("./icons/green.png"), "Green", parent)
        green_action.setShortcut("Ctrl+G")
        brush_color_menu.addAction(green_action)
        green_action.triggered.connect(parent.green)

        yellow_action = QAction(QIcon("./icons/yellow.png"), "Yellow", parent)
        yellow_action.setShortcut("Ctrl+Y")
        brush_color_menu.addAction(yellow_action)
        yellow_action.triggered.connect(parent.yellow)
