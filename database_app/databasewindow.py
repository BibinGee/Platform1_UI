import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from database_app.database import Ui_DatabaseWindow
from database_app import config
import re


class DatabaseApplication(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        database_ui = Ui_DatabaseWindow()
        database_ui.setupUi(self)

        self.database_table = database_ui.database_table
        self.event_table = database_ui.event_hisotry_table

        self.database_table.setColumnWidth(0, 60)
        self.database_table.setColumnWidth(1, 100)
        self.database_table.setColumnWidth(2, 500)
        self.database_table.setColumnWidth(3, 100)

        self.event_table.setColumnWidth(3, 400)

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
            row_number = 0
            self.event_table.setSpan(row_number, 0, 1, 5)
            self.event_table.setItem(row_number, 0, self.format_item("Major Event List"))

            row_number += 1

            for i, day in enumerate(major_event_days):
                if major_events[2*i].replace(" ", "") in config.major_event_headers:
                    self.event_table.setItem(i + row_number, 0, self.format_item(str(i)))
                    self.event_table.setItem(i + row_number, 1, self.format_item(major_events[2*i]))
                    self.event_table.setItem(i + row_number, 2, self.format_item(major_events[2*i +1]))
                    self.event_table.setItem(i + row_number, 3, self.format_item(config.major_event_headers[major_events[2*i].replace(" ", "")]))
                    self.event_table.setItem(i + row_number, 4, self.format_item(day))
                else:
                    self.event_table.setItem(i + row_number, 0, self.format_item(str(i)))
                    self.event_table.setItem(i + row_number, 1, self.format_item(major_events[2*i]))
                    self.event_table.setItem(i + row_number, 2, self.format_item(major_events[2*i +1]))
                    self.event_table.setItem(i + row_number, 3, self.format_item("undefined event ID"))
                    self.event_table.setItem(i + row_number, 4, self.format_item(day))
        #
        if minor_event_list != [] and minor_event_days != []:
            row_number += 1
            self.event_table.setSpan(row_number, 0, 1, 5)
            self.event_table.setItem(row_number, 0, self.format_item("Minor Event List"))

            row_number += 1
            for j, day in enumerate(minor_event_days):
                if minor_events[2*j].replace(" ", "") in config.minor_event_headers:
                    self.event_table.setItem(j + row_number, 0, self.format_item(str(j)))
                    self.event_table.setItem(j + row_number, 1, self.format_item(minor_events[2*j]))
                    self.event_table.setItem(j + row_number, 2, self.format_item(minor_events[2*j +1]))
                    self.event_table.setItem(j + row_number, 3, self.format_item(config.minor_event_headers[minor_events[2*j].replace(" ", "")]))
                    self.event_table.setItem(j + row_number, 4, self.format_item(day))
                else:
                    self.event_table.setItem(j + row_number, 0, self.format_item(str(j)))
                    self.event_table.setItem(j + row_number, 1, self.format_item(minor_events[2*j]))
                    self.event_table.setItem(j + row_number, 2, self.format_item(minor_events[2*j + 1]))
                    self.event_table.setItem(j + row_number, 3, self.format_item("undefined event ID"))
                    self.event_table.setItem(j + row_number, 4, self.format_item(day))

    def format_item(self, item):
        newitem = QTableWidgetItem(item)
        newitem.setTextAlignment(Qt.AlignCenter)
        return newitem



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DatabaseApplication()
    ex.show()
    sys.exit(app.exec_())
