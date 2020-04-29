import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from database_wnd.database import Ui_DatabaseWindow
from database_wnd import config
import re


class DatabaseApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowIcon(QIcon("icon/platformUI.ico"))
        self.setFixedWidth(1034)
        database_ui = Ui_DatabaseWindow()
        database_ui.setupUi(self)

        self.database_table = database_ui.database_table

        self.database_table.setColumnWidth(0, 60)
        self.database_table.setColumnWidth(1, 100)
        self.database_table.setColumnWidth(2, 500)
        self.database_table.setColumnWidth(3, 100)

        # self.fill_in_database_headers()

    def clear_table(self):
        self.database_table.clear()

    def fill_in_database(self, database):

        database_map = []
        # print(database)
        for data in database:
            data = re.findall(r" [A-Z0-9]{2}", data)
            for d in data:
                database_map.append(d)

        # print(database_map)
        for i, header in enumerate(config.database_headers):
            newitem = QTableWidgetItem(str(i))
            newitem.setTextAlignment(Qt.AlignCenter)
            self.database_table.setItem(i, 0, newitem)
            newitem = QTableWidgetItem(str(hex(i)))
            newitem.setTextAlignment(Qt.AlignCenter)
            self.database_table.setItem(i, 1, newitem)
            self.database_table.setItem(i, 2, QTableWidgetItem(header))

            newitem = QTableWidgetItem(database_map[i])
            newitem.setTextAlignment(Qt.AlignCenter)
            self.database_table.setItem(i, 3, QTableWidgetItem(newitem))

    @staticmethod
    def format_item(item):
        newitem = QTableWidgetItem(item)
        newitem.setTextAlignment(Qt.AlignCenter)
        return newitem

    def show_window(self):
        self.show()

    def closeEvent(self, *args, **kwargs):
        print("destroy database window")
        self.destroy()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DatabaseApp()
    ex.show()
    sys.exit(app.exec_())
