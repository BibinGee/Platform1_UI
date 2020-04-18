# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(508, 174)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 91, 80))
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(160, 30, 341, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.file_path = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.file_path.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.file_path.setFont(font)
        self.file_path.setObjectName("file_path")
        self.verticalLayout_2.addWidget(self.file_path)
        self.transferred_bytes = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.transferred_bytes.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.transferred_bytes.setFont(font)
        self.transferred_bytes.setObjectName("transferred_bytes")
        self.verticalLayout_2.addWidget(self.transferred_bytes)
        self.pauseBtn = QtWidgets.QPushButton(Form)
        self.pauseBtn.setGeometry(QtCore.QRect(120, 130, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pauseBtn.setFont(font)
        self.pauseBtn.setObjectName("pauseBtn")
        self.closeBtn = QtWidgets.QPushButton(Form)
        self.closeBtn.setGeometry(QtCore.QRect(300, 130, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName("closeBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "文件路径"))
        self.label_2.setText(_translate("Form", "传输字节"))
        self.pauseBtn.setText(_translate("Form", "停止"))
        self.closeBtn.setText(_translate("Form", "关闭"))
