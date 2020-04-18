import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from serialconfig_wnd import serialport
import serial.tools.list_ports


class SerialPortApplication(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        serial_port_ui = serialport.Ui_MainWindow()
        serial_port_ui.setupUi(self)

        serial_port_ui.confirmbtn.clicked.connect(self.confirm_btn_clicked)
        serial_port_ui.canclebtn.clicked.connect(self.cancle_btn_clicked)

        ports = serial.tools.list_ports.comports(include_links=False)
        for port in ports:
            serial_port_ui.comboBox.addItem(port.device)

        self.port_combox = serial_port_ui.comboBox
        self.baudrate_combox = serial_port_ui.comboBox_2
        self.port = ""
        self.baudrate = ""

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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = SerialPortApplication()

    ex.show()

    sys.exit(app.exec_())
