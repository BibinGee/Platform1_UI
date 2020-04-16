import time

from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QTextCursor

import mainwindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import serial
from serialport_app import serialportwindow
from database_app import databasewindow
from valuechange_app import valuechangewindow
from multicommand_app import multicommandwindow

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        mainwindown_ui = mainwindow.Ui_MainWindow()
        mainwindown_ui.setupUi(self)
        mainwindown_ui.actionExit_2.triggered.connect(self.close)
        mainwindown_ui.actionSerial_port.triggered.connect(self.serial_port_show)
        mainwindown_ui.actionabout_Platform1_UI.triggered.connect(self.about_show)
        mainwindown_ui.actionOpen.triggered.connect(self.open_serial_port)
        mainwindown_ui.actionClose.triggered.connect(self.close_serial_port)
        mainwindown_ui.actionAll_Seriap_output_ON.triggered.connect(self.set_command_all_serial_on)
        mainwindown_ui.actionG_dump.triggered.connect(self.set_command_G_dump)
        mainwindown_ui.actionCheck_FW_revision.triggered.connect(self.set_command_check_fw_revision)
        mainwindown_ui.actionForce_analysis_mode.triggered.connect(self.set_command_force_analysis_mode)
        mainwindown_ui.actionBattery_test.triggered.connect(self.set_command_battery_test)
        mainwindown_ui.actionChange_value.triggered.connect(self.set_command_change_value)
        mainwindown_ui.actionSkip_HD2.triggered.connect(self.set_command_skip_hd2_cal)
        mainwindown_ui.actionSkip_2_Point_Cal.triggered.connect(self.set_command_skip_2_point_cal)
        mainwindown_ui.actionMulti_commands.triggered.connect(self.set_command_multi_commands)

        self.timer = QBasicTimer()  # Define timer to loop events
        self.serial_window = serialportwindow.SerialPortApplication(self)
        self.serial_port = ""
        self.baudrate = ""
        self.serial_device = serial.Serial()
        self.output_field = mainwindown_ui.outputfield

        self.action_open = mainwindown_ui.actionOpen
        self.action_close = mainwindown_ui.actionClose

        self.database_window = databasewindow.DatabaseApplication(self)
        self.value_change_window = valuechangewindow.ValueChangeApplication(self)
        self.multi_CMD_window = multicommandwindow.MultiCMDApplication(self)

    def open_serial_port(self):
        print("serial device opened...")
        print(self.serial_window.port, self.serial_window.baudrate)
        if self.serial_window.port != "" and self.serial_window.baudrate != "" and not self.serial_device.is_open:
            self.serial_device.timeout = 0.05
            try:
                self.serial_device.port = self.serial_window.port
                self.serial_device.baudrate = self.serial_window.baudrate
                self.serial_device.open()
                self.action_close.setEnabled(True)
                print(f"{self.serial_window.port} opened, baud rate: {self.serial_window.baudrate}")

            except serial.serialutil.SerialException as e:
                print(e)
                QMessageBox.warning(self, 'Warning', str(e))
                self.serial_device.close()
        else:
            QMessageBox.warning(self, 'Warning', f"{self.serial_window.port} is opened")

        self.timer.start(100, self)

    def close_serial_port(self):
        print("serial device closed...")
        self.serial_device.close()
        self.timer.stop()
        self.action_close.setEnabled(False)

    def serial_port_show(self):
        self.serial_window.show()
        self.action_open.setEnabled(True)

    def about_show(self):
        from about import about
        about_window = QMainWindow(self)
        about_ui = about.Ui_MainWindow()
        about_ui.setupUi(about_window)
        about_window.show()

    def timerEvent(self, event):
        # print("timer tick...")
        serial_data = self.serial_device.readline()
        if serial_data != b'':
            lines = serial_data.decode("utf-8", errors='replace')
            cur_time = time.strftime('[%H:%M:%S] ', time.localtime())
            for line in lines.split("\r"):
                if line != "\r" and line != "":
                    line = cur_time + line
                    # if len(self.tedit.toPlainText()) > 5000:  # almost every 50 lines, clear the buffer
                    #     self.tedit.clear()
                    self.output_field.append(line)  # serial data showing on text field.
            self.output_field.moveCursor(QTextCursor.End)  # move cursor to the end.

    def set_command_all_serial_on(self):
        print("set_command_all_serial_on")
        self.serial_device.write("BA\r".encode())
        self.output_field.append("BA")

    def set_command_G_dump(self):
        print("set_command_G_dump")
        if self.serial_device.isOpen():
            try:
                self.serial_device.write("G1\r".encode())
                self.output_field.append("G1")
                time.sleep(0.2)
                database = self.serial_device.readline()
                database = database.decode("utf-8", errors='replace')
                self.output_field.append(database)
                database_map = database.split('\r')[2:]
                self.database_window.fill_in_database(database_map)

                self.serial_device.write("G4\r".encode())
                self.output_field.append("G4")
                time.sleep(0.2)
                major_event_list = self.serial_device.readline()
                print(f"major event list: {major_event_list}")
                major_event_list = major_event_list.decode("utf-8", errors='replace')
                self.output_field.append(major_event_list)

                self.serial_device.write("G5\r".encode())
                self.output_field.append("G5")
                time.sleep(0.2)
                minor_event_list = self.serial_device.readline()
                print(f"minor event list: {minor_event_list}")
                minor_event_list = minor_event_list.decode("utf-8", errors='replace')
                self.output_field.append(minor_event_list)

                self.database_window.fill_in_event_list(major_event_list, minor_event_list)

                self.database_window.show()

            except Exception as e:
                print(e)

    def set_command_force_analysis_mode(self):
        print("set_command_force_analysis_mode")
        self.serial_device.write("A1\r".encode())
        self.output_field.append("A1")

    def set_command_check_fw_revision(self):
        print("set_command_check_fw_revision")
        self.serial_device.write("C0\r".encode())
        self.output_field.append("C0")

    def set_command_battery_test(self):
        print("set_command_battery_test")
        self.serial_device.write("b\r".encode())
        self.output_field.append("b")

    def set_command_change_value(self):
        print("set_command_change_value")
        self.value_change_window.show_window(self.serial_device)

    def set_command_skip_hd2_cal(self):
        print("set_command_skip_hd2_cal")
        self.serial_device.write("c1 06 F7\r".encode())
        self.output_field.append("c1 06 F7")
        time.sleep(0.2)
        self.serial_device.write("c2\r".encode())
        self.output_field.append("c2")

    def set_command_skip_2_point_cal(self):
        print("set_command_skip_2_point_cal")
        self.serial_device.write("c1 06 FF\r".encode())
        self.output_field.append("c1 06 FF")
        time.sleep(0.2)
        self.serial_device.write("c2\r".encode())
        self.output_field.append("c2")

    def set_command_multi_commands(self):
        print("set_command_multi_commands")
        self.multi_CMD_window.show_window(self.serial_device)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Application()
    MainWindow.show()
    sys.exit(app.exec_())
