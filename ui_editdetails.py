# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdetails.ui'
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

class Ui_editDetailsWindow(object):
    def setupUi(self, editDetailsWindow):
        editDetailsWindow.setObjectName(_fromUtf8("editDetailsWindow"))
        editDetailsWindow.resize(1077, 788)
        editDetailsWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        editDetailsWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: white}\n"
""))
        self.gridLayout_3 = QtGui.QGridLayout(editDetailsWindow)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(editDetailsWindow)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_7 = QtGui.QLabel(editDetailsWindow)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.phoneCall = QtGui.QLineEdit(editDetailsWindow)
        self.phoneCall.setObjectName(_fromUtf8("phoneCall"))
        self.gridLayout_2.addWidget(self.phoneCall, 2, 1, 1, 1)
        self.label_8 = QtGui.QLabel(editDetailsWindow)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_6 = QtGui.QLabel(editDetailsWindow)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.email = QtGui.QLineEdit(editDetailsWindow)
        self.email.setObjectName(_fromUtf8("email"))
        self.gridLayout_2.addWidget(self.email, 1, 1, 1, 1)
        self.name = QtGui.QLineEdit(editDetailsWindow)
        self.name.setEnabled(False)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout_2.addWidget(self.name, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(editDetailsWindow)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.phoneWhatsApp = QtGui.QLineEdit(editDetailsWindow)
        self.phoneWhatsApp.setObjectName(_fromUtf8("phoneWhatsApp"))
        self.gridLayout_2.addWidget(self.phoneWhatsApp, 3, 1, 1, 1)
        self.label_9 = QtGui.QLabel(editDetailsWindow)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)
        self.roomNumber = QtGui.QLineEdit(editDetailsWindow)
        self.roomNumber.setObjectName(_fromUtf8("roomNumber"))
        self.gridLayout_2.addWidget(self.roomNumber, 4, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.label_10 = QtGui.QLabel(editDetailsWindow)
        self.label_10.setStyleSheet(_fromUtf8("font: 24pt \"Noto Sans\";"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)

        self.retranslateUi(editDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(editDetailsWindow)
        editDetailsWindow.setTabOrder(self.name, self.email)
        editDetailsWindow.setTabOrder(self.email, self.phoneCall)
        editDetailsWindow.setTabOrder(self.phoneCall, self.phoneWhatsApp)
        editDetailsWindow.setTabOrder(self.phoneWhatsApp, self.roomNumber)

    def retranslateUi(self, editDetailsWindow):
        editDetailsWindow.setWindowTitle(_translate("editDetailsWindow", "Form", None))
        self.label_7.setText(_translate("editDetailsWindow", "Phone (Calling)", None))
        self.label_8.setText(_translate("editDetailsWindow", "Phone (WhatsApp)", None))
        self.label_6.setText(_translate("editDetailsWindow", "Email", None))
        self.label_5.setText(_translate("editDetailsWindow", "Name", None))
        self.label_9.setText(_translate("editDetailsWindow", "Room Number", None))
        self.label_10.setText(_translate("editDetailsWindow", "Edit User Details", None))

