import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from setwindowtitle_wind.setwindtitle import Ui_SetWindowTitleForm


class SetWindTItleApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowIcon(QIcon("icon/platformUI.ico"))

        ui = Ui_SetWindowTitleForm()
        ui.setupUi(self)

        self.ok_button = ui.OKButton
        self.cancel_button = ui.CancleButton
        self.input_text = ui.lineEdit

        self.title = ""

    def getText(self):
        self.title = self.input_text.text()
        return self.title

    def cancel_buton_clicked(self):
        self.title = ""
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SetWindTItleApp()
    ex.show()
    sys.exit(app.exec_())
