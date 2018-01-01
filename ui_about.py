# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Mon Jan  1 14:43:32 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutWindow(object):
    def setupUi(self, aboutWindow):
        aboutWindow.setObjectName("aboutWindow")
        aboutWindow.resize(1205, 638)
        aboutWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(aboutWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(aboutWindow)
        self.label_4.setStyleSheet("font: 18pt \"Noto Sans\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(aboutWindow)
        self.label_6.setMaximumSize(QtCore.QSize(350, 300))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/arclogo.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 6, 1)
        self.label_3 = QtWidgets.QLabel(aboutWindow)
        self.label_3.setStyleSheet("font: 18pt \"Noto Sans\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(aboutWindow)
        self.label.setStyleSheet("font: 75 48pt \"Noto Sans\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(aboutWindow)
        self.label_7.setStyleSheet("font: 18pt \"Noto Sans\";")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(aboutWindow)
        self.label_5.setStyleSheet("font: italic bold 18pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 1, 1, 1)
        self.closeButton = QtWidgets.QPushButton(aboutWindow)
        self.closeButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 8, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(aboutWindow)
        self.label_2.setStyleSheet("font: bold 18pt \"Noto Sans\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 2, 1, 1)

        self.retranslateUi(aboutWindow)
        QtCore.QMetaObject.connectSlotsByName(aboutWindow)

    def retranslateUi(self, aboutWindow):
        _translate = QtCore.QCoreApplication.translate
        aboutWindow.setWindowTitle(_translate("aboutWindow", "Form"))
        self.label_4.setText(_translate("aboutWindow", "Written in Python3 using PyQt5 and SQLite"))
        self.label_3.setText(_translate("aboutWindow", "<html><head/><body><p>Developed by Ebin Philip, Arnav Dhamija, Yashdeep Thorat</p></body></html>"))
        self.label.setText(_translate("aboutWindow", "SIMS Alpha"))
        self.label_7.setText(_translate("aboutWindow", "Automation & Robotics Club, BITS Pilani, Hyderabad Campus"))
        self.label_5.setText(_translate("aboutWindow", "v1.0"))
        self.closeButton.setText(_translate("aboutWindow", "Close"))
        self.label_2.setText(_translate("aboutWindow", "Smart Inventory Management System"))

