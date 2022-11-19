import cy_kit
import process
from PyQt5 import QtWidgets
import windows.main_windows
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = main_win=windows.main_windows.Ui()
    def run_ok(*args,**kwargs):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("This is a message box")
        msg.setInformativeText("This is additional information")
        msg.setWindowTitle("MessageBox demo")
        msg.setDetailedText("The details are as follows:")
        msg.show()
        msg.exec()



    win.component.find('button_select_process').on_click(handle =run_ok)

    for x in win.component:
        print(x.name)
    win.show()

    import sys
    sys.exit(app.exec())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
