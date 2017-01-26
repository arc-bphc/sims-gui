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
        self.inventoryButton = QtGui.QPushButton(userWindow)
        self.inventoryButton.setObjectName(_fromUtf8("inventoryButton"))
        self.gridLayout.addWidget(self.inventoryButton, 3, 1, 1, 1)
        self.editDetailsButton = QtGui.QPushButton(userWindow)
        self.editDetailsButton.setObjectName(_fromUtf8("editDetailsButton"))
        self.gridLayout.addWidget(self.editDetailsButton, 6, 1, 1, 1)
        self.viewItemsButton = QtGui.QPushButton(userWindow)
        self.viewItemsButton.setObjectName(_fromUtf8("viewItemsButton"))
        self.gridLayout.addWidget(self.viewItemsButton, 4, 1, 1, 1)
        self.resetPinButton = QtGui.QPushButton(userWindow)
        self.resetPinButton.setObjectName(_fromUtf8("resetPinButton"))
        self.gridLayout.addWidget(self.resetPinButton, 7, 1, 1, 1)
        self.widget = QtGui.QWidget(userWindow)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("index.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout.addWidget(self.widget, 0, 2, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.label_3 = QtGui.QLabel(userWindow)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setMaximumSize(QtCore.QSize(175, 150))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("13015184_719298964879056_6631447530178360880_n.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label = QtGui.QLabel(userWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.requestButton = QtGui.QPushButton(userWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("save"))
        self.requestButton.setIcon(icon)
        self.requestButton.setObjectName(_fromUtf8("requestButton"))
        self.gridLayout.addWidget(self.requestButton, 5, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(userWindow)
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ChevronLeft-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(userWindow)
        QtCore.QMetaObject.connectSlotsByName(userWindow)

    def retranslateUi(self, userWindow):
        userWindow.setWindowTitle(_translate("userWindow", "Dialog", None))
        self.inventoryButton.setText(_translate("userWindow", "Inventory", None))
        self.editDetailsButton.setText(_translate("userWindow", "Edit Details", None))
        self.viewItemsButton.setText(_translate("userWindow", "View My Items", None))
        self.resetPinButton.setText(_translate("userWindow", "Reset PIN", None))
        self.label.setText(_translate("userWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Welcome, ARCUser</span></p></body></html>", None))
        self.requestButton.setText(_translate("userWindow", "Purchase Request", None))

