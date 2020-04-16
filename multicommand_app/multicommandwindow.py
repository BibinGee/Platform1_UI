import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from multicommand_app.multicommands import Ui_Form
import time


class MultiCMDApplication(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        mainwindow_ui = Ui_Form()
        mainwindow_ui.setupUi(self)

        self.text_field = mainwindow_ui.textEdit
        mainwindow_ui.confirmbtn.clicked.connect(self.transmit_cmds)
        mainwindow_ui.canclebtn.clicked.connect(self.cancle_btn_clicked)

        self.serial_device = None

    def transmit_cmds(self):
        cmd_lines = self.text_field.toPlainText().split('\n')
        print(cmd_lines[0].encode())
        self.serial_device.write(f"{cmd_lines[0]}\r".encode())
        time.sleep(0.2)
        print(cmd_lines[1].encode())
        self.serial_device.write(f"{cmd_lines[1]}\r".encode())

    def cancle_btn_clicked(self):
        self.text_field.clear()
        self.close()

    def show_window(self, serial_device):
        self.show()
        self.serial_device = serial_device


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MultiCMDApplication()
    ex.show()
    sys.exit(app.exec_())
