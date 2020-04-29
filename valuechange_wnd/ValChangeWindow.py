import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from valuechange_wnd.valuechange import Ui_MainWindow
import time


class ValueChangeApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowIcon(QIcon("icon/platformUI.ico"))

        mainwindow_ui = Ui_MainWindow()
        mainwindow_ui.setupUi(self)

        mainwindow_ui.confirmbtn.clicked.connect(self.transmit_change)
        mainwindow_ui.canclebtn.clicked.connect(self.canclebtn_clicked)

        self.address = ""
        self.value = ""

        self.address_input = mainwindow_ui.address_input
        self.value_input = mainwindow_ui.value_input
        self.serial_device = None

    def transmit_change(self):
        self.address = self.address_input.text()
        self.value = self.value_input.text()

        print(f"address:{self.address}, value:{self.value}")

        self.serial_device.write(f"c1 {self.address} {self.value}\r".encode())
        time.sleep(0.2)
        self.serial_device.write("c2\r".encode())

    def canclebtn_clicked(self):
        self.address = ""
        self.value = ""
        self.close()

    def show_window(self, serial_device):
        self.show()
        self.serial_device = serial_device


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ValueChangeApp()
    ex.show()
    sys.exit(app.exec_())
