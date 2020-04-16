# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'valuechange.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.confirmbtn = QtWidgets.QPushButton(self.centralwidget)
        self.confirmbtn.setGeometry(QtCore.QRect(100, 170, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirmbtn.setFont(font)
        self.confirmbtn.setObjectName("confirmbtn")
        self.canclebtn = QtWidgets.QPushButton(self.centralwidget)
        self.canclebtn.setGeometry(QtCore.QRect(250, 170, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.canclebtn.setFont(font)
        self.canclebtn.setObjectName("canclebtn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 40, 81, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(190, 40, 160, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.address_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.address_input.setObjectName("address_input")
        self.verticalLayout_2.addWidget(self.address_input)
        self.value_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.value_input.setObjectName("value_input")
        self.verticalLayout_2.addWidget(self.value_input)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据更改"))
        self.confirmbtn.setText(_translate("MainWindow", "发送"))
        self.canclebtn.setText(_translate("MainWindow", "取消"))
        self.label.setText(_translate("MainWindow", "Address"))
        self.label_2.setText(_translate("MainWindow", "Value"))
