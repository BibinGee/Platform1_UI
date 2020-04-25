import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
from serialconfig_wnd import serialport
import serial.tools.list_ports


class SerialPortApp(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowIcon(QIcon("../platformUI.ico"))

        serial_port_ui = serialport.Ui_MainWindow()
        serial_port_ui.setupUi(self)

        serial_port_ui.confirmbtn.clicked.connect(self.confirm_btn_clicked)
        serial_port_ui.canclebtn.clicked.connect(self.cancle_btn_clicked)

        self.port_combox = serial_port_ui.comboBox
        self.baudrate_combox = serial_port_ui.comboBox_2
        self.port = ""
        self.baudrate = ""

        self.ports_refresh()

    def ports_refresh(self):
        self.port_combox.clear()
        ports = serial.tools.list_ports.comports(include_links=False)
        for port in ports:
            self.port_combox.addItem(port.device)

    def confirm_btn_clicked(self):
        print("confirm btn clicked")
        self.port = self.port_combox.currentText()
        self.baudrate = self.baudrate_combox.currentText()
        self.close()

    def cancle_btn_clicked(self):
        print("cancle btn clicked")
        self.port = ""
        self.baudrate = ""
        self.close()

    def show_window(self):
        self.show()
        self.ports_refresh()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = SerialPortApp()

    ex.show()

    sys.exit(app.exec_())
