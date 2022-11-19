import pathlib
import os
from PyQt5 import QtWidgets, uic
from ui.utils import UIComponent
ui_path = os.path.join(pathlib.Path(__file__).parent.parent.__str__(),"ui","main_windows.ui")
import sys
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(ui_path, self) # Load the .ui file
        self.component =  UIComponent(self)


class App:
    def __init__(self):
        self.win = Ui()
    def run(self):
        self.win.show()