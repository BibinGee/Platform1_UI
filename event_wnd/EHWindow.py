import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from event_wnd import event_history_ui
import re
from database_wnd import config


class EventHistoryApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowIcon(QIcon("icon/platformUI.ico"))
        self.setFixedWidth(1034)
        event_history = event_history_ui.Ui_Form()
        event_history.setupUi(self)

        self.major_event_table = event_history.major_event_table
        self.minor_event_table = event_history.minor_event_table

        self.major_event_table.setColumnWidth(0, 120)
        self.major_event_table.setColumnWidth(1, 120)
        self.major_event_table.setColumnWidth(2, 120)
        self.major_event_table.setColumnWidth(3, 400)

        self.minor_event_table.setColumnWidth(0, 120)
        self.minor_event_table.setColumnWidth(1, 120)
        self.minor_event_table.setColumnWidth(2, 120)
        self.minor_event_table.setColumnWidth(3, 400)

    def clear_table(self):
        self.major_event_table.clear()
        self.minor_event_table.clear()

    def fill_in_event_list(self, major_event_list, minor_event_list):
        major_events = re.findall(r"[A-Z0-9]{2} ", major_event_list)
        major_event_days = re.findall(r"[A-Z0-9]{4}", major_event_list)
        # print(major_events, major_event_days)

        minor_events = re.findall(r"[A-Z0-9]{2} ", minor_event_list)
        minor_event_days = re.findall(r"[A-Z0-9]{4}", minor_event_list)
        # print(minor_events, minor_event_days)

        if major_event_list != []:
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
        if minor_event_days != []:
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
        self.show()

    def closeEvent(self, *args, **kwargs):
        print("destroy event history window")
        self.destroy()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EventHistoryApp()
    ex.show()
    sys.exit(app.exec_())
