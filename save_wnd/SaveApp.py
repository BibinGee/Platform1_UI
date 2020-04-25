import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from save_wnd.save import Ui_Form


class SaveApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowIcon(QIcon("../platformUI.ico"))

        save_ui = Ui_Form()
        save_ui.setupUi(self)

        self.pauseBtn = save_ui.pauseBtn
        self.closeBtn = save_ui.closeBtn
        self.path_field = save_ui.file_path
        self.byte_field = save_ui.transferred_bytes

        self.closeBtn.clicked.connect(self.close_btn_clicked)

        self.saved_number = 0

    def close_btn_clicked(self):
        self.close()

    def show_window(self, path):
        self.path_field.setText(path)
        self.show()

    def set_transferred_bytes(self, byte_number):
        self.saved_number += byte_number
        self.byte_field.setText(f"{self.saved_number} bytes transferred")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SaveApp()
    ex.show()
    sys.exit(app.exec_())
