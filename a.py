# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AntennaCalulator(object):
    def setupUi(self, AntennaCalulator):
        AntennaCalulator.setObjectName("AntennaCalulator")
        AntennaCalulator.resize(585, 406)
        self.centralwidget = QtWidgets.QWidget(AntennaCalulator)
        self.centralwidget.setObjectName("centralwidget")
        self.Calculate = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate.setGeometry(QtCore.QRect(120, 280, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Calculate.setFont(font)
        self.Calculate.setObjectName("Calculate")
        self.Quit = QtWidgets.QPushButton(self.centralwidget)
        self.Quit.setGeometry(QtCore.QRect(320, 280, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Quit.setFont(font)
        self.Quit.setObjectName("Quit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 180, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 230, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 70, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(320, 40, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.An_L = QtWidgets.QTextBrowser(self.centralwidget)
        self.An_L.setGeometry(QtCore.QRect(250, 200, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.An_L.setFont(font)
        self.An_L.setObjectName("An_L")
        self.An_W = QtWidgets.QTextBrowser(self.centralwidget)
        self.An_W.setGeometry(QtCore.QRect(250, 90, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.An_W.setFont(font)
        self.An_W.setObjectName("An_W")
        self.fc = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.fc.setGeometry(QtCore.QRect(40, 220, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fc.setFont(font)
        self.fc.setDecimals(4)
        self.fc.setMaximum(999999999999999.0)
        self.fc.setObjectName("fc")
        self.er = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.er.setGeometry(QtCore.QRect(40, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.er.setFont(font)
        self.er.setDecimals(1)
        self.er.setObjectName("er")
        self.he = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.he.setEnabled(True)
        self.he.setGeometry(QtCore.QRect(40, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.he.setFont(font)
        self.he.setDecimals(4)
        self.he.setMaximum(100.99)
        self.he.setProperty("value", 0.0)
        self.he.setObjectName("he")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(510, 210, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(510, 100, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        AntennaCalulator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AntennaCalulator)
        self.statusbar.setObjectName("statusbar")
        AntennaCalulator.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(AntennaCalulator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 21))
        self.menubar.setObjectName("menubar")
        AntennaCalulator.setMenuBar(self.menubar)

        self.retranslateUi(AntennaCalulator)
        QtCore.QMetaObject.connectSlotsByName(AntennaCalulator)

    def retranslateUi(self, AntennaCalulator):
        _translate = QtCore.QCoreApplication.translate
        AntennaCalulator.setWindowTitle(_translate("AntennaCalulator", "Antenna Calculator"))
        self.Calculate.setText(_translate("AntennaCalulator", "Calculate"))
        self.Quit.setText(_translate("AntennaCalulator", "Quit"))
        self.label.setText(_translate("AntennaCalulator", "Enter Freq."))
        self.label_2.setText(_translate("AntennaCalulator", "Enter h"))
        self.label_3.setText(_translate("AntennaCalulator", "Enter E_r"))
        self.label_4.setText(_translate("AntennaCalulator", "MHz"))
        self.label_6.setText(_translate("AntennaCalulator", "mm"))
        self.label_7.setText(_translate("AntennaCalulator", "Antenna Width"))
        self.label_8.setText(_translate("AntennaCalulator", "Antenna Length"))
        self.label_9.setText(_translate("AntennaCalulator", "mm"))
        self.label_10.setText(_translate("AntennaCalulator", "mm"))
