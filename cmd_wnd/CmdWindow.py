import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from cmd_wnd.multicommands import Ui_Form
import time


class MultiCMDApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowIcon(QIcon("icon/platformUI.ico"))

        mainwindow_ui = Ui_Form()
        mainwindow_ui.setupUi(self)

        self.text_field = mainwindow_ui.textEdit
        mainwindow_ui.confirmbtn.clicked.connect(self.transmit_cmds)
        mainwindow_ui.canclebtn.clicked.connect(self.cancel_btn_clicked)

        self.serial_device = None

    def transmit_cmds(self):
        cmd_lines = self.text_field.toPlainText()
        if '\n' in cmd_lines:
            cmd_lines = cmd_lines.split('\n')
            for cmd_line in cmd_lines:
                print(cmd_line.encode())
                self.serial_device.write(f"{cmd_line}\r".encode())
                time.sleep(0.2)
        else:
            print(cmd_lines.encode())
            self.serial_device.write(f"{cmd_lines}\r".encode())

    def cancel_btn_clicked(self):
        self.text_field.clear()
        self.close()

    def show_window(self, serial_device):
        self.show()
        self.serial_device = serial_device


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MultiCMDApp()
    ex.show()
    sys.exit(app.exec_())
