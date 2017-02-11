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
        self.resetPinButton.setMinimumSize(QtCore.QSize(400, 0))
        self.resetPinButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.resetPinButton.setObjectName(_fromUtf8("resetPinButton"))
        self.gridLayout.addWidget(self.resetPinButton, 9, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 11, 1, 1, 1)
        self.welcomeLabel = QtGui.QLabel(userWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcomeLabel.sizePolicy().hasHeightForWidth())
        self.welcomeLabel.setSizePolicy(sizePolicy)
        self.welcomeLabel.setObjectName(_fromUtf8("welcomeLabel"))
        self.gridLayout.addWidget(self.welcomeLabel, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        self.inventoryButton = QtGui.QPushButton(userWindow)
        self.inventoryButton.setMinimumSize(QtCore.QSize(400, 0))
        self.inventoryButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.inventoryButton.setObjectName(_fromUtf8("inventoryButton"))
        self.gridLayout.addWidget(self.inventoryButton, 5, 1, 1, 1)
        self.requestButton = QtGui.QPushButton(userWindow)
        self.requestButton.setMinimumSize(QtCore.QSize(400, 0))
        self.requestButton.setMaximumSize(QtCore.QSize(400, 16777215))
        icon = QtGui.QIcon.fromTheme(_fromUtf8("save"))
        self.requestButton.setIcon(icon)
        self.requestButton.setObjectName(_fromUtf8("requestButton"))
        self.gridLayout.addWidget(self.requestButton, 7, 1, 1, 1)
        self.editDetailsButton = QtGui.QPushButton(userWindow)
        self.editDetailsButton.setMinimumSize(QtCore.QSize(400, 0))
        self.editDetailsButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.editDetailsButton.setObjectName(_fromUtf8("editDetailsButton"))
        self.gridLayout.addWidget(self.editDetailsButton, 8, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 0, 1, 1)
        self.cartButton = QtGui.QPushButton(userWindow)
        self.cartButton.setMinimumSize(QtCore.QSize(400, 0))
        self.cartButton.setMaximumSize(QtCore.QSize(400, 16777215))
        self.cartButton.setObjectName(_fromUtf8("cartButton"))
        self.gridLayout.addWidget(self.cartButton, 6, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        self.profilePic = QtGui.QLabel(userWindow)
        self.profilePic.setMinimumSize(QtCore.QSize(75, 75))
        self.profilePic.setMaximumSize(QtCore.QSize(150, 150))
        self.profilePic.setText(_fromUtf8(""))
        self.profilePic.setPixmap(QtGui.QPixmap(_fromUtf8("index.png")))
        self.profilePic.setScaledContents(True)
        self.profilePic.setObjectName(_fromUtf8("profilePic"))
        self.gridLayout.addWidget(self.profilePic, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton = QtGui.QPushButton(userWindow)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 150))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(userWindow)
        QtCore.QMetaObject.connectSlotsByName(userWindow)

    def retranslateUi(self, userWindow):
        userWindow.setWindowTitle(_translate("userWindow", "Dialog", None))
        self.resetPinButton.setText(_translate("userWindow", "Reset PIN", None))
        self.welcomeLabel.setText(_translate("userWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">Welcome, ARCUser</span></p></body></html>", None))
        self.inventoryButton.setText(_translate("userWindow", "Inventory", None))
        self.requestButton.setText(_translate("userWindow", "Purchase Request", None))
        self.editDetailsButton.setText(_translate("userWindow", "Edit Details", None))
        self.cartButton.setText(_translate("userWindow", "View Cart", None))

