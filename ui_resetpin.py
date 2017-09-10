# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resetpin.ui'
#
# Created: Sun Sep 10 11:23:29 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_resetPinWindow(object):
    def setupUi(self, resetPinWindow):
        resetPinWindow.setObjectName("resetPinWindow")
        resetPinWindow.resize(935, 585)
        resetPinWindow.setStyleSheet("QPushButton {padding: 10px}\n"
"QWidget {background-color: rgb(255, 255, 255)}\n"
"")
        self.gridLayout_3 = QtWidgets.QGridLayout(resetPinWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(resetPinWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("font: 24pt \"Noto Sans\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(resetPinWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet("font: 75 20pt \"Noto Sans\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 4, 1, 1)
        self.currentPwd = QtWidgets.QLineEdit(resetPinWindow)
        self.currentPwd.setMaxLength(4)
        self.currentPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.currentPwd.setObjectName("currentPwd")
        self.gridLayout.addWidget(self.currentPwd, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(resetPinWindow)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(resetPinWindow)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.newPwd = QtWidgets.QLineEdit(resetPinWindow)
        self.newPwd.setMaxLength(4)
        self.newPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPwd.setObjectName("newPwd")
        self.gridLayout.addWidget(self.newPwd, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 3, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(resetPinWindow)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 5, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 3, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(resetPinWindow)
        QtCore.QMetaObject.connectSlotsByName(resetPinWindow)

    def retranslateUi(self, resetPinWindow):
        _translate = QtCore.QCoreApplication.translate
        resetPinWindow.setWindowTitle(_translate("resetPinWindow", "Form"))
        self.label_5.setText(_translate("resetPinWindow", "Reset PIN"))
        self.label_6.setText(_translate("resetPinWindow", "This operation cannot be reversed!"))
        self.label.setText(_translate("resetPinWindow", "Current PIN"))
        self.label_2.setText(_translate("resetPinWindow", "New PIN"))

