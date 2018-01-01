# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdetails.ui'
#
# Created: Mon Jan  1 13:39:45 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editDetailsWindow(object):
    def setupUi(self, editDetailsWindow):
        editDetailsWindow.setObjectName("editDetailsWindow")
        editDetailsWindow.resize(1077, 788)
        editDetailsWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        editDetailsWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(editDetailsWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(editDetailsWindow)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(editDetailsWindow)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.phoneCall = QtWidgets.QLineEdit(editDetailsWindow)
        self.phoneCall.setObjectName("phoneCall")
        self.gridLayout_2.addWidget(self.phoneCall, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(editDetailsWindow)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(editDetailsWindow)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.email = QtWidgets.QLineEdit(editDetailsWindow)
        self.email.setObjectName("email")
        self.gridLayout_2.addWidget(self.email, 1, 1, 1, 1)
        self.name = QtWidgets.QLineEdit(editDetailsWindow)
        self.name.setEnabled(False)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(editDetailsWindow)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.phoneWhatsApp = QtWidgets.QLineEdit(editDetailsWindow)
        self.phoneWhatsApp.setObjectName("phoneWhatsApp")
        self.gridLayout_2.addWidget(self.phoneWhatsApp, 3, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(editDetailsWindow)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)
        self.roomNumber = QtWidgets.QLineEdit(editDetailsWindow)
        self.roomNumber.setObjectName("roomNumber")
        self.gridLayout_2.addWidget(self.roomNumber, 4, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(editDetailsWindow)
        self.label_10.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)

        self.retranslateUi(editDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(editDetailsWindow)
        editDetailsWindow.setTabOrder(self.name, self.email)
        editDetailsWindow.setTabOrder(self.email, self.phoneCall)
        editDetailsWindow.setTabOrder(self.phoneCall, self.phoneWhatsApp)
        editDetailsWindow.setTabOrder(self.phoneWhatsApp, self.roomNumber)

    def retranslateUi(self, editDetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        editDetailsWindow.setWindowTitle(_translate("editDetailsWindow", "Form"))
        self.label_7.setText(_translate("editDetailsWindow", "Phone (Calling)"))
        self.label_8.setText(_translate("editDetailsWindow", "Phone (WhatsApp)"))
        self.label_6.setText(_translate("editDetailsWindow", "Email"))
        self.label_5.setText(_translate("editDetailsWindow", "Name"))
        self.label_9.setText(_translate("editDetailsWindow", "Room Number"))
        self.label_10.setText(_translate("editDetailsWindow", "Edit User Details"))

