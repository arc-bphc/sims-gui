# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finger.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.setEnabled(True)
        loginWindow.resize(960, 669)
        loginWindow.setStyleSheet("QWidget {background-color: white}\n"
"QPushButton {padding: 20px}")
        self.gridLayout_2 = QtWidgets.QGridLayout(loginWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(loginWindow)
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(loginWindow)
        self.label.setMaximumSize(QtCore.QSize(400, 300))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/fingerprint-icon.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(loginWindow)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.label_4.setText(_translate("loginWindow", "Place your finger on the sensor"))
        self.label_3.setText(_translate("loginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#005500;\">VERIFIED</span></p></body></html>"))

