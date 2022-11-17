from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMenuBar


class MyMenuBar(QMenuBar):

    def __init__(self, parent):
        super().__init__()

        self.setNativeMenuBar(False)

        # Add menus to menu bar
        file_menu = self.addMenu(" File")  # Add file menu to the menu bar, "File" is reserved in Mac
        tool_size_menu = self.addMenu(" Tool Size")  # Add the "Brush Size" menu to the menu bar
        tool_color_menu = self.addMenu(" Tool Colour")  # Add the "Brush Colour" menu to the menu bar

        # Save Action
        save_action = QAction(QIcon("./icons/save.png"), "Save", parent)  # Create a save action with an icon
        save_action.setShortcut("Ctrl+S")  # Connect this save action to a keyboard shortcut
        file_menu.addAction(save_action)  # Add the save action to the file menu
        save_action.triggered.connect(parent.canvas.save)  # Connect action to respective slot

        # Clear Action
        clear_action = QAction(QIcon("./icons/clear.png"), "Clear", parent)  # Create a clear action with icon
        clear_action.setShortcut("Ctrl+C")  # Connect this clear action to a keyboard shortcut
        file_menu.addAction(clear_action)  # Add this action to the file menu
        clear_action.triggered.connect(parent.canvas.clear)  # Connect action to respective slot

        # Undo action
        undo_action = QAction(QIcon("./icons/undo.png"), "Undo", parent)  # Create a clear action with icon
        undo_action.setShortcut("Ctrl+Z")  # Connect this clear action to a keyboard shortcut
        file_menu.addAction(undo_action)  # Add this action to the file menu
        undo_action.triggered.connect(parent.canvas.undo)  # Connect action to respective slot
        
        # Redo action
        redo_action = QAction(QIcon("./icons/redo.png"), "Redo", parent)  # Create a clear action with icon
        redo_action.setShortcut("Ctrl+Y")  # Connect this clear action to a keyboard shortcut
        file_menu.addAction(redo_action)  # Add this action to the file menu
        redo_action.triggered.connect(parent.canvas.redo)  # Connect action to respective slot

        # Change Brush Thickness
        increase_tool_size = QAction(QIcon(), "Increase brush size", parent)
        increase_tool_size.setShortcut("Ctrl++")
        tool_size_menu.addAction(increase_tool_size)  # connect the action to the function below
        increase_tool_size.triggered.connect(parent.controllers_box.increase_tool_size)

        # Change Brush Thickness
        decrease_tool_size = QAction(QIcon("./icons/three_px.png"), "Decrease brush size", parent)
        decrease_tool_size.setShortcut("Ctrl+-")
        tool_size_menu.addAction(decrease_tool_size)  # connect the action to the function below
        decrease_tool_size.triggered.connect(parent.controllers_box.decrease_tool_size)

        # Change Brush Colors
        black_action = QAction(QIcon("./icons/black.png"), "Black", parent)
        black_action.setShortcut("Ctrl+B")
        tool_color_menu.addAction(black_action)
        black_action.triggered.connect(lambda: parent.controllers_box.change_current_color("#000000"))

