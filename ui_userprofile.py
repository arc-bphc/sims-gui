# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userprofile.ui'
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

class Ui_userWindow(object):
    def setupUi(self, userWindow):
        userWindow.setObjectName(_fromUtf8("userWindow"))
        userWindow.resize(972, 733)
        userWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: rgb(255, 255, 255)}\n"
""))
        self.gridLayout_2 = QtGui.QGridLayout(userWindow)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setVerticalSpacing(16)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.resetPinButton = QtGui.QPushButton(userWindow)
        self.resetPinButton.setObjectName(_fromUtf8("resetPinButton"))
        self.gridLayout.addWidget(self.resetPinButton, 6, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 1, 1, 1)
        self.label = QtGui.QLabel(userWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 1, 1, 1)
        self.inventoryButton = QtGui.QPushButton(userWindow)
        self.inventoryButton.setObjectName(_fromUtf8("inventoryButton"))
        self.gridLayout.addWidget(self.inventoryButton, 3, 1, 1, 1)
        self.requestButton = QtGui.QPushButton(userWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("save"))
        self.requestButton.setIcon(icon)
        self.requestButton.setObjectName(_fromUtf8("requestButton"))
        self.gridLayout.addWidget(self.requestButton, 4, 1, 1, 1)
        self.editDetailsButton = QtGui.QPushButton(userWindow)
        self.editDetailsButton.setObjectName(_fromUtf8("editDetailsButton"))
        self.gridLayout.addWidget(self.editDetailsButton, 5, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(userWindow)
        QtCore.QMetaObject.connectSlotsByName(userWindow)

    def retranslateUi(self, userWindow):
        userWindow.setWindowTitle(_translate("userWindow", "Dialog", None))
        self.resetPinButton.setText(_translate("userWindow", "Reset PIN", None))
        self.label.setText(_translate("userWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">Welcome, ARCUser</span></p></body></html>", None))
        self.inventoryButton.setText(_translate("userWindow", "Inventory", None))
        self.requestButton.setText(_translate("userWindow", "Purchase Request", None))
        self.editDetailsButton.setText(_translate("userWindow", "Edit Details", None))

