# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'event_history_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1034, 541)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(12, 12, 1021, 521))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.major_event_table = QtWidgets.QTableWidget(self.tab_2)
        self.major_event_table.setEnabled(True)
        self.major_event_table.setGeometry(QtCore.QRect(11, 11, 993, 481))
        self.major_event_table.setMinimumSize(QtCore.QSize(993, 0))
        self.major_event_table.setShowGrid(True)
        self.major_event_table.setRowCount(500)
        self.major_event_table.setColumnCount(5)
        self.major_event_table.setObjectName("major_event_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.major_event_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.major_event_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.major_event_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.major_event_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.major_event_table.setHorizontalHeaderItem(4, item)
        self.major_event_table.horizontalHeader().setVisible(True)
        self.major_event_table.horizontalHeader().setCascadingSectionResizes(True)
        self.major_event_table.horizontalHeader().setDefaultSectionSize(200)
        self.major_event_table.horizontalHeader().setMinimumSectionSize(50)
        self.major_event_table.verticalHeader().setVisible(False)
        self.major_event_table.verticalHeader().setCascadingSectionResizes(False)
        self.major_event_table.verticalHeader().setHighlightSections(True)
        self.tabWidget.addTab(self.tab_2, "")
        self.MinorE = QtWidgets.QWidget()
        self.MinorE.setObjectName("MinorE")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.MinorE)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.minor_event_table = QtWidgets.QTableWidget(self.MinorE)
        self.minor_event_table.setMinimumSize(QtCore.QSize(993, 0))
        self.minor_event_table.setShowGrid(True)
        self.minor_event_table.setRowCount(500)
        self.minor_event_table.setColumnCount(5)
        self.minor_event_table.setObjectName("minor_event_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.minor_event_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.minor_event_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.minor_event_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.minor_event_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.minor_event_table.setHorizontalHeaderItem(4, item)
        self.minor_event_table.horizontalHeader().setCascadingSectionResizes(True)
        self.minor_event_table.horizontalHeader().setDefaultSectionSize(200)
        self.minor_event_table.horizontalHeader().setMinimumSectionSize(50)
        self.minor_event_table.verticalHeader().setVisible(False)
        self.minor_event_table.verticalHeader().setCascadingSectionResizes(False)
        self.minor_event_table.verticalHeader().setHighlightSections(True)
        self.verticalLayout_4.addWidget(self.minor_event_table)
        self.tabWidget.addTab(self.MinorE, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Event history list"))
        self.major_event_table.setSortingEnabled(True)
        item = self.major_event_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Index"))
        item = self.major_event_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Event ID"))
        item = self.major_event_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Sequency"))
        item = self.major_event_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Event description"))
        item = self.major_event_table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Day"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Major Event Hisotry"))
        self.minor_event_table.setSortingEnabled(True)
        item = self.minor_event_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Index"))
        item = self.minor_event_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Event ID"))
        item = self.minor_event_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Sequency"))
        item = self.minor_event_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Event description"))
        item = self.minor_event_table.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Day"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MinorE), _translate("Form", "Minior Event History"))
