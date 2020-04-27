import time

import xlwt as xlwt
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QTextCursor, QIcon

import mainwindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QInputDialog, QLineEdit
import serial
from serialconfig_wnd import SerialConfigWindow
from database_wnd import DBWindow
from valuechange_wnd import ValChangeWindow
from cmd_wnd import CmdWindow
from save_wnd import SaveApp
from setwindowtitle_wind import SetWindTitleWindow
import string


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("platformUI.ico"))

        mainwindown_ui = mainwindow.Ui_MainWindow()
        mainwindown_ui.setupUi(self)
        mainwindown_ui.actionSave_2.triggered.connect(self.save_click)
        mainwindown_ui.actionExit_2.triggered.connect(self.close)
        mainwindown_ui.actionStop.triggered.connect(self.save_paused)
        mainwindown_ui.actionShow_record.triggered.connect(self.show_record)
        mainwindown_ui.actionSerial_port.triggered.connect(self.serial_port_show)
        mainwindown_ui.actionabout_Platform1_UI.triggered.connect(self.about_show)
        mainwindown_ui.actionOpen.triggered.connect(self.open_serial_port)
        mainwindown_ui.actionClose.triggered.connect(self.close_serial_port)
        mainwindown_ui.actionAll_serial_output_ON.triggered.connect(self.set_command_all_serial_on)
        mainwindown_ui.actionCloseSerial.triggered.connect(self.set_serial_output_clsoed)
        mainwindown_ui.actionOnly_Smoke_output.triggered.connect(self.set_serial_smoke_only)
        mainwindown_ui.actionOnly_CO_output.triggered.connect(self.set_serial_CO_only)
        mainwindown_ui.actionG_dump.triggered.connect(self.set_command_G_dump)
        mainwindown_ui.actionCheck_FW_revision.triggered.connect(self.set_command_check_fw_revision)
        mainwindown_ui.actionForce_analysis_mode.triggered.connect(self.set_command_force_analysis_mode)
        mainwindown_ui.actionBattery_test.triggered.connect(self.set_command_battery_test)
        mainwindown_ui.actionChange_value.triggered.connect(self.set_command_change_value)
        mainwindown_ui.actionSkip_HD2.triggered.connect(self.set_command_skip_hd2_cal)
        mainwindown_ui.actionSkip_2_Point_Cal.triggered.connect(self.set_command_skip_2_point_cal)
        mainwindown_ui.actionMulti_commands.triggered.connect(self.set_command_multi_commands)
        mainwindown_ui.actionL0.triggered.connect(self.set_command_L0)
        mainwindown_ui.actionL1.triggered.connect(self.set_command_L1)
        mainwindown_ui.actionL4.triggered.connect(self.set_command_L4)
        mainwindown_ui.actionL5.triggered.connect(self.set_command_L5)
        mainwindown_ui.actionSetWindTitle.triggered.connect(self.show_set_window)
        mainwindown_ui.actionClearbuffer.triggered.connect(self.clear_buffer)

        self.timer = QBasicTimer()  # Define timer to loop events
        self.serial_window = SerialConfigWindow.SerialPortApp(self)
        self.serial_port = ""
        self.baudrate = ""
        self.serial_device = serial.Serial()
        self.output_field = mainwindown_ui.outputfield

        self.command_menu = mainwindown_ui.menuCommand
        self.action_open = mainwindown_ui.actionOpen
        self.action_close = mainwindown_ui.actionClose
        self.action_save = mainwindown_ui.actionSave_2
        self.action_pause = mainwindown_ui.actionStop
        self.action_show_record = mainwindown_ui.actionShow_record

        self.database_window = DBWindow.DatabaseApp(self)
        self.value_change_window = ValChangeWindow.ValueChangeApp(self)
        self.cmd_window = CmdWindow.MultiCMDApp(self)
        self.saveWindow = SaveApp.SaveApp(self)
        self.saveWindow.pauseBtn.clicked.connect(self.save_paused)
        self.setWinTitle = SetWindTitleWindow.SetWindTItleApp()
        self.setWinTitle.ok_button.clicked.connect(self.set_window_title)

        self.filepath = ""
        self.workbook = None
        self.row_number = 0

    def save_click(self):
        path, extension = QFileDialog.getSaveFileName(caption='Save file', directory='',
                                                      filter='Excel(*.xls);;Text(*.txt)')
        print(path, extension)
        if path != "":
            self.filepath = path
            self.workbook = self.save_file_init(path)
            self.action_save.setEnabled(False)
            self.action_pause.setEnabled(True)
            self.action_show_record.setEnabled(True)
            self.saveWindow.show_window(path)
            self.saveWindow.clear_transferred_bytes()
            self.saveWindow.pauseBtn.setEnabled(True)

    def save_file_init(self, file):
        col_titles = [
            "Time", "1 IR-F-R", "2 IR-B-R", "3 BL-F-R", "4 IR-F_X0", "5 IR-B_X0", "6 BL-F_X0",
            "7 IR-F_S1_X0", "8 IR-B_S1_X0", "9 BL-F_S1_X0", "10 Amt_Light_FW", "11 Amt_Light_BW",
            "12 IR-F/IR-B_MSB", "13 IR-F/IR-B_LSB", "14 BL-F/IR-B_MSB", "15 BL-F/IR-B_LSB", "16 BL-F/IR-F_MSB",
            "17 BL-F/IR-F_MSB", "18 MW_State", "19 MSB", "20 LSB", "21 Equation", "22 F_Cnt", "23 F_Cnt",
            "24 Ambient_IR-F", "25 Ambient_IR-B", "26 Ambient_Blue", "27 Change_IR-F", "28 Change_IR-B",
            "29 Change_Blue", "30 Int_Cnt", "31 Int_Cnt", "", "32 Alarm",
        ]

        style = self.get_xlwt_style()

        workbook = xlwt.Workbook(encoding='utf-8')
        hex_sheet = workbook.add_sheet('Hex data', cell_overwrite_ok=True)
        dec_sheet = workbook.add_sheet('Dec data', cell_overwrite_ok=True)

        if file.endswith("xls"):
            for i, text in enumerate(col_titles):  # writing 32 bytes title to xls file.
                hex_sheet.write(0, i, text, style)
                dec_sheet.write(0, i, text, style)

            self.set_xlwt_row_number(1)  # row number increase.
            workbook.save(file)  # save workbook
            return workbook
        else:
            with open(file, "a+", encoding="utf-8") as f:  # writing title information to txt file.
                f.write("Time Serial_data ")
                f.write("\n")
            return None

    def get_xlwt_style(self):
        style = xlwt.XFStyle()
        align = xlwt.Alignment()
        align.horz = xlwt.Alignment.HORZ_CENTER
        align.wrap = xlwt.Alignment.WRAP_AT_RIGHT
        align.vert = xlwt.Alignment.VERT_CENTER
        style.alignment = align
        return style

    def save_file(self, serial_data):
        saved_bytes = 0
        cur_time = time.strftime('%H:%M:%S', time.localtime())
        text = serial_data.replace(">", "")
        # text = text.encode("gbk", 'ignore').decode("gbk", "ignore")  # To ignore some mess up characters.

        row_number = self.get_xlwt_row_number()
        if self.filepath.endswith("xls"):
            if len(text) > 95:
                hex_sheet = self.workbook.get_sheet(0)
                dec_sheet = self.workbook.get_sheet(1)
                style = self.get_xlwt_style()

                hex_sheet.write(row_number, 0, cur_time, style)
                dec_sheet.write(row_number, 0, cur_time, style)
                for i, element in enumerate(text.split(" ")):  # writing 32 bytes serial data from column 3 to 35
                    hex_sheet.write(row_number, 1 + i, element, style)
                    if all(c in string.hexdigits for c in
                           element) and element != '':  # the last byte is alarm condition, condition outputs: "N" or "Y"
                        dec_sheet.write(row_number, 1 + i, int(element, 16), style)  # convert hex to decimal
                    else:
                        dec_sheet.write(row_number, 1 + i, element, style)
                    saved_bytes = i

                self.set_xlwt_row_number(row_number + 1)  # row number increase
                self.workbook.save(self.filepath)  # save workbook

            return saved_bytes * 2
        else:
            saved_bytes = len(text)
            with open(self.filepath, "a+", encoding="utf-8") as f:
                f.write(f"{cur_time} {text}")
                f.write("\n")
            return saved_bytes

    def get_xlwt_row_number(self):
        return self.row_number

    def set_xlwt_row_number(self, row_number):
        self.row_number = row_number

    def save_paused(self):
        self.filepath = ""
        self.workbook = None
        self.action_save.setEnabled(True)
        self.action_pause.setEnabled(False)
        self.action_show_record.setEnabled(False)
        self.saveWindow.pauseBtn.setEnabled(False)

    def show_record(self):
        self.saveWindow.show_window(self.filepath)

    def open_serial_port(self):
        print("serial device opened...")
        print(self.serial_window.port, self.serial_window.baudrate)
        if self.serial_window.port != "" and self.serial_window.baudrate != "" and not self.serial_device.is_open:
            self.serial_device.timeout = 0.05
            try:
                self.serial_device.port = self.serial_window.port
                self.serial_device.baudrate = self.serial_window.baudrate
                self.serial_device.open()
                self.action_open.setEnabled(False)
                self.action_close.setEnabled(True)
                self.command_menu.setEnabled(True)
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
        self.action_open.setEnabled(True)
        self.command_menu.setEnabled(False)

    def serial_port_show(self):
        self.serial_window.show_window()
        self.action_open.setEnabled(True)

    def clear_buffer(self):
        self.output_field.clear()

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
            if "\n" in lines:
                lines = lines.replace("\n", "\r")
            splited_lines = lines.split("\r")
            for line in splited_lines:
                if line != '':
                    line = cur_time + line
                    self.output_field.append(line)  # serial data showing on text field.
            self.output_field.moveCursor(QTextCursor.End)  # move cursor to the end.

            if self.filepath != "":
                saved_bytes = self.save_file(lines)
                self.saveWindow.set_transferred_bytes(saved_bytes)

    def show_set_window(self):
        self.setWinTitle.show()

    def set_window_title(self):
        self.setWinTitle.close()
        self.setWindowTitle(self.setWinTitle.getText())

    def set_command_all_serial_on(self):
        print("set_command_all_serial_on")
        self.serial_device.write("BA\r".encode())
        self.output_field.append("BA")

    def set_serial_output_clsoed(self):
        print("set_serial_output_clsoed")
        self.serial_device.write("BZ\r".encode())

    def set_serial_smoke_only(self):
        print("set_serial_smoke_only")
        self.serial_device.write("BE\r".encode())

    def set_serial_CO_only(self):
        print("set_serial_CO_only")
        self.serial_device.write("BC\r".encode())

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
        self.cmd_window.show_window(self.serial_device)

    def set_command_L0(self):
        print("set_command_L0")
        self.serial_device.write("L0\r".encode())

    def set_command_L1(self):
        print("set_command_L1")
        self.serial_device.write("L1\r".encode())

    def set_command_L4(self):
        print("set_command_L4")
        self.serial_device.write("L4\r".encode())

    def set_command_L5(self):
        print("set_command_L5")
        self.serial_device.write("L5\r".encode())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = Application()
    MainWindow.show()
    sys.exit(app.exec_())
