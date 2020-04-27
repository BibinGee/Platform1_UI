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
        self.setWindowIcon(QIcon("../platformUI.ico"))

        database_ui = Ui_DatabaseWindow()
        database_ui.setupUi(self)

        self.database_table = database_ui.database_table
        self.major_event_table = database_ui.major_event_table
        self.minor_event_table = database_ui.minor_event_table

        self.database_table.setColumnWidth(0, 60)
        self.database_table.setColumnWidth(1, 100)
        self.database_table.setColumnWidth(2, 500)
        self.database_table.setColumnWidth(3, 100)

        # self.fill_in_database_headers()

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

    def fill_in_event_list(self, major_event_list, minor_event_list):
        major_events = re.findall(r"[A-Z0-9]{2} ", major_event_list)
        major_event_days = re.findall(r"[A-Z0-9]{4}", major_event_list)
        # print(major_events, major_event_days)

        minor_events = re.findall(r"[A-Z0-9]{2} ", minor_event_list)
        minor_event_days = re.findall(r"[A-Z0-9]{4}", minor_event_list)
        # print(minor_events, minor_event_days)

        if major_event_list != [] and major_event_days != []:
            for i, day in enumerate(major_event_days):
                if major_events[2*i].replace(" ", "") in config.major_event_headers:
                    self.major_event_table.setItem(i, 0, self.format_item(str(i)))
                    self.major_event_table.setItem(i, 1, self.format_item(major_events[2*i]))
                    self.major_event_table.setItem(i, 2, self.format_item(major_events[2*i +1]))
                    self.major_event_table.setItem(i, 3,QTableWidgetItem(config.major_event_headers[major_events[2*i].replace(" ", "")]))
                    self.major_event_table.setItem(i, 4, self.format_item(day))
                else:
                    self.major_event_table.setItem(i, 0, self.format_item(str(i)))
                    self.major_event_table.setItem(i, 1, self.format_item(major_events[2*i]))
                    self.major_event_table.setItem(i, 2, self.format_item(major_events[2*i +1]))
                    self.major_event_table.setItem(i, 3, QTableWidgetItem("undefined event ID"))
                    self.major_event_table.setItem(i, 4, self.format_item(day))
        #
        if minor_event_list != [] and minor_event_days != []:
            for j, day in enumerate(minor_event_days):
                if minor_events[2*j].replace(" ", "") in config.minor_event_headers:
                    self.minor_event_table.setItem(j, 0, self.format_item(str(j)))
                    self.minor_event_table.setItem(j, 1, self.format_item(minor_events[2*j]))
                    self.minor_event_table.setItem(j, 2, self.format_item(minor_events[2*j + 1]))
                    self.minor_event_table.setItem(j, 3, QTableWidgetItem(config.minor_event_headers[minor_events[2*j].replace(" ", "")]))
                    self.minor_event_table.setItem(j, 4, self.format_item(day))
                else:
                    self.minor_event_table.setItem(j, 0, self.format_item(str(j)))
                    self.minor_event_table.setItem(j, 1, self.format_item(minor_events[2*j]))
                    self.minor_event_table.setItem(j, 2, self.format_item(minor_events[2*j + 1]))
                    self.minor_event_table.setItem(j, 3, QTableWidgetItem("undefined event ID"))
                    self.minor_event_table.setItem(j, 4, self.format_item(day))

    @staticmethod
    def format_item(item):
        newitem = QTableWidgetItem(item)
        newitem.setTextAlignment(Qt.AlignCenter)
        return newitem

    def show_window(self):
        self.database_table.clear()
        self.event_table.clear()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DatabaseApp()
    ex.show()
    sys.exit(app.exec_())
