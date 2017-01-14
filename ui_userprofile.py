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
        userWindow.resize(1082, 775)
        userWindow.setStyleSheet(_fromUtf8("QPushButton {padding: 10px}\n"
"QWidget {background-color: rgb(255, 255, 255)}\n"
""))
        self.gridLayout_2 = QtGui.QGridLayout(userWindow)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_2 = QtGui.QPushButton(userWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ChevronLeft-128.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label = QtGui.QLabel(userWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_2 = QtGui.QLabel(userWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(120, 120))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("index.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3 = QtGui.QLabel(userWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(175, 150))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("13015184_719298964879056_6631447530178360880_n.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.inventoryButton = QtGui.QPushButton(userWindow)
        self.inventoryButton.setObjectName(_fromUtf8("inventoryButton"))
        self.gridLayout.addWidget(self.inventoryButton, 3, 1, 1, 1, QtCore.Qt.AlignTop)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(userWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("system-shutdown"))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.requestButton = QtGui.QPushButton(userWindow)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("save"))
        self.requestButton.setIcon(icon)
        self.requestButton.setObjectName(_fromUtf8("requestButton"))
        self.gridLayout.addWidget(self.requestButton, 5, 1, 1, 1, QtCore.Qt.AlignTop)
        self.resetPinButton = QtGui.QPushButton(userWindow)
        self.resetPinButton.setObjectName(_fromUtf8("resetPinButton"))
        self.gridLayout.addWidget(self.resetPinButton, 7, 1, 1, 1, QtCore.Qt.AlignTop)
        self.editDetailsButton = QtGui.QPushButton(userWindow)
        self.editDetailsButton.setObjectName(_fromUtf8("editDetailsButton"))
        self.gridLayout.addWidget(self.editDetailsButton, 6, 1, 1, 1, QtCore.Qt.AlignTop)
        self.viewItemsButton = QtGui.QPushButton(userWindow)
        self.viewItemsButton.setObjectName(_fromUtf8("viewItemsButton"))
        self.gridLayout.addWidget(self.viewItemsButton, 4, 1, 1, 1, QtCore.Qt.AlignTop)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.lockButton = QtGui.QPushButton(userWindow)
        self.lockButton.setObjectName(_fromUtf8("lockButton"))
        self.gridLayout_2.addWidget(self.lockButton, 3, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)

        self.retranslateUi(userWindow)
        QtCore.QMetaObject.connectSlotsByName(userWindow)

    def retranslateUi(self, userWindow):
        userWindow.setWindowTitle(_translate("userWindow", "Dialog", None))
        self.pushButton_2.setText(_translate("userWindow", "Back", None))
        self.label.setText(_translate("userWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Welcome, ARCUser</span></p></body></html>", None))
        self.inventoryButton.setText(_translate("userWindow", "Inventory", None))
        self.pushButton.setText(_translate("userWindow", "Logout", None))
        self.requestButton.setText(_translate("userWindow", "Purchase Request", None))
        self.resetPinButton.setText(_translate("userWindow", "Reset PIN", None))
        self.editDetailsButton.setText(_translate("userWindow", "Edit Details", None))
        self.viewItemsButton.setText(_translate("userWindow", "View My Items", None))
        self.lockButton.setText(_translate("userWindow", "🔒 Lock", None))

