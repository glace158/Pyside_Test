import sys
from PySide6.QtCore import *
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import *
from dock import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Arduino GUI")

        # Window dimensions
        geometry = self.screen().availableGeometry()
        self.setFixedSize(int(geometry.width() * 0.8), int(geometry.height() * 0.7))

        self.create_menu()
        self.create_status_bar
        
        dock1 = self.create_dock_widget("dock1", Qt.LeftDockWidgetArea)
        dock2 = self.create_dock_widget("dock2", Qt.RightDockWidgetArea)
        #self.tabifyDockWidget(dock1,dock2)
        #self.create_scene()
        self.create_list_dock_widget("nodelist", Qt.RightDockWidgetArea)
    
    def create_menu(self):
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        self.create_actions()

    def create_actions(self):
        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

    def create_status_bar(self):
        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Data loaded and plotted")

    def create_dock_widget(self, title, area):
        self.setDockNestingEnabled(True)
        dock = Dock(title, self)
        #dock = QDockWidget(title,self)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea |
                            Qt.RightDockWidgetArea)
        self.addDockWidget(area, dock)
        return dock
    
    def create_list_dock_widget(self, title, area):
        self.setDockNestingEnabled(True)
        dock = ListDock(title, self)
        #dock = QDockWidget(title,self)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea |
                            Qt.RightDockWidgetArea)
        self.addDockWidget(area, dock)
        return dock
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec())