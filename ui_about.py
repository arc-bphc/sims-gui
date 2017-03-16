# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_aboutWindow(object):
    def setupUi(self, aboutWindow):
        aboutWindow.setObjectName(_fromUtf8("aboutWindow"))
        aboutWindow.resize(1174, 638)
        aboutWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.gridLayout_2 = QtGui.QGridLayout(aboutWindow)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(aboutWindow)
        self.label_4.setStyleSheet(_fromUtf8("font: 18pt \"Noto Sans\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 2)
        self.label_6 = QtGui.QLabel(aboutWindow)
        self.label_6.setMaximumSize(QtCore.QSize(350, 300))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("images/arclogo.png")))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 6, 1)
        self.label_3 = QtGui.QLabel(aboutWindow)
        self.label_3.setStyleSheet(_fromUtf8("font: 18pt \"Noto Sans\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.label = QtGui.QLabel(aboutWindow)
        self.label.setStyleSheet(_fromUtf8("font: 75 48pt \"Noto Sans\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        self.label_7 = QtGui.QLabel(aboutWindow)
        self.label_7.setStyleSheet(_fromUtf8("font: 18pt \"Noto Sans\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 2)
        self.label_5 = QtGui.QLabel(aboutWindow)
        self.label_5.setStyleSheet(_fromUtf8("font: italic bold 18pt \"Noto Sans\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 1, 1, 1)
        self.closeButton = QtGui.QPushButton(aboutWindow)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 8, 1, 1, 1)
        self.label_2 = QtGui.QLabel(aboutWindow)
        self.label_2.setStyleSheet(_fromUtf8("font: bold 18pt \"Noto Sans\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 2, 1, 1)

        self.retranslateUi(aboutWindow)
        QtCore.QMetaObject.connectSlotsByName(aboutWindow)

    def retranslateUi(self, aboutWindow):
        aboutWindow.setWindowTitle(_translate("aboutWindow", "Form", None))
        self.label_4.setText(_translate("aboutWindow", "Written in Python using PyQt4 and SQLite", None))
        self.label_3.setText(_translate("aboutWindow", "Developed by Arnav Dhamija and Yashdeep Thorat", None))
        self.label.setText(_translate("aboutWindow", "SIMS Alpha", None))
        self.label_7.setText(_translate("aboutWindow", "Automation & Robotics Club, BITS Pilani, Hyderabad Campus", None))
        self.label_5.setText(_translate("aboutWindow", "v0.1a", None))
        self.closeButton.setText(_translate("aboutWindow", "Close", None))
        self.label_2.setText(_translate("aboutWindow", "Smart Inventory Management System", None))

