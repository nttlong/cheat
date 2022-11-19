from PyQt5 import QtWidgets
__cache__ = {}
class BaseComponent:
    def __init__(self):
        self.widget:QtWidgets.QWidget =None
        self.name =None
    def on_click(self,handle):pass


class UIComponent:
    def __init__(self,win:QtWidgets.QWidget):
        self.widget =win
        if issubclass(type(self.widget), QtWidgets.QMainWindow):
            self.widget = self.widget.findChild(QtWidgets.QWidget, 'centralwidget')
        self.name =self.widget.objectName()
    def find(self, item)->BaseComponent:
        global __cache__
        if __cache__.get(item):
            return __cache__[item]

        for x in self.widget.children():
            if x.objectName()==item:
                __cache__[item]=UIComponent(x)
                return __cache__[item]
    def __iter__(self):

        for x in self.widget.children():
            yield UIComponent(x)
    def __dir__(self):
        for x in self.widget.children():
            yield x.objectName()
    def on_click(self,handle):
        self.widget.clicked.connect(handle)

