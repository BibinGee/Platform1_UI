# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setwindtitle.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetWindowTitleForm(object):
    def setupUi(self, SetWindowTitleForm):
        SetWindowTitleForm.setObjectName("SetWindowTitleForm")
        SetWindowTitleForm.setEnabled(True)
        SetWindowTitleForm.resize(522, 147)
        self.label = QtWidgets.QLabel(SetWindowTitleForm)
        self.label.setGeometry(QtCore.QRect(50, 40, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(SetWindowTitleForm)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.OKButton = QtWidgets.QPushButton(SetWindowTitleForm)
        self.OKButton.setGeometry(QtCore.QRect(90, 100, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OKButton.setFont(font)
        self.OKButton.setObjectName("OKButton")
        self.CancleButton = QtWidgets.QPushButton(SetWindowTitleForm)
        self.CancleButton.setGeometry(QtCore.QRect(280, 100, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CancleButton.setFont(font)
        self.CancleButton.setObjectName("CancleButton")

        self.retranslateUi(SetWindowTitleForm)
        QtCore.QMetaObject.connectSlotsByName(SetWindowTitleForm)

    def retranslateUi(self, SetWindowTitleForm):
        _translate = QtCore.QCoreApplication.translate
        SetWindowTitleForm.setWindowTitle(_translate("SetWindowTitleForm", "设置窗口标题"))
        self.label.setText(_translate("SetWindowTitleForm", "标题"))
        self.OKButton.setText(_translate("SetWindowTitleForm", "确定"))
        self.CancleButton.setText(_translate("SetWindowTitleForm", "取消"))
