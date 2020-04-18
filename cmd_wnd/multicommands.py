# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multicommands.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(495, 267)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 471, 191))
        self.textEdit.setObjectName("textEdit")
        self.confirmbtn = QtWidgets.QPushButton(Form)
        self.confirmbtn.setGeometry(QtCore.QRect(110, 220, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirmbtn.setFont(font)
        self.confirmbtn.setObjectName("confirmbtn")
        self.canclebtn = QtWidgets.QPushButton(Form)
        self.canclebtn.setGeometry(QtCore.QRect(280, 220, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.canclebtn.setFont(font)
        self.canclebtn.setObjectName("canclebtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "多行命令发送"))
        self.confirmbtn.setText(_translate("Form", "发送"))
        self.canclebtn.setText(_translate("Form", "取消"))
