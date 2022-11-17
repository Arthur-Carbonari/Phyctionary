from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMenuBar


class MyMenuBar(QMenuBar):

    def __init__(self, parent):
        super().__init__()

        self.setNativeMenuBar(False)

        # Add menus to menu bar
        file_menu = self.addMenu(" File")  # Add file menu to the menu bar, "File" is reserved in Mac
        tool_menu = self.addMenu(" Tool")  # Add the "Brush Size" menu to the menu bar

        # File Menu ========================

        # Save Action
        save_action = QAction(QIcon("./icons/save.png"), "Save", parent)  # Create a save action with an icon
        save_action.setShortcut("Ctrl+S")  # Connect this save action to a keyboard shortcut
        file_menu.addAction(save_action)  # Add the save action to the file menu
        save_action.triggered.connect(parent.canvas.save)  # Connect action to respective slot

        # Open Action
        open_action = QAction(QIcon("./icons/open.png"), "Open", parent)  # Create a save action with an icon
        open_action.setShortcut("Ctrl+O")  # Connect this save action to a keyboard shortcut
        file_menu.addAction(open_action)  # Add the save action to the file menu
        open_action.triggered.connect(parent.canvas.open)  # Connect action to respective slot

        # Insert Action
        insert_action = QAction(QIcon("./icons/insert.png"), "Insert Image", parent)  # Create a save action with an icon
        insert_action.setShortcut("Ctrl+I")  # Connect this save action to a keyboard shortcut
        file_menu.addAction(insert_action)  # Add the save action to the file menu
        insert_action.triggered.connect(parent.canvas.insert_image)  # Connect action to respective slot

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

        # Exit action
        exit_action = QAction(QIcon("./icons/exit.png"), "Exit", parent)  # Create a clear action with icon
        exit_action.setShortcut("Alt+X")  # Connect this clear action to a keyboard shortcut
        file_menu.addAction(exit_action)  # Add this action to the file menu
        exit_action.triggered.connect(exit)  # Connect action to respective slot

        # Tool Menu ========================

        # Change Tool Thickness
        increase_tool_size = QAction(QIcon(), "Increase brush size", parent)
        increase_tool_size.setShortcut("Ctrl++")
        tool_menu.addAction(increase_tool_size)  # connect the action to the function below
        increase_tool_size.triggered.connect(parent.controllers_box.increase_tool_size)

        decrease_tool_size = QAction(QIcon("./icons/three_px.png"), "Decrease brush size", parent)
        decrease_tool_size.setShortcut("Ctrl+-")
        tool_menu.addAction(decrease_tool_size)  # connect the action to the function below
        decrease_tool_size.triggered.connect(parent.controllers_box.decrease_tool_size)

        # Change Tool
        change_to_brush = QAction(QIcon("./icons/paint-brush.png"), "Brush", parent)
        change_to_brush.setShortcut("Ctrl+Alt+B")
        tool_menu.addAction(change_to_brush)  # connect the action to the function below
        change_to_brush.triggered.connect(lambda: parent.canvas.change_current_tool("brush"))

        change_to_eraser = QAction(QIcon("./icons/eraser.png"), "Eraser", parent)
        change_to_eraser.setShortcut("Ctrl+Alt+E")
        tool_menu.addAction(change_to_eraser)  # connect the action to the function below
        change_to_eraser.triggered.connect(lambda: parent.canvas.change_current_tool("eraser"))

        change_to_spray = QAction(QIcon("./icons/spray.png"), "Spray", parent)
        change_to_spray.setShortcut("Ctrl+Alt+S")
        tool_menu.addAction(change_to_spray)  # connect the action to the function below
        change_to_spray.triggered.connect(lambda: parent.canvas.change_current_tool("spray"))

        change_to_bucket = QAction(QIcon("./icons/bucket.png"), "Bucket", parent)
        change_to_bucket.setShortcut("Ctrl+Alt+F")
        tool_menu.addAction(change_to_bucket)  # connect the action to the function below
        change_to_bucket.triggered.connect(lambda: parent.canvas.change_current_tool("bucket"))

        # Change Tool Colors
        skip_turn_action = QAction(QIcon("./icons/black.png"), "Black", parent)
        skip_turn_action.setShortcut("Ctrl+B")
        tool_menu.addAction(skip_turn_action)
        skip_turn_action.triggered.connect(lambda: parent.controllers_box.change_current_color("#000000"))

        # Skip Turn
        skip_turn_action = QAction(QIcon("./icons/skip.png"), "Skip Turn", parent)
        skip_turn_action.setShortcut("Ctrl+Shift+S")
        tool_menu.addAction(skip_turn_action)
        skip_turn_action.triggered.connect(parent.skip_turn)


